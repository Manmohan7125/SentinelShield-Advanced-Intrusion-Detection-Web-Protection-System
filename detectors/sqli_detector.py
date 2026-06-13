import re

patterns = [
    r"(\bor\b|\band\b)\s+\d+\s*=\s*\d+",
    r"union\s+select",
    r"drop\s+table",
    r"insert\s+into",
    r"delete\s+from",
    r"--",
    r";"
]


def detect_sqli(data):

    for p in patterns:

        if re.search(p, data):

            return True

    return False