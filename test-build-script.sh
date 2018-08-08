#!/usr/bin/env bash

rm -rf public
export CI_PROJECT_NAME=public
export CI_PROJECT_URL=localhost:8000
cat build_wiki.py | python - public README.md
python3 -m http.server