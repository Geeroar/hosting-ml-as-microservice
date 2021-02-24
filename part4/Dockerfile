FROM ubuntu:20.04

RUN apt-get update && \
        apt-get install -y python3-pip python3-dev build-essential

COPY requirements.txt .
RUN pip3 install -r requirements.txt

ENV FLASK_APP=app.py
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

WORKDIR /app
COPY src /app
