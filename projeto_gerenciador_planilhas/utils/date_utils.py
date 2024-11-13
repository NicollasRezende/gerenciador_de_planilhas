import datetime
from dateutil import parser, tz

# Definindo a timezone configurada
TIMEZONE = tz.gettz("America/Sao_Paulo")

def format_date(date, format="%d/%m/%Y"):
    return date.strftime(format)

def parse_date(date_string, format="%d/%m/%Y"):
    return datetime.datetime.strptime(date_string, format).replace(tzinfo=TIMEZONE)

def is_valid_date(date_string, format="%d/%m/%Y"):
    try:
        datetime.datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False

def get_current_timestamp():
    return datetime.datetime.now(TIMEZONE)

def parse_iso_date(date_string):
    return parser.isoparse(date_string).replace(tzinfo=TIMEZONE)