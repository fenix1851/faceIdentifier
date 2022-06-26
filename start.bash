#!/bin/bash

source ./school/bin/activate
echo "The current python directory is:"
which python
echo "Installing dependences..."
pip install -r code/requirements.txt
echo "Done!"
echo "Starting web server..."
cd ./code/devScripts/
uvicorn fastApi:app --reload --host localhost --port 8080
