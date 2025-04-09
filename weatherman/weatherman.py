import socket
import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def return_condition():
    try:
        return f"""
        Wind: {requests.get("http://wind:5005/")}
        Temp: {requests.get("http://temp:5005/")}
        Humidity: {requests.get("http://humidity:5005/")}
        """
    except requests.exceptions.RequestException as e:
        return f"error: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
