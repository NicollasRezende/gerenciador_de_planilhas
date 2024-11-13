import pandas as pd
from config import EXPORT_DIRECTORY

def export_sheet_to_csv(data, filename):
    """Exporta os dados para um arquivo CSV no diretório de exportação."""
    file_path = f"{EXPORT_DIRECTORY}/{filename}.csv"
    data.to_csv(file_path, index=False)
    return file_path
