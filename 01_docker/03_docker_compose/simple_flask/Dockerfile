FROM python:3.12-alpine

WORKDIR /app

RUN pip3 install Flask

COPY app.py .

ENTRYPOINT ["python3"]
CMD ["app.py"]
