from flask import Flask
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default-key")

@app.route("/")
def hello():
    return (
        f"Mode : {os.getenv('FLASK_ENV')} – "
        f"Secret key = {app.config['SECRET_KEY']}"
    )

if __name__ == "__main__":
    port = int(os.getenv("FLASK_PORT", 5000))
    app.run(host="0.0.0.0", port=port)