FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_DEBUG=1

COPY . .

ENTRYPOINT ["python3"]
CMD ["app.py"]