import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_SHEETS_CREDENTIALS_FILE

def open_sheet(sheet_id):
    """Abre a planilha do Google Sheets."""
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEETS_CREDENTIALS_FILE, scope)
    client = gspread.authorize(credentials)
    return client.open_by_key(sheet_id)

def read_data(sheet, range):
    """Lê os dados da planilha no intervalo especificado."""
    worksheet = sheet.get_worksheet(0)  # Assume que estamos lendo da primeira aba
    return worksheet.get(range)