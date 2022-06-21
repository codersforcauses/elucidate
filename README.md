# Elucidate Winter 2022

![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/codersforcauses/elucidate)
![Codecov](https://img.shields.io/codecov/c/github/codersforcauses/elucidate)
![GitHub](https://img.shields.io/github/license/codersforcauses/elucidate)

![Alt](https://repobeats.axiom.co/api/embed/05fb1e2f61500a1be3ed92811dc0c097522d696d.svg "Repobeats analytics image")

## Introduction

### Technologies

Frontend

- Client
  - [NuxtJS](https://nuxtjs.org/)
  - [VueJS](https://vuejs.org/)
  - [Tailwind CSS](https://tailwindcss.com/)
  - [Axios](https://axios-http.com/)
- Testing
  - [Jest](https://jestjs.io/)
  - [Cypress](https://www.cypress.io/)
- Linting
  - [ESLint](https://eslint.org/)
- Formatting
  - [Prettier](https://prettier.io/)

Backend

- Webserver
  - [Django](https://www.djangoproject.com/)
  - [Django Rest Framework](https://www.django-rest-framework.org/)
  - [Apache](https://httpd.apache.org/)
- Database
  - [PostgreSQL](https://www.postgresql.org/)
  - [psycopg2](https://www.psycopg.org/)
- Linting
  - [flake8](https://flake8.pychond.org/)
- Formatting
  - [black](https://black.readthedocs.io/)

Other

- Documentation
  - [MkDocs](https://www.mkdocs.org/)
  - [MkDocstrings](https://mkdocstrings.github.io/)

## Getting started

### Setup Python development enivorment

Download and install Python from [here](https://www.python.org/downloads/). 3.10.5 is recommended, but any 3.10.x version should work.

#### Install Poetry

Poetry is a better Python package manager than pip. Download and install Poetry from [here](hhttps://python-poetry.org/docs/#installation).

Run the following command to configure virtual environments to be created in the project directory: `poetry config virtualenvs.in-project true`

#### Install Python dependencies

From the `server` directory, run the following command to install dependencies: `poetry install`

#### Activate the virtual environment

if you are using VS Code

- Press `Ctrl + Shift + P`
- Type in `Python: Select Interpreter`
- Choose the virtual environment in the project directory.
- Kill and restart the terminal.

If you are using a terminal

- Type in `source .venv/bin/activate`

### Setup NodeJS development environment

Install NodeJS from [here](https://nodejs.org/). 16.15.1 LTS is recommended, but any 16.x LTS version should work.

#### Install Yarn

Yarn is a better NodeJS package manager than npm. Download and install Yarn by using the following command: `npm install --global yarn`

#### Install NodeJS dependencies

From the `client` directory, run the following command to install dependencies: `yarn install`

## Setup commitlint

Commitlint is a tool that enforces your commits to be semantically formatted under the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format.

Commitlint should have been automatically installed by the `yarn install` command.

### Install Husky

Husky is a tool that automatically manages your git hooks. For this project, I have configured Husky to run `commitlint` before each commit.

Husky can be installed by using the following command in the `client` directory: `yarn prepare`.

Then run the following command from the root directory to make Husky executable: `chmod a+x .husky/commit-msg`.

### Conventional commit messages

Your commit messages **and** pull requests should be in the following format.

```none
Format: <type>(<scope>): <subject>

<scope> is optional, but highly recommended

Example
feat(core): add hat wobble
^--^^----^  ^------------^
|   |       |
|   |       +-> Subject: Summary in present tense and in lowercase.
|   +---------> scope: What is the scope of the change?
+-------------> Type: Description of the type of change.
```

### Types

More types can be added if neccessary in the `commitlint.config.js` file.

The commit type must be of the following:
feat: (new feature for the user, not a new feature for build script)
fix: (bug fix for the user, not a fix to a build script)
docs: (changes to the documentation)
style: (formatting, missing semi colons, etc; no production code change)
refactor: (refactoring production code, eg. renaming a variable)
test: (adding missing tests, refactoring tests; no production code change)
chore: (updating grunt tasks etc; no production code change)
build: (changes related to the build process)
perf: (increasing performance)
revert: (reverting a commit)
ci: (continuous integration related changes. We won't be using this; instead we will be using the ci and cd scopes for devops related changes.)

### Scopes

More scopes can be added if neccessary in the `commitlint.config.js` file. If there are overlapping scopes in your commit/pull request, choose the most suitable scope.

The commit scope must be of the following or blank:
core: (core functionality changes)
linting: (linting related changes)
frontend: (frontend changes)
backend: (backend changes)
auth: (authenication changes)
styles: (changes to the styling)
config: (changes to the configuration)
misc: (other miscellaneous changes)
ci: (changes to the continuous integration)
cd: (changes to the continuous delivery)

## Running tests

### Frontend

#### Jest tests

#### Cypress tests

### Backend

## Writing documentations
