import csv
from datetime import datetime
from config import LOG_FILE_PATH, LOG_FORMAT, TIMEZONE
from utils.date_utils import get_current_timestamp

def log_action(user, action, details):
    """Registra uma ação no arquivo de log."""
    timestamp = get_current_timestamp().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = LOG_FORMAT % {"asctime": timestamp, "user": user, "action": action, "details": details}
    
    with open(LOG_FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, user, action, details])