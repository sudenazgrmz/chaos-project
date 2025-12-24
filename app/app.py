from flask import Flask, render_template_string
import requests

app = Flask(__name__)

BACKEND_URL = "http://backend:5001/alerts"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Security Alert Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f5f5f5; }
        table { border-collapse: collapse; width: 80%; margin: 40px auto; background: white; }
        th, td { padding: 12px; border-bottom: 1px solid #ddd; text-align: center; }
        th { background: #333; color: white; }

        .CRITICAL { background-color: #ff4d4d; color: white; }
        .HIGH { background-color: #ff9933; }
        .MEDIUM { background-color: #ffeb3b; }
        .LOW { background-color: #8bc34a; }
        .UNKNOWN { background-color: #bdbdbd; }
    </style>
</head>
<body>
    <h2 style="text-align:center;">Security Alerts Dashboard</h2>
    <table>
        <tr>
            <th>Alert Type</th>
            <th>Severity</th>
            <th>Source</th>
        </tr>
        {% for alert in alerts %}
        <tr class="{{ alert.severity }}">
            <td>{{ alert.alert_type }}</td>
            <td>{{ alert.severity }}</td>
            <td>{{ alert.source }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route("/")
def dashboard():
    try:
        response = requests.get(BACKEND_URL, timeout=2)
        alerts = response.json()
    except Exception:
        alerts = []

    return render_template_string(HTML_TEMPLATE, alerts=alerts)
