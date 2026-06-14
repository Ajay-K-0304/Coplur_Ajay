FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    openjdk-21-jdk \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirement.txt .
COPY partition.py .

RUN pip install --no-cache-dir -r requirement.txt
CMD ["python","partition.py"]