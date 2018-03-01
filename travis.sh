#!/bin/sh
parallel ::: 'pip install --upgrade pip && pip install pipenv && pipenv install --dev' \
             'npm install --global npm && npm install -g grunt-cli && npm install'
