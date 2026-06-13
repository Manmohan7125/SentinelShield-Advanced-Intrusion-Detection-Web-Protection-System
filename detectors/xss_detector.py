import re

patterns = [

    r"<script.*?>",

    r"</script>",

    r"alert\s*\(",

    r"onerror\s*=",

    r"onload\s*="

]


def detect_xss(data):

    for p in patterns:

        if re.search(p, data):

            return True

    return False