Sentinel Shield Enterprise

Web Security Monitoring and Intrusion Detection System

---

1. Project Overview

Sentinel Shield Enterprise is a Python and Flask based Web Security Monitoring and Intrusion Detection System (IDS). The system monitors incoming HTTP requests, detects suspicious activities, logs security events, and displays alerts through a web dashboard.

The project is designed to demonstrate how modern web applications can monitor and detect common web attacks in real time.

---

2. Objective

The main objectives of this project are:

- Monitor incoming HTTP requests.
- Detect malicious payloads and suspicious requests.
- Identify common web attacks.
- Log all security events into a database.
- Display alerts and logs through a web dashboard.
- Provide real-time security monitoring.

---

3. Features

Real Time Request Monitoring

Every incoming request is inspected before processing.

SQL Injection Detection

Detects SQL Injection attack patterns such as:

- OR 1=1
- UNION SELECT
- DROP TABLE
- INSERT INTO
- DELETE FROM

Cross Site Scripting (XSS) Detection

Detects malicious JavaScript payloads such as:

- "<script>"
- "alert()"
- "onload="
- "onerror="

Path Traversal Detection

Detects unauthorized file access attempts such as:

- ../
- ..\
- /etc/passwd
- boot.ini

Command Injection Detection

Detects suspicious shell commands and operators:

- ;
- &&
- ||
- |
- wget
- curl

Security Logs

Stores:

- IP Address
- Attack Type
- Payload
- Timestamp
- Action Taken

Alerts Dashboard

Displays:

- Total Requests
- Allowed Requests
- Blocked Requests
- Attack History
- Recent Alerts

---

4. Technology Stack

Technology| Purpose
Python| Backend Programming
Flask| Web Framework
SQLite| Database
SQLAlchemy| ORM
HTML| User Interface
Regex| Attack Pattern Matching

---

5. Project Structure

Sentinel Shield Enterprise

app.py
config.py

database/
    db.py
    models.py

detectors/
    sqli_detector.py
    xss_detector.py
    path_traversal_detector.py
    command_injection_detector.py

middleware/
    request_inspector.py
    rate_limiter.py

logging_system/
    logger.py
    alert_manager.py

dashboard/
    routes.py

    templates/

        dashboard.html

        logs.html

        alerts.html

data/

    security.db

README.md

requirements.txt

---

6. Installation

Install all dependencies:

pip install -r requirements.txt

---

7. Run Project

Start the application:

python app.py

Application runs on:

http://127.0.0.1:5000

---

8. Dashboard URLs

Home

http://127.0.0.1:5000

Dashboard

http://127.0.0.1:5000/dashboard

Security Logs

http://127.0.0.1:5000/logs

Alerts

http://127.0.0.1:5000/alerts

---

9. Test Cases

XSS Attack Test

http://127.0.0.1:5000/?q=<script>alert(1)</script>

Expected Result:

- Attack detected
- Logged in database
- Displayed in Alerts page

---

Path Traversal Test

http://127.0.0.1:5000/?file=../../etc/passwd

Expected Result:

- Path Traversal detected
- Alert generated
- Stored in Logs page

---

10. Future Enhancements

Future versions of the project may include:

- Machine Learning based threat detection
- IP Reputation Checking
- Geo-location Tracking
- Email Alerts
- JWT Authentication
- Role Based Access Control
- Docker Deployment
- Cloud Deployment
- Real Time Charts
- Bootstrap Dashboard UI

---

11. Conclusion

Sentinel Shield Enterprise is a Web Security Monitoring and Intrusion Detection System that monitors incoming requests and detects suspicious activities. The system identifies common web attacks such as SQL Injection, Cross Site Scripting (XSS), Path Traversal, and Command Injection.

The project demonstrates how security monitoring, attack detection, logging, and alerting can be integrated into a web application to improve overall security and provide real-time visibility of malicious activities.