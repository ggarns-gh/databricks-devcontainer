FROM ubuntu:22.04

USER root

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
        ca-certificates \
        curl \
        git \
        gnupg

# Install Zulu Java 8 JRE from Azul
RUN curl -s https://repos.azul.com/azul-repo.key | gpg --dearmor -o /usr/share/keyrings/azul.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/azul.gpg] https://repos.azul.com/zulu/deb stable main" | tee /etc/apt/sources.list.d/zulu.list
RUN apt-get update && apt-get install --no-install-recommends -y zulu8-ca-jre

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