from flask import Blueprint
from flask import render_template

from database.models import SecurityLog


dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    template_folder="templates"
)


@dashboard_bp.route("/dashboard")
def dashboard():

    total = SecurityLog.query.count()

    blocked = SecurityLog.query.filter_by(
        action="BLOCKED"
    ).count()

    allowed = SecurityLog.query.filter_by(
        action="ALLOWED"
    ).count()


    return render_template(

        "dashboard.html",

        total=total,

        blocked=blocked,

        allowed=allowed

    )


@dashboard_bp.route("/logs")
def logs():

    logs = SecurityLog.query.order_by(

        SecurityLog.timestamp.desc()

    ).all()


    return render_template(

        "logs.html",

        logs=logs

    )


@dashboard_bp.route("/alerts")
def alerts():

    alerts = SecurityLog.query.filter_by(

        action="BLOCKED"

    ).order_by(

        SecurityLog.timestamp.desc()

    ).all()


    return render_template(

        "alerts.html",

        alerts=alerts

    )