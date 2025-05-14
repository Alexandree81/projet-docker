from flask import Flask
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = open("/run/secrets/secret_key").read().strip()

@app.route("/")
def hello():
    return "Hellllllloooo"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)