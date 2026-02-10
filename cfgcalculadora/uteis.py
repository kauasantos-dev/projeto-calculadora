from . import operacoes, gerenciar_arquivos

def ver_historico():
    historico_salvo = gerenciar_arquivos.arquivo_r()
    historico_formatado = ""
    
    if not historico_salvo:
       return "O histórico de operações está vazio."
    for operacao in historico_salvo:
        for operacao_salva, resultado in operacao.items():
            historico_formatado += f"{operacao_salva} = {resultado}\n\n"

    return historico_formatado

def apagar_historico():
    historico_salvo = gerenciar_arquivos.arquivo_r()
    if not historico_salvo:
        return False
    gerenciar_arquivos.arquivo_w([])
    return True

def salvar_operacao_no_historico(operacao_efetuada, resultado):
    nova_operacao = {operacao_efetuada: resultado}

    historico_salvo = gerenciar_arquivos.arquivo_r()
    historico_salvo.append(nova_operacao)
    gerenciar_arquivos.arquivo_w(historico_salvo)

def historico_nova_operacao(lista_numeros, operacao, resultado):
    for valor in range(len(lista_numeros)):
        lista_numeros[valor] = str(lista_numeros[valor])

    operacao_realizada = f" {operacao} ".join(lista_numeros)

    return {operacao_realizada: resultado}

def realizar_operacao(operacao_usuario: str):
    numeros_operadores_separados = []
    primeiro_elemento_operacao = operacao_usuario[0]
        
    valores_da_operacao = ""
    if primeiro_elemento_operacao in "+-":
        valores_da_operacao = primeiro_elemento_operacao
        operacao_usuario = operacao_usuario[1:]

    for elemento in operacao_usuario:
        if elemento.isdigit() or elemento == ".":
            valores_da_operacao += elemento
        else:
            numeros_operadores_separados.append(valores_da_operacao)
            numeros_operadores_separados.append(elemento)
            valores_da_operacao = ""
    numeros_operadores_separados.append(valores_da_operacao)
        
    if len(numeros_operadores_separados) == 3:
        valores = [float(numeros_operadores_separados[0]), float(numeros_operadores_separados[2])]
        operador = numeros_operadores_separados[1]
        resultado_operacao = chamar_operacao(valores, operador)
        return resultado_operacao
        
    resultado_operacao_anterior = None
    for valor in range(1, len(numeros_operadores_separados), 2):
        if resultado_operacao_anterior or resultado_operacao_anterior == 0:
            primeiro_valor = resultado_operacao_anterior
        else:
            primeiro_valor = float(numeros_operadores_separados[valor-1])

        segundo_valor = float(numeros_operadores_separados[valor+1])
        total_numeros = [primeiro_valor, segundo_valor]
        operador_equacao = numeros_operadores_separados[valor]
        resultado_operacao_anterior = chamar_operacao(total_numeros, operador_equacao)

        if valor == len(numeros_operadores_separados) - 2:
            break
    resultado_final_operacao = resultado_operacao_anterior
    return resultado_final_operacao

def chamar_operacao(numeros: list, simbolo_operacao: str):
    if simbolo_operacao == "+":
        resultado_operacao = operacoes.soma(numeros)
    
    elif simbolo_operacao == "-":
        resultado_operacao = operacoes.subtracao(numeros)
    
    elif simbolo_operacao == "×":
        resultado_operacao = operacoes.multiplicacao(numeros)
    
    elif simbolo_operacao == "÷":
        resultado_operacao = operacoes.divisao(numeros)
    
    elif simbolo_operacao == "√":
        resultado_operacao = operacoes.radiciacao(numeros)
    
    elif simbolo_operacao == "^":
        resultado_operacao = operacoes.potenciacao(numeros)
    
    return resultado_operacao