from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    alert_type = data.get("alert_type", "")

    if alert_type == "cpu_spike":
        severity = "HIGH"
    elif alert_type == "memory_leak":
        severity = "MEDIUM"
    else:
        severity = "LOW"

    return jsonify({"severity": severity})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
