from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"message": "HELLO DESDE DOCKER"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


# IMPORTANTE: Este bloque debe ir al inicio de la línea, sin espacios
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
