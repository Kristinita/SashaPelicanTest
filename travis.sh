#!/bin/sh
(pip install pipenv && pipenv install --dev) >& pip.log &
(npm install -g grunt-cli && npm install) >& npm.log &