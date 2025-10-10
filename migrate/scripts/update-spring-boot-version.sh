#!/usr/bin/env bash
# Update Spring Boot version in Maven (parent & BOM) and Gradle build files.
set -euo pipefail
TARGET_VERSION="$1"
if [ -z "$TARGET_VERSION" ]; then echo "Usage: $0 <target-version>"; exit 1; fi
shopt -s nullglob
for POM in $(find . -name pom.xml); do
  TMP=$(tr -d '\n' < "$POM")
  if [[ $TMP =~ (<parent>[^<]*<groupId>org.springframework.boot</groupId>[^<]*<artifactId>spring-boot-starter-parent</artifactId>[^<]*<version>)([^<]+)(</version>) ]]; then
    sed -i.bak -E "s/(<parent>[^"]*<groupId>org.springframework.boot<\/groupId>[^"]*<artifactId>spring-boot-starter-parent<\/artifactId>[^"]*<version>)([^<]+)(<\/version>)/\1${TARGET_VERSION}\3/" "$POM"
  fi
  if [[ $TMP =~ (<dependencyManagement>.*?spring-boot-dependencies.*?<version>)([^<]+)(</version>) ]]; then
    perl -0777 -pi -e "s/(<dependencyManagement>.*?spring-boot-dependencies.*?<version>)([^<]+)(<\/version>)/\1${TARGET_VERSION}\3/s" "$POM"
  fi
  rm -f "$POM.bak"
  echo "[Update-SB] Updated $POM"
done
for G in $(find . -name build.gradle -o -name build.gradle.kts); do
  sed -i.bak -E "s/(springBootVersion\s*=\s*")([^"]+)(")/\1${TARGET_VERSION}\3/" "$G" || true
  sed -i.bak -E "s/(id\("org.springframework.boot"\)\s*version\s*")([^"]+)(")/\1${TARGET_VERSION}\3/" "$G" || true
  rm -f "$G.bak"
  echo "[Update-SB] Updated $G"
done
