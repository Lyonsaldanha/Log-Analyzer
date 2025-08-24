import re

LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(?P<level>\w+)\] (?P<message>.+)$"
)


def load_log(filename="app.log"):
    """Read log file line by line."""
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()


def parse_log_line(line):
    """Extract timestamp, level, and message from a line."""
    # Example line: "2025-08-24 10:15:22 [INFO] Server started"
    # TODO: Split into timestamp, level, message
    match = LOG_PATTERN.match(line.strip())
    if not match:
        return "ErrorParsingLog"
    return (
        match.group("timestamp"),
        match.group("level"),
        match.group("message"),
    )


def count_levels(logs):
    """Count how many INFO/WARNING/ERROR lines."""
    # TODO: Return dict {"INFO": x, "WARNING": y, "ERROR": z}
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    for line in logs:
        parsed = parse_log_line(line)

        if parsed == "ErrorParsingLog":
            continue
        level = parsed[1]
        counts[level] = counts.get(level, 0) + 1

    return counts


def filter_by_level(logs, level):
    """Return only logs of a given level (e.g. ERROR)."""
    # TODO: Filter logs by matching level
    filtered = []
    for line in logs:
        parsed = parse_log_line(line)
        if parsed[1] == level:
            filtered.append(parsed)
    return filtered


def most_common_error(logs):
    """Find most repeated ERROR message."""
    # TODO: Use a dict to count error messages
    counts = {}
    for line in logs:
        parsed = parse_log_line(line)
        if parsed == "ErrorParsingLog":
            continue
        timestamp, level, message = parsed
        if level == "ERROR":
            counts[message] = counts.get(message, 0) + 1

    if not counts:
        return None
    most_common = max(counts, key=counts.get)
    return most_common


def main():
    logs = list(load_log("app.log"))

    while True:
        print("\n=== Log File Analyzer ===")
        print("1. Show summary")
        print("2. Show all ERROR logs")
        print("3. Show all WARNING logs")
        print("4. Show most common ERROR")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("Summary:", count_levels(logs))
        elif choice == "2":
            errors = filter_by_level(logs, "ERROR")
            for e in errors:
                print(e)
        elif choice == "3":
            warnings = filter_by_level(logs, "WARNING")
            for w in warnings:
                print(w)
        elif choice == "4":
            common = most_common_error(logs)
            if common:
                print("Most common error:", common)
            else:
                print("No errors found.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
