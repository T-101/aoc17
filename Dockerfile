FROM python:3.5-alpine

VOLUME ["/opt/app"]
WORKDIR /opt/app
COPY requirements.txt .

RUN apk update && \
	apk --no-cache add \
	    sqlite && \
	rm -rf /var/cache/apk/* && \
	pip install --upgrade pip && \
	pip install -r requirements.txt

EXPOSE 8000

COPY . .
