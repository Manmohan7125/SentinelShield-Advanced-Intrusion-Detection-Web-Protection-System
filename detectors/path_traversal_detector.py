import re

patterns = [

    r"\.\./",

    r"\.\.\\",

    r"/etc/passwd",

    r"boot.ini"

]


def detect_path_traversal(data):

    for p in patterns:

        if re.search(p, data):

            return True

    return False