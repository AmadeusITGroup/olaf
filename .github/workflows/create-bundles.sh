#!/bin/bash

set -e

MANIFEST_FILE="deployment-manifest.yml"
VERSION_TAG="$1"

if [ -z "$VERSION_TAG" ]; then
    echo "Usage: $0 <version_tag>"
    exit 1
fi

if ! command -v yq &> /dev/null; then
    echo "Installing yq..."
    sudo wget -qO /usr/local/bin/yq https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64
    sudo chmod +x /usr/local/bin/yq
fi

shopt -s globstar nullglob

# Function to parse directory destination mapping
# Input: "source-dir:destination" or "source-dir"
# Returns: source_dir destination_dir via global variables
parse_directory_mapping() {
    local dir_spec="$1"
    local default_dest="$2"

    if [[ "$dir_spec" == *":"* ]]; then
        # Custom destination specified
        source_dir="${dir_spec%%:*}"
        custom_dest="${dir_spec#*:}"

        if [[ "$custom_dest" == "." ]]; then
            # Copy to project root
            destination_dir=""
        elif [[ "$custom_dest" == *"/" ]]; then
            # Destination ends with /, copy contents to that directory
            destination_dir="${custom_dest%/}"
        else
            # Regular custom destination, copy directory into it
            destination_dir="$custom_dest"
        fi
    else
        # Use default destination
        source_dir="$dir_spec"
        destination_dir="$default_dest"
    fi
}

