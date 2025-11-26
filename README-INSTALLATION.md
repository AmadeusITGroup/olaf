# OLAF Installation Guide

Simple installation guide for the OLAF framework.

## Recommended Installation Method: VSCode/Windsurf Extension

The easiest way to install OLAF is through our VSCode extension, which works with VSCode, Windsurf and Kiro IDEs. When installed, it will automatically install OLAF components and create the .olaf/ folder in your workspace. 
if you install OLaf through manual installation, you will need to copy the olaf-core and olaf-data folders to your project directory under .olaf/ folder.

### 1. Install the Extension

#### From VSCode Marketplace
1. Open VSCode, Windsurf or Kiro IDE
2. Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS) to open Extensions view
3. Search for "OLAF"
4. Click "Install"

#### From VSIX Package
1. Download the latest `.vsix` file from [GitHub Releases](https://github.com/AmadeusITGroup/olaf/releases)
2. Open VSCode, Windsurf or Kiro IDE
3. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
4. Type "Extensions: Install from VSIX"
5. Select the downloaded `.vsix` file

### 2. Install OLAF Components

1. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Type "OLAF: Install" and press Enter
3. Select installation scope:
   - **Project**: Install for the current project (recommended)
    - **User**: Install for the current user 

4. The extension will automatically download the latest release and install all components

### 3. Verify Installation

- Check the presence of olaf-core/ and olaf-data/ and docs/ folders in your workspace under .olaf/ folder. 

## Alternative: Manual Installation

If you prefer manual installation or the extension is not available:

### 1. Download the ZIP file 

- Go to the latest release [GitHub Releases](https://github.com/AmadeusITGroup/olaf/releases)
- Download the Source code (zip or tar.gz file)

### 2. Extract the ZIP file
- Extract to any location on your computer
- Navigate into the extracted folder and you will find the following folders:
- `olaf-core/` - Core prompts, templates, and reference materials
- `olaf-data/` - Data storage and project files
- `docs/` - Complete documentation and guides
- `.github/` - GitHub integration and workflow configurations
- `.windsurf/` - Windsurf IDE configuration and workflows
- `.kiro/` - for kiro IDE with hooks/ and steering/ folders.

### 3. Copy the framework folders
- Copy these folders to your project directory under .olaf/ folder:
- `olaf-core/` - Core prompts, templates, and reference materials
- `olaf-data/` - Data storage and project files
- `docs/` - Complete documentation and guides

- Copy these folders depending on which IDE you are using directly under your project directory:
- `.github/` - GitHub integration and workflow configurations
- `.windsurf/` - Windsurf IDE configuration and workflows
- `.kiro/` - for kiro IDE with hooks/ and steering/ folders.
P.S: you can copy all three folders, it does not affect the functioning of the framework.


## That's it!

You now have the OLAF framework installed in your project.

## What You Get
 When the installation is complete, you will have a **.olaf/** folder with the following structure:
- **olaf-core/** - Core prompts, templates, and reference materials
- **olaf-data/** - Data storage and project files
- **docs/** - Complete documentation and guides
 and depending on the IDE you are using, you will have additional folders:
- **.github/** - GitHub integration and workflow configurations
- **.windsurf/** - Windsurf rules and workflows
- **.kiro/** - Kiro hooks and steering  

## Extension Features



## Updating OLAF

### With Extension (Recommended)
1. Open VSCode, Windsurf or Kiro IDE 
2- make sure you have hte latest version of the installer, if not update it in the extension marketplace by uninstalling and installing it again.
3. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)

### Manual Update
To update manually:
1. Download the ZIP file again (same URL)
2. Extract and copy the folders
3. Replace existing files and folders with the new ones

## Older Versions

For older versions, you have two options:

### GitHub Releases (if available)
Check for releases at: `https://github.com/AmadeusITGroup/olaf/releases`



## Support
This is an experimental project and is not supported by Amadeus IT Group.
We do not provide any support for this project , but you can help us by reporting issues


For issues or questions:
- **GitHub Issues**: [Report bugs or request features](https://github.com/AmadeusITGroup/olaf/issues)
- **Documentation**: [Read the full documentation](https://github.com/AmadeusITGroup/olaf/wiki)
- Contact the OLAF team or repository maintainers
