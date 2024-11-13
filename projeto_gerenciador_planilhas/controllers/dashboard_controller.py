import time
from config import DASHBOARD_REFRESH_INTERVAL

def refresh_dashboard():
    """Atualiza o dashboard em intervalos regulares."""
    while True:
        print("Atualizando o dashboard...")
        # lógica de atualização aqui
        time.sleep(DASHBOARD_REFRESH_INTERVAL)
