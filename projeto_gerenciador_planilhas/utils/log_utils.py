import csv
from datetime import datetime
import os
from config import LOG_FILE_PATH, LOG_FORMAT

def log_action(user, action, details):
    """Registra uma ação no arquivo de log."""
    with open(LOG_FILE_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            "timestamp": timestamp,
            "user": user,
            "action": action,
            "details": details
        }
        writer.writerow([log_entry[key] for key in ["timestamp", "user", "action", "details"]])

def read_logs():
    """Lê os logs do arquivo de log."""
    logs = []
    with open(LOG_FILE_PATH, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            logs.append(row)
    return logs
