FROM python:3.7-alpine

RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

# RUN pip install splunk-opentelemetry==0.5.0
# RUN splk-py-trace-bootstrap
# ENV SPLK_SERVICE_NAME=srv-search

COPY . /app

CMD	flask run --host 0.0.0.0 --port 8001
# CMD	splk-py-trace flask run --host 0.0.0.0 --port 8001


