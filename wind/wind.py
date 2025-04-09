import socket
import random
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def return_condition():
    num = random.randint(5, 120)
    return f"wind = {num}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
