FROM python:3.9

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
EXPOSE 8000

COPY . .

RUN pip install -r requirements.txt
