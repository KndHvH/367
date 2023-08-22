FROM ubuntu:latest

RUN apt-get update -y && apt install python3 -y && apt install python3-pip -y

WORKDIR /usr/app

COPY ./app .

CMD ["python3","main.py"]
