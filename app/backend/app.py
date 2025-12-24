from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

CLASSIFIER_URL = "http://classifier:5002/classify"

alerts = []  # in-memory storage

@app.route("/generate-alert", methods=["POST"])
def generate_alert():
    data = request.get_json()
    alert_type = data.get("alert_type")

    if not alert_type:
        return jsonify({"error": "alert_type is required"}), 400

    # Call classifier service
    try:
        response = requests.post(
            CLASSIFIER_URL,
            json={"alert_type": alert_type},
            timeout=2
        )
        severity = response.json().get("severity", "UNKNOWN")
    except Exception as e:
        severity = "UNKNOWN"

    alert = {
        "alert_type": alert_type,
        "severity": severity,
        "source": "manual-endpoint"
    }

    alerts.append(alert)

    return jsonify(alert)


@app.route("/alerts", methods=["GET"])
def list_alerts():
    return jsonify(alerts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)