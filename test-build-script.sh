#!/usr/bin/env bash

rm -rf public
cat build_wiki.py | python - public README.md