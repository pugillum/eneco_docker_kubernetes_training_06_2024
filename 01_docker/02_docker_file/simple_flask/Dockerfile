FROM python:3.12-alpine

RUN mkdir code
RUN pip3 install Flask

COPY app.py /code/

ENTRYPOINT ["python3"]
CMD ["./code/app.py"]
