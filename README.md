# Log Analyzer

A simple Python tool to parse and analyze log files.  
Supports counting log levels, filtering by severity, and finding the most common error message.

## Features
- Parse log lines into `timestamp`, `level`, and `message`
- Count log levels (`INFO`, `WARNING`, `ERROR`)
- Filter logs by severity
- Identify the most common error message
- Interactive CLI menu

## Example Log Format
2025-08-24 10:15:22 [INFO] Server started
2025-08-24 10:16:02 [ERROR] Connection lost
2025-08-24 10:16:05 [WARNING] Low memory


## Usage
Clone the repository and run:

```bash
python log_analyzer.py
```

## Project Structure
log-analyzer/
│── log_analyzer.py    # Main script
│── app.log            # Sample log file
│── test_log_analyzer.py # Unit tests



Running Tests
```bash
pytest - v
```


## Requirements

Python 3.8+
No external dependencies are required.



# Note: You can change the regex in `analyzer.py` to suit your log format.

