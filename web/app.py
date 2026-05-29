from flask import Flask, render_template, request
import requests
import qrcode
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/iplookup", methods=["POST"])
def iplookup():

    target = request.form["target"]

    try:

        response = requests.get(
            f"http://ip-api.com/json/{target}",
            timeout=5
        )

        data = response.json()

        return render_template(
            "index.html",
            result=data
        )

    except Exception as e:

        return render_template(
            "index.html",
            error=str(e)
        )


@app.route("/qr", methods=["POST"])
def qr():

    text = request.form["text"]

    img = qrcode.make(text)

    path = "web/static/nexus_qr.png"

    img.save(path)

    return render_template(
        "index.html",
        qr_image="static/nexus_qr.png"
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
