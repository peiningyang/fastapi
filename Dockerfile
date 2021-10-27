FROM python:3.7.3-stretch

# Working Directory
WORKDIR /main

# Copy source code to working directory
COPY . main.py /main/

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt
