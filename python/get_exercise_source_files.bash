#!/usr/bin/env bash

# Set invalid password to intentionally hide the real one.
# Contact Trey Hunner (trey@pythonmorsels.com) to get the real
# password or take one of his Python courses on O'Reilly Learning! 
password=secret_password

# Retrieve exercise source file howdy.py.
uv run --with requests \
  python get_exercise_source_file.py \
  --password $password \
  https://modern-testing.pym.dev/_downloads/c16bccf706c04a8a443ccc5c1eb3b3e7/howdy.py

# Retrieve exercise source file dollars.py.
uv run --with requests \
  python get_exercise_source_file.py \
  --password $password \
  https://modern-testing.pym.dev/_downloads/6c71c5a6c266cbe29d7755889443b8c2/dollars.py
