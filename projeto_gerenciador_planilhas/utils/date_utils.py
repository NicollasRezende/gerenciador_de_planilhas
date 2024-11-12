import datetime
from dateutil import parser, tz
from projeto_gerenciador_planilhas.config import TIMEZONE

# Definindo a timezone configurada
TIMEZONE = tz.gettz(TIMEZONE)

def format_date(date, format="%d/%m/%Y"):
    """
    Formata um objeto datetime para uma string no formato especificado.
    
    :param date: Objeto datetime a ser formatado.
    :param format: Formato desejado para a string de saída.
    :return: String representando a data formatada.
    """
    return date.strftime(format)

def parse_date(date_string, format="%d/%m/%Y"):
    """
    Converte uma string de data para um objeto datetime.
    
    :param date_string: String representando a data.
    :param format: Formato da string de entrada.
    :return: Objeto datetime.
    """
    return datetime.datetime.strptime(date_string, format).replace(tzinfo=TIMEZONE)

def is_valid_date(date_string, format="%d/%m/%Y"):
    """
    Verifica se uma string de data está no formato válido.
    
    :param date_string: String representando a data.
    :param format: Formato esperado da string de data.
    :return: Booleano indicando se a data é válida.
    """
    try:
        datetime.datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False

def get_current_datetime():
    """
    Retorna a data e hora atual na timezone configurada.
    
    :return: Objeto datetime representando a data e hora atual.
    """
    return datetime.datetime.now(TIMEZONE)

def parse_iso_date(date_string):
    """
    Converte uma string de data no formato ISO 8601 para um objeto datetime.
    
    :param date_string: String representando a data no formato ISO 8601.
    :return: Objeto datetime.
    """
    return parser.isoparse(date_string).replace(tzinfo=TIMEZONE)