FROM --platform=linux/amd64 python:3.13.0

# SET WORKING DIRECTORY
WORKDIR /app_code

# Install Dependencies
RUN apt-get update && apt-get install -y --no-install-recommends boxes g++ libssl-dev gcc xmlsec1 gnupg curl software-properties-common

# Update pip and install poetry
RUN pip install --upgrade pip && pip install poetry

# Copy application code into a directory called 'app_code'
# This copy includes pyproject.toml and poetry.lock
COPY ./server /app_code

# Installing requirements using poetry
# `poetry config virtualenvs.create false` -> Use system python and not virtualenvs
# `poetry install --no-dev` -> Install from lock file with no dev dependencies
# `pip install poetry` -> reinstall poetry again because --no-dev param is removing poetry dependencies. If we don't reinstall, poetry will be broken.
# `apt-get autoremove --yes gcc g++` Remove gcc and g++ because it's no longer needed after poetry install
RUN poetry config virtualenvs.create false && poetry install --no-dev && pip install poetry && apt-get autoremove --yes gcc g++

# Copy runtime script & make it executable
COPY /docker/server/runtime.sh /runtime.sh
RUN chmod +x /runtime.sh

# ========================================
# ---- Executed at Container Runtime ----
# ========================================

# CMD commands get executed at container runtime!
CMD ["/runtime.sh"]