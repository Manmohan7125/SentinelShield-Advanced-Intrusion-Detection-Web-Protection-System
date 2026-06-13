from database.db import db
from datetime import datetime


class SecurityLog(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    ip_address = db.Column(
        db.String(50),
        nullable=False
    )

    attack_type = db.Column(
        db.String(100),
        nullable=False
    )

    payload = db.Column(
        db.Text
    )

    action = db.Column(
        db.String(50),
        default="ALLOWED"
    )

    def _repr_(self):

        return f"<{self.ip_address} {self.attack_type}>"