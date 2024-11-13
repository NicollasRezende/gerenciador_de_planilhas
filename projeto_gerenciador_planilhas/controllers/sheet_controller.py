import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_SHEETS_CREDENTIALS_FILE, GOOGLE_SHEETS_URL

def connect_to_sheet():
    """Conecta ao Google Sheets usando as credenciais de serviço."""
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEETS_CREDENTIALS_FILE, scope)
    client = gspread.authorize(credentials)
    return client

def get_sheet(sheet_id):
    """Obtém a planilha especificada pelo ID."""
    client = connect_to_sheet()
    return client.open_by_key(sheet_id)
