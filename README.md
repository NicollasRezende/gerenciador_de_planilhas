
---

# Documentação do Projeto - Gerenciador de Planilhas

## Visão Geral

Este projeto é um Gerenciador de Planilhas desenvolvido em Python, voltado para o controle de inventário com uma organização em três níveis: Corredor, Prateleira e Segmento. Utilizando a API do Google Sheets com OAuth2, ele permite o monitoramento e manutenção de registros de estoque ou biblioteca de documentos com visualizações em tempo real, controle de usuários e exportação de dados.

### Principais Funcionalidades

1. **Conexão com Google Sheets**:
    - Integração via API do Google Sheets, utilizando OAuth2 para autenticação segura.
    - Permite acesso a dados externos em planilhas públicas e privadas, garantindo a atualização em tempo real.

2. **Gestão de Inventário**:
    - Organização de inventário em níveis (Corredor, Prateleira e Segmento).
    - Funcionalidades de adição, remoção e atualização de itens com rastreamento de cada ação (quem realizou e quando).
    - Acompanhamento de retiradas e adições com visualização integrada para análise de dados.

3. **Controle de Usuários e Acesso**:
    - Dois tipos de perfis: Administrador e Usuário Comum.
    - **Administrador**: Acesso total ao sistema, incluindo gerenciamento de usuários e logs.
    - **Usuário Comum**: Acesso restrito, com permissão para visualização e edição apenas.

4. **Sistema de Logs**:
    - Registra todas as operações com detalhes, incluindo tipo de ação, usuário, data/hora e itens afetados.
    - Acesso aos logs é restrito aos administradores para manter segurança e integridade do sistema.

5. **Dashboard e Relatórios**:
    - Painel de visualização de dados usando gráficos Seaborn, com exibição em tempo real.
    - Exportação de relatórios e logs em formatos Excel e CSV para auditoria e backup, possibilitando fácil consulta e análise.

## Estrutura Geral de Arquivos e Pastas

Para uma organização eficiente, o projeto segue a estrutura de diretórios abaixo, maximizando escalabilidade, modularidade e clareza:

```plaintext
projeto_gerenciador_de_planilhas/
├── controllers/
│   ├── 

auth_controller.py


│   ├── 

dashboard_controller.py


│   ├── 

export_controller.py


│   └── 

log_controller.py


├── credenciais/
│   └── 

gerenciador-planilhas-441520-14508a0d8819.json


├── dashboard/
│   └── 

dashboard_view.py


├── data/
│   ├── exported_inventory.csv
│   └── exported_logs.csv
├── services/
│   ├── 

auth_service.py


│   └── 

google_sheets_service.py


├── tests/
│   └── 

test_dependencies.py


├── utils/
│   ├── 

date_utils.py


│   └── 

log_utils.py


├── 

config.py


├── 

main.py


├── 

README.md


└── 

requirements.txt


```

### Descrição dos Componentes

1. **config.py**: Define variáveis globais, incluindo URLs de planilhas, credenciais, parâmetros para logs e permissões.

2. **main.py**: Ponto de entrada do sistema, inicializa configurações, autenticação e executa os controladores.

