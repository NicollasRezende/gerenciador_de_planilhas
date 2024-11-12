Aqui está a documentação atualizada com as bibliotecas que decidimos usar, incluindo detalhes sobre o uso de cada uma no projeto:

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

---

## Estrutura Geral de Arquivos e Pastas

Para uma organização eficiente, o projeto segue a estrutura de diretórios abaixo, maximizando escalabilidade, modularidade e clareza:

```plaintext
projeto_gerenciador_planilhas/
├── config.py                   # Configurações globais do sistema
├── main.py                     # Arquivo principal para execução do programa
├── README.md                   # Documentação do projeto e instruções de uso
├── requirements.txt            # Lista de dependências do projeto
│
├── controllers/                # Controladores do sistema, para a lógica de negócio
│   ├── user_controller.py      # Controlador para manipulação de usuários
│   ├── inventory_controller.py # Controlador para gerenciamento de inventário
│   └── log_controller.py       # Controlador para manipulação e consulta de logs
│
├── services/                   # Serviços para interação com APIs e manipulação de dados
│   ├── google_sheets_service.py # Serviço para conexão com Google Sheets
│   └── auth_service.py         # Serviço de autenticação com OAuth2
│
├── utils/                      # Funções utilitárias de suporte
│   ├── date_utils.py           # Funções para manipulação de datas
│   └── log_utils.py            # Funções para registros e manipulação de logs
│
├── dashboard/                  # Interface e funções do dashboard de visualização
│   └── dashboard_view.py       # Painel de visualização com gráficos Seaborn
│
└── data/                       # Pasta para armazenamento de dados exportados
    ├── exported_logs.xlsx      # Logs exportados
    └── exported_inventory.xlsx # Inventário exportado
```

### Descrição dos Componentes

1. **config.py**: Define variáveis globais, incluindo URLs de planilhas, credenciais, parâmetros para logs e permissões.

2. **main.py**: Ponto de entrada do sistema, inicializa configurações, autenticação e executa os controladores.

3. **controllers/**: Lógica de negócio organizada por módulos:

    - `user_controller.py`: Autenticação e controle de permissões de usuários.
    - `inventory_controller.py`: Gerencia operações de inventário, como adição e retirada de itens.
    - `log_controller.py`: Gerencia o sistema de logs, registrando todas as ações do sistema.

4. **services/**: Serviços especializados para manipulação de dados externos e autenticação:

    - `google_sheets_service.py`: Conecta e manipula dados no Google Sheets usando `gspread`.
    - `auth_service.py`: Controla a autenticação OAuth2 para Google Sheets.

5. **utils/**: Funções auxiliares para suporte ao projeto:

    - `date_utils.py`: Manipula datas e horários para formatação e validação.
    - `log_utils.py`: Funções de suporte para geração e gerenciamento de logs.

6. **dashboard/**: Interface de visualização e geração de relatórios em tempo real.

    - `dashboard_view.py`: Gera visualizações usando Seaborn e Matplotlib embutidos na interface PyQt5.

7. **data/**: Pasta para armazenamento temporário de dados exportados (planilhas e logs) em formatos Excel ou CSV.

---

## Dependências do Projeto

O arquivo `requirements.txt` lista todas as bibliotecas necessárias:

-   `gspread`: Manipulação de dados no Google Sheets.
-   `oauth2client`: Autenticação OAuth2 para integração segura com APIs do Google.
-   `pandas`: Manipulação e formatação de dados para exportação em CSV e Excel.
-   `openpyxl` e `xlsxwriter`: Para manipulação e criação de arquivos Excel.
-   `PyQt5`: Interface gráfica para desktop.
-   `Seaborn` e `Matplotlib`: Visualização de dados no dashboard com gráficos.

Exemplo do conteúdo de `requirements.txt`:

```plaintext
gspread==5.2.0
oauth2client==4.1.3
pandas==1.3.5
openpyxl==3.0.9
xlsxwriter==3.0.2
PyQt5==5.15.4
seaborn==0.11.2
matplotlib==3.4.3
```

---

## Fluxo Geral do Projeto

1. **Autenticação**: Ao iniciar, o sistema carrega `config.py`, autentica o usuário com OAuth2 e verifica o tipo de usuário (administrador ou comum).

2. **Controle de Acesso**: Com base nas permissões, o sistema controla o acesso às funcionalidades:

    - Usuário Comum: Visualização e edição básica do inventário.
    - Administrador: Acesso completo a todos os recursos, incluindo logs e dashboards.

3. **Operações de Inventário**: O `inventory_controller.py` permite adicionar, remover e atualizar itens no inventário, registrando cada ação.

4. **Registro de Logs**: Através do `log_controller.py`, cada operação é registrada para manter um histórico de ações com detalhes (usuário, data/hora, tipo de ação).

5. **Dashboard e Exportação**: O administrador visualiza e analisa dados em tempo real com gráficos e tem a opção de exportar relatórios no formato Excel para consulta ou backup.

---

Este projeto oferece uma solução completa e escalável para gestão de inventário, com autenticação segura, controle de permissões, visualização de dados e exportação. É adequado para ambientes que exigem rastreabilidade, acesso controlado e relatórios detalhados, mantendo todos os registros organizados e facilmente acessíveis.
