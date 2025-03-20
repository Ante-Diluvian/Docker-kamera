FROM python:3.9

WORKDIR /app
COPY server.py /app/

# OpenCV odvisnosti
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

RUN pip install flask opencv-python-headless requests

CMD ["python", "server.py"]
