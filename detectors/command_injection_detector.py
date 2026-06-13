import re

patterns = [

    r";",

    r"\|\|",

    r"&&",

    r"\|",

    r"`",

    r"wget",

    r"curl"

]


def detect_command_injection(data):

    for p in patterns:

        if re.search(p, data):

            return True

    return False