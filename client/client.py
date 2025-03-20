from flask import Flask, request, render_template
import base64

app = Flask(__name__)
image_data = None

@app.route('/')
def home():
    global image_data
    return render_template('index.html', image_data=image_data)

@app.route('/upload', methods=['POST'])
def upload():
    global image_data
    data = request.get_json()
    image_data = data.get("image", "")
    return {"status": "OK"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