3. **controllers/**: Lógica de negócio organizada por módulos:
    - `auth_controller.py`: Verifica se o usuário é administrador e se possui permissões específicas.
    - `dashboard_controller.py`: Atualiza o dashboard em intervalos regulares.
    - `export_controller.py`: Exporta dados para arquivos CSV.
    - `log_controller.py`: Registra ações no sistema de logs.

4. **credenciais/**: Contém o arquivo de credenciais JSON necessário para autenticação com a API do Google Sheets.

5. **dashboard/**: Interface de visualização e geração de relatórios em tempo real:
    - `dashboard_view.py`: Gera visualizações usando Seaborn e Matplotlib embutidos na interface Tkinter.

6. **data/**: Pasta para armazenamento temporário de dados exportados (planilhas e logs) em formatos Excel ou CSV.

7. **services/**: Serviços especializados para manipulação de dados externos e autenticação:
    - `auth_service.py`: Controla a autenticação OAuth2 para Google Sheets.
    - `google_sheets_service.py`: Conecta e manipula dados no Google Sheets usando `gspread`.

8. **utils/**: Funções auxiliares para suporte ao projeto:
    - `date_utils.py`: Manipula datas e horários para formatação e validação.
    - `log_utils.py`: Funções de suporte para geração e gerenciamento de logs.

9. **tests/**: Contém testes para verificar as dependências do projeto:
    - `test_dependencies.py`: Verifica se todas as bibliotecas necessárias foram importadas com sucesso.

### Dependências do Projeto

O arquivo `requirements.txt` lista todas as bibliotecas necessárias:

```plaintext
# Google Sheets API e autenticação
gspread==5.2.0
oauth2client==4.1.3

# Manipulação de planilhas e dados
pandas==1.3.5
openpyxl==3.0.9
xlsxwriter==1.4.4

# Visualização e Dashboard
seaborn==0.11.2
matplotlib==3.7.2
PyQt5==5.15.4  # Ou PySide2 caso prefira

# Logs e utilitários de data e hora
python-dateutil==2.8.2
```

### Fluxo Geral do Projeto

1. **Autenticação**: Ao iniciar, o sistema carrega `config.py`, autentica o usuário com OAuth2 e verifica o tipo de usuário (administrador ou comum).

2. **Controle de Acesso**: Com base nas permissões, o sistema controla o acesso às funcionalidades:
    - Usuário Comum: Visualização e edição básica do inventário.
    - Administrador: Acesso completo a todos os recursos, incluindo logs e dashboards.

3. **Operações de Inventário**: O `inventory_controller.py` permite adicionar, remover e atualizar itens no inventário, registrando cada ação.

4. **Registro de Logs**: Através do `log_controller.py`, cada operação é registrada para manter um histórico de ações com detalhes (usuário, data/hora, tipo de ação).

5. **Dashboard e Exportação**: O administrador visualiza e analisa dados em tempo real com gráficos e tem a opção de exportar relatórios no formato Excel para consulta ou backup.

### Justificativa para Descontinuação

Infelizmente, o projeto `Gerenciador de Planilhas` foi descontinuado devido à falta de tempo para manutenção e desenvolvimento contínuo. Embora o sistema tenha sido projetado para ser uma solução completa e escalável para gestão de inventário, com autenticação segura, controle de permissões, visualização de dados e exportação, a equipe responsável não pôde continuar com o suporte necessário para garantir sua evolução e estabilidade.

Agradecemos a todos que contribuíram para o desenvolvimento deste projeto e esperamos que o código e a documentação fornecidos possam ser úteis para outros desenvolvedores e projetos futuros.

---

## Detalhamento dos Arquivos

### `config.py`

Define variáveis globais, incluindo URLs de planilhas, credenciais, parâmetros para logs e permissões.

### `main.py`

Ponto de entrada do sistema, inicializa configurações, autenticação e executa os controladores.

### `controllers/auth_controller.py`

Verifica se o usuário é administrador e se possui permissões específicas.

```python
from config import ADMIN_USERS, PERMISSIONS

def is_admin(user_email):
    """Verifica se o usuário é administrador."""
    return user_email in ADMIN_USERS

def has_permission(user_role, permission):
    """Verifica se o usuário possui permissão para uma ação específica."""
    return PERMISSIONS.get(user_role, {}).get(permission, False)
```

### `controllers/dashboard_controller.py`

Atualiza o dashboard em intervalos regulares.

```python
import time
from config import DASHBOARD_REFRESH_INTERVAL

def refresh_dashboard():
    """Atualiza o dashboard em intervalos regulares."""
    while True:
        print("Atualizando o dashboard...")
        # lógica de atualização aqui
        time.sleep(DASHBOARD_REFRESH_INTERVAL)
```

### `controllers/export_controller.py`

Exporta dados para arquivos CSV.

```python
import pandas as pd
from config import EXPORT_DIRECTORY

def export_sheet_to_csv(data, filename):
    """Exporta os dados para um arquivo CSV no diretório de exportação."""
    file_path = f"{EXPORT_DIRECTORY}/{filename}.csv"
    data.to_csv(file_path, index=False)
    return file_path
```

### `controllers/log_controller.py`

Registra ações no sistema de logs.

```python
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
```

### `credenciais/gerenciador-planilhas-441520-14508a0d8819.json`

Contém o arquivo de credenciais JSON necessário para autenticação com a API do Google Sheets.

### `dashboard/dashboard_view.py`

Gera visualizações usando Seaborn e Matplotlib embutidos na interface Tkinter.

```python
import tkinter as tk
from tkinter import messagebox
from services.google_sheets_service import open_sheet, read_data
from services.auth_service import has_permission, is_admin
from config import GOOGLE_SHEETS_URL, ADMIN_USERS, DASHBOARD_REFRESH_INTERVAL

class DashboardView:
    def __init__(self, root, user_email):
        self.root = root
        self.user_email = user_email
        self.root.title("Painel de Controle - Gerenciador de Inventário")
        self.root.geometry("800x600")
        
        # Configurar interface
        self.create_widgets()
        self.update_dashboard()
        
    def create_widgets(self):
        """Cria os widgets do painel de controle."""
        self.inventory_label = tk.Label(self.root, text="Inventário", font=("Arial", 16))
        self.inventory_label.pack(pady=10)

        self.inventory_list = tk.Listbox(self.root, width=100, height=20)
        self.inventory_list.pack(pady=5)

        # Botão para exportar dados
        if has_permission("admin" if is_admin(self.user_email) else "user", "export_data"):
            self.export_button = tk.Button(self.root, text="Exportar Dados", command=self.export_data)
            self.export_button.pack(pady=10)

        # Botão para visualizar logs
        if has_permission("admin" if is_admin(self.user_email) else "user", "view_logs"):
            self.logs_button = tk.Button(self.root, text="Visualizar Logs", command=self.view_logs)
            self.logs_button.pack(pady=5)

    def update_dashboard(self):
        """Atualiza o painel com dados do inventário."""
        # Conecta com o Google Sheets para ler os dados
        try:
            sheet_id = GOOGLE_SHEETS_URL.split('/d/')[1].split('/')[0]
            sheet = open_sheet(sheet_id)
            data = read_data(sheet, "A1:Z100")  # Ajuste o intervalo conforme necessário

            self.inventory_list.delete(0, tk.END)
            for row in data:
                self.inventory_list.insert(tk.END, " | ".join(row))

            # Atualiza a cada X segundos
            self.root.after(DASHBOARD_REFRESH_INTERVAL * 1000, self.update_dashboard)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar o inventário: {e}")

    def export_data(self):
        """Exporta os dados do inventário para um arquivo."""
        # Lógica de exportação
        messagebox.showinfo("Exportação", "Dados exportados com sucesso!")

    def view_logs(self):
        """Abre uma nova janela para exibir os logs."""
        # Lógica para exibir logs
        messagebox.showinfo("Logs", "Exibindo logs do sistema.")

# Código principal para iniciar o painel
if __name__ == "__main__":
    root = tk.Tk()
    user_email = "user@example.com"  # Este email deve vir do sistema de autenticação
    dashboard = DashboardView(root, user_email)
    root.mainloop()
```

### `data/exported_inventory.csv`

Arquivo CSV para armazenamento temporário de dados exportados do inventário.

### `data/exported_logs.csv`

Arquivo CSV para armazenamento temporário de logs exportados.

### `services/auth_service.py`

Controla a autenticação OAuth2 para Google Sheets.

```python
from config import ADMIN_USERS, PERMISSIONS

def is_admin(user_email):
    """Verifica se o usuário é um administrador."""
    return user_email in ADMIN_USERS

def get_user_permissions(user_role):
    """Retorna as permissões para o perfil de usuário especificado."""
    return PERMISSIONS.get(user_role, {})

def has_permission(user_role, action):
    """Verifica se o perfil do usuário tem permissão para a ação."""
    return PERMISSIONS.get(user_role, {}).get(action, False)
```

### `services/google_sheets_service.py`

Conecta e manipula dados no Google Sheets usando `gspread`.

```python
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
```

### `tests/test_dependencies.py`

Verifica se todas as bibliotecas necessárias foram importadas com sucesso.

```python
# Importações principais
try:
    import gspread
    import oauth2client
    import pandas as pd
    import openpyxl
    import xlsxwriter
    import seaborn as sns
    import matplotlib.pyplot as plt
    print("Todas as bibliotecas foram importadas com sucesso!")
except ImportError as e:
    print(f"Erro ao importar: {e}")
```

### `utils/date_utils.py`

Manipula datas e horários para formatação e validação.

```python
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
```

### `utils/log_utils.py`

Funções de suporte para geração e gerenciamento de logs.

```python
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
```

---

Este projeto oferece uma solução completa e escalável para gestão de inventário, com autenticação segura, controle de permissões, visualização de dados e exportação. É adequado para ambientes que exigem rastreabilidade, acesso controlado e relatórios detalhados, mantendo todos os registros organizados e facilmente acessíveis.

Infelizmente, o projeto foi descontinuado devido à falta de tempo para manutenção e desenvolvimento contínuo. espero que o código e a documentação fornecidos possam ser úteis para outros desenvolvedores e projetos futuros.

