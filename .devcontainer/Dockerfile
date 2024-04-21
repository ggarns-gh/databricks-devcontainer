FROM ubuntu:22.04

USER root

# Install Python 3.10
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
        python3.10 \
        python3-pip \
        python3-venv
ENV PYTHONUNBUFFERED=1

# Create Python venv
RUN python3 -m venv --clear /opt/venv

# Install requirements.txt into venv
COPY requirements.txt .
RUN ["/bin/bash", "-c", "source /opt/venv/bin/activate && python3 -m pip install --upgrade pip && pip install -r requirements.txt"]

# Tidy
RUN rm requirements.txt
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get clean