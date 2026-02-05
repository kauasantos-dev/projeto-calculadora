import re
from .uteis import realizar_operacao

def validar_operacao(valor, operacao_atual):
    if valor is None:
        return "0"
    
    elif operacao_atual == "0":
        return valor
    
    elif valor == "=":
        estrutura_operacao = r'^[-+]?[0-9]+(\.[0-9]+)?([\-+×÷\^\√][0-9]+(\.[0-9]+)?)+$'
        if re.fullmatch(estrutura_operacao, operacao_atual):
            return str(realizar_operacao(operacao_atual))
        return "0"
    
    else:
        return None