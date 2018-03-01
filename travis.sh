#!/bin/sh
parallel ::: 'pip install pipenv && pipenv install --dev' \
             'npm install -g grunt-cli && npm install'
