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