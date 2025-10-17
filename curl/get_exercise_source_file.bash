#!/usr/bin/env bash

# Enable strict mode.
set -euo pipefail
IFS=$'\n\t'

if [[ $# != 2 ]]
then
  echo "Usage: $0 [PASSWORD] [SOURCE_FILE_URL]"
  exit 1
fi

password=${1:-}
source_file_url=${2:-}

# Retrieve source file after submitting password form.
curl $source_file_url \
  --cookie "" \
  --form-string "form-name=form 1" \
  --form "password=$password" \
  --location-trusted \
  --remote-name \
  --silent
