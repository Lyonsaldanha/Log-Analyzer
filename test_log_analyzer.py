import pytest
from log_analyzer import parse_log_line, count_levels, most_common_error


def test_parse_log_line():
    line = "2025-08-24 10:15:22 [INFO] Server started"
    parsed = parse_log_line(line)
    assert parsed == ("2025-08-24 10:15:22", "INFO", "Server started")


def test_count_levels():
    logs = [
        "2025-08-24 10:15:22 [INFO] Server started",
        "2025-08-24 10:16:02 [ERROR] Connection lost",
    ]
    assert count_levels(logs) == {"INFO": 1, "WARNING": 0, "ERROR": 1}


def test_most_common_error():
    logs = [
        "2025-08-24 10:16:02 [ERROR] Connection lost",
        "2025-08-24 10:16:05 [ERROR] Connection lost",
    ]
    assert most_common_error(logs) == "Connection lost"
