from flask import Flask, render_template
from database.db import db
from dashboard.routes import dashboard_bp
from middleware.request_inspector import inspect_request

app = Flask(__name__)

# Configuration
app.config.from_object("config.Config")

# Database initialize
db.init_app(app)

# Dashboard blueprint
app.register_blueprint(dashboard_bp)

# Create database tables
with app.app_context():
    db.create_all()

# Inspect every request
@app.before_request
def before():
    inspect_request()

# Home Page
@app.route("/")
def home():
    return """
    <h1>Sentinel Shield Enterprise</h1>
    <h3>Web Security Monitoring System Active</h3>

    <ul>
      <li><a href='/dashboard'>Dashboard</a></li>
      <li><a href='/logs'>Security Logs</a></li>
      <li><a href='/alerts'>Alerts</a></li>
    </ul>
    """

if __name__ == "__main__":
    app.run(debug=True)