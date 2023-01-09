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

`.\venv\Scripts\alembic.exe init alembic`

- MacOS or Linux

`./venv/bin/alembic init alembic`

### Alembic Settings

1. Edit the alembic.ini file  
I only changed the `sqlalchemy.url =` line to `sqlalchemy.url = sqlite3:///sqlite3.db` to use/create an sqlite3 database file
relative to the current project folder.

2. Create the initial Alembic revision  
`alembic revision -m "create initial tables"`  
(Note the newly created Python file name and the path)

3. Make the edits to the newly created Python file from the previous step  
Since this is the first revision, you won't have any downgrade options--leave `pass` in for the downgrade function.
Use the op.create_table() function to define your table and its columns per the SQLAlchemy documentation 
