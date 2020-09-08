FROM python:3.8.5-slim
RUN apt-get update && \
    apt-get -y install gcc \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY /app /app
COPY ./requirements.txt /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["uwsgi", "--ini", "/app/wsgi.ini"]