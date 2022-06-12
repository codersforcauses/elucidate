# Elucidate Backend

## Introduction

### Technologies

- Webserver
  - [Django](https://www.djangoproject.com/)
  - [Django Rest Framework](https://www.django-rest-framework.org/)
  - [Apache](https://httpd.apache.org/)
- Database
  - [PostgreSQL](https://www.postgresql.org/)
  - [psycopg2](https://www.psycopg.org/)
- Documentation
  - [MkDocs](https://www.mkdocs.org/)
  - [MkDocstrings](https://mkdocstrings.github.io/)

## Setting up your backend workspace

### 0. Install VS Code extensions

Recommended extensions:

- Python Extensions
  - ms-python.python
  - batisteo.vscode-django
  - KevinRose.vsc-python-indent
  - njpwerner.autodocstring
- Database Extensions
  - mtxr.sqltools
  - mtxr.sqltools-driver-pg
- API Testing
  - rangav.vscode-thunder-client
- Documentations
  - DavidAnson.vscode-markdownlint
  - yzhang.markdown-all-in-one
- Quality of Life Extensions
  - eamodio.gitlens
  - VisualStudioExptTeam.vscodeintellicode
  - christian-kohler.path-intellisense
  - oderwat.indent-rainbow

### 1. Install python 3.10.5 from [here](https://www.python.org/downloads/release/python-3105/)

### 2. Create a python virtual environment at the root of the backend folder

- Open VS Code from the root of this directory via `code .`
- Open the integrated terminal via `Ctrl + \``
- type in `python3 -m venv env`

### 3. Activate the virtual environment

if you are using VS Code

- Press `Ctrl + Shift + P`
- Type in `Python: Select Interpreter`
- Choose the virtual environment you created.
- Kill

If you are using a terminal

- Type in `source env/bin/activate`

### 4. Install dependencies

- Type in `pip install -r requirements.txt`

## Setting up a local PostgreSQL database
