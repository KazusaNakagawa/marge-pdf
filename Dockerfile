FROM python:3.9
RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    nginx \
    vim

RUN mkdir /code
WORKDIR /code
WORKDIR /python_doc

ADD ./requirements.txt /code
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
