FROM python:3.9

WORKDIR /app
COPY client.py /app/
COPY templates /app/templates
RUN pip install flask

CMD ["python", "client.py"]
