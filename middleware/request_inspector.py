from flask import request

from detectors.sqli_detector import detect_sqli
from detectors.xss_detector import detect_xss
from detectors.path_traversal_detector import detect_path_traversal
from detectors.command_injection_detector import detect_command_injection

from logging_system.logger import log_event


def inspect_request():

    data = request.query_string.decode().lower()

    ip = request.remote_addr


    if detect_sqli(data):

        log_event(
            ip,
            "SQL Injection",
            data,
            "BLOCKED"
        )


    elif detect_xss(data):

        log_event(
            ip,
            "XSS",
            data,
            "BLOCKED"
        )


    elif detect_path_traversal(data):

        log_event(
            ip,
            "Path Traversal",
            data,
            "BLOCKED"
        )


    elif detect_command_injection(data):

        log_event(
            ip,
            "Command Injection",
            data,
            "BLOCKED"
        )


    else:

        log_event(
            ip,
            "Normal Request",
            data,
            "ALLOWED"
        )