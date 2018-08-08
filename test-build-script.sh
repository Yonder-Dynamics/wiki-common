#!/usr/bin/env bash

rm -rf public
cat build_wiki.py | python - public README.md
cd public
python3 -m http.server

