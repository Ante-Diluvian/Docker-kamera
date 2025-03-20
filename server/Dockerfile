FROM python:3.9

WORKDIR /app
COPY server.py /app/

RUN pip install flask opencv-python-headless requests

CMD ["python", "server.py"]
