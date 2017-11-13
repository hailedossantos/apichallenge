FROM python:latest

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python python-pip

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -U pip
RUN pip install -Ur requirements.txt

EXPOSE 8000
CMD ["/code/run_app.sh"]