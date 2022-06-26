# Elucidate Winter 2022

![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/codersforcauses/elucidate)
![Codecov](https://img.shields.io/codecov/c/github/codersforcauses/elucidate)
![GitHub](https://img.shields.io/github/license/codersforcauses/elucidate)

![Alt](https://repobeats.axiom.co/api/embed/05fb1e2f61500a1be3ed92811dc0c097522d696d.svg "Repobeats analytics image")

## Table of Contents

- [Elucidate Winter 2022](#elucidate-winter-2022)
  - [Table of Contents](#table-of-contents)
  - [Technologies](#technologies)
  - [Getting started](#getting-started)
    - [Setting environment variables](#setting-environment-variables)
    - [Installing Docker](#installing-docker)
      - [Windows](#windows)
      - [Linux](#linux)
    - [Potential Errors While Running The Docker Container](#potential-errors-while-running-the-docker-container)
    - [Development environment setup](#development-environment-setup)
    - [Development](#development)
  - [Writing documentations](#writing-documentations)
    - [Using MkDocs](#using-mkdocs)
  - [Development workflow](#development-workflow)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->

## Technologies

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

### Setting environment variables

1. Create a copy of the `.env.example` file. (do not delete or replace the original `.env.example`).
2. Rename the copy to `.env`.

### Installing Docker

- [Download and Install Docker Documentation + Links](https://docs.docker.com/get-started/#download-and-install-docker)

#### Windows
- Once docker is installed, try running it. If docker-engine starts successfully, you can proceed.
- If your docker requires you to install WSL, you can easily do so by the following steps:
  - Open powershell with administrator privileges.
  - Type `WSL --install`
  - Restart your computer and try running `WSL` in cmd. If you get no error, then you are all set.
  - If you are asked to enable Windows Virtualisation Platform, or HyperV then:
    - Run `bcdedit /set hypervisorlaunchtype auto` in an admin privilege Powershell and restart your computer.
- Once docker-engine is running successfully, you can close the docker window as it should continue running in the background.

#### Linux
- If you are running Linux, Docker compose wil not be automatically installed. You will need to install it manually by following [this guide](https://docs.docker.com/compose/install/).

### Potential Errors While Running The Docker Container

- **Windows** : If the client and/or server continers fail to run due to `runtime.sh` not being found, then you need to change the line endings of the "runtime.sh" file (located in `docker/client/` and `docker/server`) from CRLF to LF.
  - You can do this in VS code by opening the `runtime.sh` file, and at the bottom-right corner, click on CRLF. A dialogue box pops up, click on LF and save the file.
  <p align="center">
    <img src="https://cdn.discordapp.com/attachments/831493951185485883/990558770209882162/unknown.png" height="50px"/>
  </p>
- **Mac** : 
- **Linux** : 

### Development environment setup

- Install the `Docker` and the `Remote - Containers` extensions.

![Docker extension](https://cdn.discordapp.com/attachments/701301203849576501/990567061350658128/unknown.png)
![Remote containers](https://cdn.discordapp.com/attachments/701301203849576501/990566970493661234/unknown.png)

- Navigate to the remote explorer tab

![Remote explorer tab](https://cdn.discordapp.com/attachments/701301203849576501/990565794536632340/unknown.png)

- Click the `Open Folder in Container` button and open the `client` folder.

![Client folder](https://cdn.discordapp.com/attachments/701301203849576501/990567691284795402/unknown.png)

- The first time this is launched, it may take up to 5 minutes to install and configure everything.
- After you are shown the workspace, there should be a pop up at the bottom right asking you to install recommended extensions. Click install.

![Install extensions](https://cdn.discordapp.com/attachments/701301203849576501/990568208878694400/unknown.png)

- Afterwards, close out of the remote container

![close](https://media.discordapp.net/attachments/701301203849576501/990568354895003648/unknown.png)
- Navigate to the remote explorer extension tab again. If you see the below, then the frontend workspace has been successfully configured.

- Press the plus symbol.

![client](https://cdn.discordapp.com/attachments/701301203849576501/990568519617888316/unknown.png)

- Click open folder in container

![open folder] (https://media.discordapp.net/attachments/701301203849576501/990568586412183562/unknown.png)

- Select the `server` folder

![server folder](https://media.discordapp.net/attachments/701301203849576501/990568648055873556/unknown.png)

- Again, wait until the installation process completes, install the recommended extensions, and exit the container.
- If you now navigate to the remote explorer tab, you should see 3 containers; one for frontend, backend, and database.
- The installation process is now complete.

### Development

- To start developing, navigate to the remote extensions tab. Hover over the frontend or backend container and click the folder icon.
![open folder](https://media.discordapp.net/attachments/701301203849576501/990574912181784656/unknown.png)
- Note, for the backend, you may need to start the database container first. To do so, right click on the database container and click `Start Container`.

![start db](https://media.discordapp.net/attachments/701301203849576501/990571489587789864/unknown.png)

## Writing documentations

We will be using MkDocs to generate the documentations for this project. MkDocs is a documentation generator that is based on Markdown.

### Using MkDocs

Quickstart guide in progress

## Development workflow

1. Decide as a team the issue/s you want to work on.
2. Assign yourselves to the relevant issue on GitHub.
3. A branch corresponding to the issue should be created (unless it is a point 5 issue).
4. checkout the branch corresponding to the issue. It should be in the format of `i<issue number>-<issue_name>`
5. Work on your changes.
6. Make commits and push them to the issue branch.
7. Open a pull request on GitHub.
8. Await for code reviews.
9. Your feature is merged!
10. Delete your local branch with `git branch -d <branch_name>`.
