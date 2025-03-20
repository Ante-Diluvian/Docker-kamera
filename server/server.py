import cv2
import time
import base64
import threading
import requests
from flask import Flask, jsonify

app = Flask(__name__)

CLIENT_URL = "http://client:5001/upload"  # URL klienta za prejemanje slik

def capture_and_send():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Napaka pri zajemu slike")
            continue

        _, buffer = cv2.imencode('.jpg', frame)
        image_base64 = base64.b64encode(buffer).decode('utf-8')

        try:
            # Pošlji sliko vsakih 10 sekund
            response = requests.post(CLIENT_URL, json={"image": image_base64})
            if response.status_code == 200:
                print(f"Slika poslana, odgovor: {response.status_code}")
            else:
                print(f"Napaka pri pošiljanju slike: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Napaka pri pošiljanju slike: {e}")

        time.sleep(10)

@app.route('/')
def home():
    return jsonify({"message": "Strežnik deluje!"})

if __name__ == "__main__":
    threading.Thread(target=capture_and_send, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
