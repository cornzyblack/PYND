FROM python:3.8-slim-buster

ENV ENVIRONMENT="development"

COPY ./requirements.txt /src/requirements.txt

WORKDIR /src

RUN apt-get update -y
RUN apt-get -y install build-essential libpoppler-cpp-dev pkg-config python3-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY ./src  /src

ENTRYPOINT ["python"]
CMD ["/src/app.py"]
