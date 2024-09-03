# syntax = docker/dockerfile:1.2.1

FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update

# Set work directory
WORKDIR /code 
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache \    
    pip install -r requirements.txt 

EXPOSE 8080
COPY . /code/

# CMD ["gunicorn", "--bind", ":8080", "--workers", "3", "config.wsgi"]