# Function to copy directory with custom destination support
copy_directory_to_destination() {
    local source="$1"
    local dest_base="$2"
    local temp_dir="$3"
    local preserve_source_name="$4"  # true/false

    if [[ ! -d "$source" ]]; then
        echo "Warning: Source directory '$source' does not exist"
        return
    fi

    local final_dest
    if [[ "$preserve_source_name" == "true" ]]; then
        # Copy directory into destination (e.g., source/.github -> dest/custom/.github)
        final_dest="$temp_dir/$dest_base/$(basename "$source")"
    else
        # Copy contents to destination (e.g., source/.github/* -> dest/custom/*)
        final_dest="$temp_dir/$dest_base"
    fi

    mkdir -p "$final_dest"

    # Copy all files from source to destination
    if [[ "$preserve_source_name" == "true" ]]; then
        cp -r "$source"/* "$final_dest/" 2>/dev/null || true
        echo "Copied directory: $source -> $final_dest"
    else
        cp -r "$source"/* "$final_dest/" 2>/dev/null || true
        echo "Copied directory contents: $source/* -> $final_dest/"
    fi
}

# Function to check if a file matches a pattern (supports ** for recursive matching)
matches_pattern() {
    local file="$1"
    local pattern="$2"

    # Handle ** recursive patterns
    if [[ "$pattern" == *"**"* ]]; then
        # For patterns like ".github/**/*" or ".github/workflows/**/*"
        # Find the position of /** in the pattern
        # Check for /**/* at the end first
        if [[ "$pattern" == *"/**/*" ]]; then
            # Pattern has /**/* at the end - this is a recursive match
            local prefix="${pattern%/**/*}"   # Everything before /**/*
            if [[ "$file" == "$prefix"/* ]]; then
                return 0
            fi
        elif [[ "$pattern" == *"/**/"* ]]; then
            # Pattern has /**/ in the middle
            local prefix="${pattern%%/**/*}"  # Everything before /**
            local suffix="${pattern#*/**/}"   # Everything after **/

            # If suffix is just *, match any file under prefix recursively
            if [[ "$suffix" == "*" ]]; then
                if [[ "$file" == "$prefix"/* ]]; then
                    return 0
                fi
            fi
        elif [[ "$pattern" == *"/**" ]]; then
            # Pattern ends with /** - match anything under the prefix
            local prefix="${pattern%/**}"
            if [[ "$file" == "$prefix"/* ]]; then
                return 0
            fi
        fi
    else
        # Handle regular glob patterns with single *
        # For patterns like "something-else/*instruction*"
        if [[ "$file" == $pattern ]]; then
            return 0
        fi

        # Special handling for patterns with directory and wildcard
        if [[ "$pattern" == *"/*"* ]]; then
            local dir_part="${pattern%/*}"
            local file_part="${pattern##*/}"
            local file_dir="$(dirname "$file")"
            local file_name="$(basename "$file")"

            # Check if file is in the right directory and matches the pattern
            if [[ "$file_dir" == "$dir_part" && "$file_name" == $file_part ]]; then
                return 0
            fi
        fi
    fi
    return 1
}

get_filtered_files() {
    local section="$1"
    local preserve_paths="$2"
    local root_folder="$3"
    local temp_dir="$4"

    # Get include and exclude patterns
    mapfile -t includes < <(yq eval "${section}.include_patterns[]" "$MANIFEST_FILE" 2>/dev/null || echo)
    mapfile -t excludes < <(yq eval "${section}.exclude_patterns[]" "$MANIFEST_FILE" 2>/dev/null || echo)

    # Also get directories and files if they exist
    mapfile -t directories < <(yq eval "${section}.directories[]" "$MANIFEST_FILE" 2>/dev/null || echo)
    mapfile -t files < <(yq eval "${section}.files[]" "$MANIFEST_FILE" 2>/dev/null || echo)

    local all_files=()

    # Collect all files from include patterns and directories
    # First, process all include patterns
    for pattern in "${includes[@]}"; do
        if [[ -n "$pattern" && "$pattern" != "null" ]]; then
            if [[ "$pattern" == *"**"* ]]; then
                # Handle recursive patterns like ".github/**/*"
                local base_dir="${pattern%%/**}"
                if [[ -d "$base_dir" ]]; then
                    while IFS= read -r -d '' file; do
                        file="${file#./}"
                        all_files+=("$file")
                    done < <(find "$base_dir" -type f -print0 2>/dev/null || true)
                fi
            else
                # Handle regular glob patterns
                shopt -s nullglob
                for f in $pattern; do
                    if [[ -f "$f" ]]; then
                        all_files+=("$f")
                    fi
                done
                shopt -u nullglob
            fi
        fi
    done

    # Process directories with custom destination support
    local processed_dirs=()  # Track directories we've already processed with custom destinations

    for dir_spec in "${directories[@]}"; do
        if [[ -n "$dir_spec" && "$dir_spec" != "null" ]]; then
            # Parse the directory mapping
            parse_directory_mapping "$dir_spec" "$root_folder"

            if [[ -d "$source_dir" ]]; then
                # Store info about this directory for later custom copying
                processed_dirs+=("$dir_spec")

                # Check if there are any include patterns for this directory
                local dir_patterns=()
                for pattern in "${includes[@]}"; do
                    if [[ -n "$pattern" && "$pattern" != "null" && "$pattern" == "$source_dir"* ]]; then
                        dir_patterns+=("$pattern")
                    fi
                done

                # Find all files in the directory
                while IFS= read -r -d '' file; do
                    file="${file#./}"
                    local include_file=false

                    # If there are specific include patterns for this directory, file must match one
                    if [[ ${#dir_patterns[@]} -gt 0 ]]; then
                        for pattern in "${dir_patterns[@]}"; do
                            if matches_pattern "$file" "$pattern"; then
                                include_file=true
                                break
                            fi
                        done
                    else
                        # If no specific patterns, include all files from the directory
                        include_file=true
                    fi

                    if [[ "$include_file" == "true" ]]; then
                        all_files+=("$file")
                    fi
                done < <(find "$source_dir" -type f -print0 2>/dev/null || true)
            fi
        fi
    done

    # Add individual files
    for file in "${files[@]}"; do
        if [[ -n "$file" && "$file" != "null" && -f "$file" ]]; then
            all_files+=("$file")
        fi
    done

    # Filter out excluded files
    local filtered=()
    for file in "${all_files[@]}"; do
        local skip=false
        for pattern in "${excludes[@]}"; do
            if [[ -n "$pattern" && "$pattern" != "null" ]]; then
                if matches_pattern "$file" "$pattern"; then
                    skip=true
                    break
                fi
            fi
        done
        if [[ "$skip" == "false" && -f "$file" ]]; then
            filtered+=("$file")
        fi
    done

    # Copy filtered files to destination
    for file in "${filtered[@]}"; do
        # Check if this file belongs to a directory with custom destination
        local custom_dest_used=false

        for dir_spec in "${processed_dirs[@]}"; do
            parse_directory_mapping "$dir_spec" "$root_folder"

            if [[ "$file" == "$source_dir"/* ]]; then
                # This file belongs to a directory with custom destination
                local relative_path="${file#$source_dir/}"
                local final_dest_dir

                if [[ -z "$destination_dir" ]]; then
                    # Copy to project root
                    final_dest_dir="$temp_dir"
                else
                    final_dest_dir="$temp_dir/$destination_dir"
                fi

                if [[ "$preserve_paths" == "true" ]]; then
                    dest="$final_dest_dir/$source_dir/$relative_path"
                else
                    dest="$final_dest_dir/$relative_path"
                fi

                mkdir -p "$(dirname "$dest")"
                cp "$file" "$dest"
                echo "Copied (custom dest): $file -> $dest"
                custom_dest_used=true
                break
            fi
        done

        # If no custom destination was used, use default logic
        if [[ "$custom_dest_used" == "false" ]]; then
            if [[ "$preserve_paths" == "true" ]]; then
                dest="$temp_dir/$root_folder/$file"
                mkdir -p "$(dirname "$dest")"
                cp "$file" "$dest"
                echo "Copied: $file -> $dest"
            else
                dest="$temp_dir/$root_folder/"
                mkdir -p "$dest"
                cp "$file" "$dest"
                echo "Copied: $file -> $dest$(basename "$file")"
            fi
        fi
    done
}

create_bundle() {
    local bundle_type="$1"
    local bundle_name="$2"
    local include_common="$3"

    local temp_dir="temp-${bundle_type}-bundle"
    rm -rf "$temp_dir"
    mkdir -p "$temp_dir"
    dest_root_folder=$(yq eval '.common.dest_root_folder' "$MANIFEST_FILE")

    if [ "$bundle_type" == "common" ]; then
        preserve_paths=true
        get_filtered_files ".common" "$preserve_paths" "$dest_root_folder" "$temp_dir"
    else
        preserve_paths=$(yq eval ".environments.${bundle_type}.bundle_structure.preserve_paths" "$MANIFEST_FILE")

        if [ "$include_common" = "true" ]; then
            # Put common files in root folder, so they don't overlap with env dest_root_folder
            get_filtered_files ".common" "true" "$dest_root_folder" "$temp_dir"
        fi
        get_filtered_files ".environments.${bundle_type}" "$preserve_paths" "$dest_root_folder" "$temp_dir"
    fi

    # Create the bundle
    (cd "$temp_dir" && zip -r "../${bundle_name}" .)
    rm -rf "$temp_dir"
    echo "Created: ${bundle_name}"
}

INCLUDE_COMMON=$(yq eval '.bundle_settings.include_common_in_environment_bundles' "$MANIFEST_FILE")
CREATE_COMMON=$(yq eval '.bundle_settings.create_common_bundle' "$MANIFEST_FILE")

if [ "$CREATE_COMMON" = "true" ]; then
    COMMON_BUNDLE_NAME=$(yq eval '.bundle_settings.naming.common_bundle' "$MANIFEST_FILE" | sed "s/{version}/$VERSION_TAG/g")
    create_bundle "common" "$COMMON_BUNDLE_NAME" "true"
fi

for env in $(yq eval '.environments | keys | .[]' "$MANIFEST_FILE"); do
    if [ "$INCLUDE_COMMON" = "true" ]; then
        BUNDLE_NAME=$(yq eval '.bundle_settings.naming.full_bundle' "$MANIFEST_FILE" | sed "s/{environment}/$env/g" | sed "s/{version}/$VERSION_TAG/g")
    else
        BUNDLE_NAME=$(yq eval '.bundle_settings.naming.environment_bundle' "$MANIFEST_FILE" | sed "s/{environment}/$env/g" | sed "s/{version}/$VERSION_TAG/g")
    fi
    create_bundle "$env" "$BUNDLE_NAME" "$INCLUDE_COMMON"
done

echo "Bundle creation completed!"