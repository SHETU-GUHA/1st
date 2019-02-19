FROM alpine:latest
RUN apk update
RUN apk upgrade
RUN apk add python3 py-pip
COPY . /app
WORKDIR /app
RUN pip install flask
ENTRYPOINT ["python"]
CMD ["app.py"]
