import socket
import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def forecast():
    try:
        wind = requests.get("http://nginx/wind/").text
        temp = requests.get("http://nginx/temp/").text
        humidity = requests.get("http://nginx/humidity/").text

        return f"{wind}<br>{temp}<br>{humidity}"
    except requests.exceptions.RequestException as e:
        return f"uh oh error: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
