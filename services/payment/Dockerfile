FROM python:3.7-alpine

RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

RUN pip install splunk-opentelemetry==0.5.0
RUN splk-py-trace-bootstrap
ENV SPLK_SERVICE_NAME=srv-payment

COPY . /app

CMD python main.py
# CMD splk-py-trace python main.py
