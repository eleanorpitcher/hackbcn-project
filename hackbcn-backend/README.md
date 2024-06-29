# Backend API


## Create a virtual environment:
python -m venv venv

## activate the virtual env
Set-ExecutionPolicy Unrestricted -Scope Process
venv\Scripts\activate

## Install your project dependencies:
pip install geopy mapillary

## deactivate
venv/Scripts/deactivate

## dump requirements
pip freeze > requirements.txt