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

# Use HTTPie to submit password form and retrieve source file.
http $source_file_url \
  form-name="form 1" \
  password="$password" \
  --download \
  --follow \
  --form \
  --quiet
