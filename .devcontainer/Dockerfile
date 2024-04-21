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

# Install Spark 3.5.0
RUN curl -O https://archive.apache.org/dist/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
# TODO: Verify downloaded file https://www.apache.org/info/verification.html
RUN tar xvf spark-3.5.0-bin-hadoop3.tgz
RUN mv spark-3.5.0-bin-hadoop3 /opt/spark
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Install Python 3.10
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
        python3.10 \
        python3-pip \
        python3-venv
ENV PYTHONUNBUFFERED=1

# Add pyspark/py4j to PYTHONPATH so they are importable
ENV PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
ENV PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.9.7-src.zip:$PYTHONPATH

# Create Python venv
RUN python3 -m venv --clear /opt/venv

# Install requirements.txt into venv
COPY requirements.txt .
RUN ["/bin/bash", "-c", "source /opt/venv/bin/activate && python3 -m pip install --upgrade pip && pip install -r requirements.txt"]

# Tidy
RUN rm spark-3.5.0-bin-hadoop3.tgz requirements.txt
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get clean