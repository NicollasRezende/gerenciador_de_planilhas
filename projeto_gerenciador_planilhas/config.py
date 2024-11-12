import os

# Configurações do Google Sheets
GOOGLE_SHEETS_CREDENTIALS_FILE = os.path.join('projeto_gerenciador_planilhas', 'credenciais', 'gerenciador-planilhas-441520-14508a0d8819.json') # Caminho para o arquivo de credenciais JSON
SHEET_ID = "1xZE1h-sF9u-uXxeZEsoyix4-42xRb1YRnoi82K9BU8c"
GOOGLE_SHEETS_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}"# Substitua {sheet_id} pelo ID da sua planilha

# Configurações de autenticação e controle de usuários
ADMIN_USERS = ["nicollaspereira025@gmail.com"]  # Lista de e-mails de administradores
DEFAULT_USER_ROLE = "user"  # Role padrão para novos usuários

# Controle de permissões
PERMISSIONS = {
    "admin": {
        "view_inventory": True,
        "edit_inventory": True,
        "view_logs": True,
        "export_data": True, 
    },
    "user": {
        "view_inventory": True,
        "edit_inventory": True,
        "view_logs": False,
        "export_data": False,
    }
}

# Configurações de Log
LOG_FILE_PATH = os.path.join('data', 'action_logs.csv')  # Localização do arquivo de logs
LOG_FORMAT = "%(asctime)s - %(user)s - %(action)s - %(details)s"  # Formato dos logs

# Configurações de exportação
EXPORT_DIRECTORY = os.path.join('data', 'exports')  # Diretório para salvar arquivos exportados

# Configurações do Dashboard
DASHBOARD_REFRESH_INTERVAL = 60  # Intervalo de atualização do dashboard em segundos

# Configurações de UI
WINDOW_TITLE = "Gerenciador de Planilhas - Controle de Inventário"

TIMEZONE = "America/Sao_Paulo"  # Fuso horário para exibição de datas e horas