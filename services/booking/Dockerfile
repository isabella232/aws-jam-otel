FROM python:3.7-alpine


RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

RUN pip install splunk-opentelemetry==0.5.0
RUN splk-py-trace-bootstrap
ENV SPLK_SERVICE_NAME=srv-booking

COPY . /app

RUN ./manage.py migrate

CMD splk-py-trace ./manage.py runserver 0.0.0.0:8002
# CMD ./manage.py runserver 0.0.0.0:8002