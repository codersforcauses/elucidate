FROM --platform=linux/amd64 python:3.10.5

# SET WORKING DIRECTORY
WORKDIR /app_code

# Update pip
RUN pip install --upgrade pip

# Copy application code into a directory called 'app_code'
# This copy includes pyproject.toml and poetry.lock
COPY ./documentation /app_code

# Installing requirements
RUN pip install -r /app_code/requirements.txt