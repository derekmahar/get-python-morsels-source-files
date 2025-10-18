#!/usr/bin/env uvrs
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "requests",
# ]
# [tool.uv]
# exclude-newer = "2025-10-18T16:44:57Z"
# ///
import argparse
import requests
import json
from urllib.parse import urlparse, urlunparse
from pathlib import Path

def filename_from_url(url: str) -> str:
    path = urlparse(url).path
    name = Path(path).name
    return name or "downloaded.file"

def login_url_from_file_url(file_url: str) -> str:
    parsed = urlparse(file_url)
    scheme = parsed.scheme or "https"
    domain = parsed.netloc
    return urlunparse((scheme, domain, "", "", "", ""))

def main():
    parser = argparse.ArgumentParser(
        description="Submit form (fields 'form-name' and 'password'), save cookie, then download a file using that cookie."
    )
    parser.add_argument("file_url", help="URL of the file to download (protected resource)")
    parser.add_argument("--password", required=True, help="Password value for the form (named parameter)")
    args = parser.parse_args()

    file_url = args.file_url
    login_url = login_url_from_file_url(file_url)    # derived from file URL domain
    cookie_file = Path("cookies.json")               # fixed default
    output_path = Path(filename_from_url(file_url))  # renamed variable

    # Submit the login form and collect cookies
    session = requests.Session()
    form_data = {
        "form-name": "form 1",
        "password": args.password
    }
    login_response = session.post(login_url, data=form_data)
    login_response.raise_for_status()

    get_file_response = session.get(file_url, stream=True)
    get_file_response.raise_for_status()

    # Save the file using name derived from file URL
    with output_path.open("wb") as output_file:
        for chunk in get_file_response.iter_content(chunk_size=8192):
            if chunk:
                output_file.write(chunk)

if __name__ == "__main__":
    main()
