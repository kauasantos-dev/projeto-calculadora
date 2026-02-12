import re
from .uteis import realizar_operacao, salvar_operacao_no_historico

def validar_operacao(valor, operacao_atual):
    if valor is None:
        return "0"
    
    elif operacao_atual == "0":
        return valor
    
    elif valor == "=":
        estrutura_operacao = r'^[-+]?[0-9]+(\.[0-9]+)?([\-+×÷\^\√][0-9]+(\.[0-9]+)?)+$'
        if re.fullmatch(estrutura_operacao, operacao_atual):
            resultado = str(realizar_operacao(operacao_atual))

            operacao_atual = operacao_atual.replace('^', 'xⁿ')

            salvar_operacao_no_historico(operacao_atual, resultado)
            return resultado
        
        return '0'