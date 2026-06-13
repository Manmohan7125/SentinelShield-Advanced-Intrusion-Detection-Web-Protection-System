from database.db import db

from database.models import SecurityLog



def log_event(

        ip,

        attack,

        payload,

        action

):

    log = SecurityLog(

        ip_address=ip,

        attack_type=attack,

        payload=payload,

        action=action

    )


    db.session.add(log)

    db.session.commit()


    print(

        f"[{action}] "

        f"{attack} "

        f"from "

        f"{ip}"

    )