FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip install -r requirements.txt
RUN curl -sL https://deb.nodesource.com/setup_$v.x | bash - &
RUN apt-get update && apt-get install -y nodejs-legacy && apt-get -y install npm