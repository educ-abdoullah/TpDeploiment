from flask import Flask, jsonify

app = Flask(__name__)


def addition(a, b):
    return a + b


@app.route("/")
def home():
    return jsonify({
        "message": "Route APP fonctionnelle"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/addition/<int:a>/<int:b>")
def addition_route(a, b):
    return jsonify({
        "result": addition(a, b)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)