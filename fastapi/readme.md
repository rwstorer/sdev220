# FastAPI

## Virtual Environment

### Create the Virtual Environment

`python -m venv ./venv`

### Activate the Virtual Environment

#### Windows Virtual Environment Activation

`.\venv\scripts\activate.bat` (if using cmd.exe)  
OR `.\venv\scripts\Activate.ps1` (if using PowerShell)

#### Linux and MacOS Virtual Environment Activation

`./venv/bin/activate`

### Confirm Virtual Environment Activation

*(venv)* should show at the start of your current shell's command line  
e.g. *(venv) C:\fastapi*

## Install Modules

1. `pip install fastapi`  
2. `pip install pydantic`  
3. `pip install sqlalchemy`  
4. `pip install alembic`

## Alembic

## Initialize Alembic

- Windows

`.\venv\bin\alembic init alembic`

- MacOS or Linux

`./venv/bin/alembic init alembic`

### Edit the Alembic INI File


