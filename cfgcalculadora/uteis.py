from . import operacoes, validadores, gerenciar_arquivos

def ver_historico():
    historico = gerenciar_arquivos.arquivo_r()
    if not historico:
        print("O HISTÓRICO DE OPERAÇÕES ESTÁ VAZIO.\n")
    else:
        print("\nHISTÓRICO DE OPERAÇÕES:\n")
        for produto in historico:
            for chave, valor in produto.items():
                print(f"{chave} = {valor}\n")

def apagar_historico():
    gerenciar_arquivos.arquivo_w([])
    print("HISTÓRICO APAGADO COM SUCESSO!\n")

def salvar_historico(nova_operacao_efetuada):
    historico_salvo = gerenciar_arquivos.arquivo_r()
    if not historico_salvo:
        historico_salvo = [nova_operacao_efetuada]
    else:
        historico_salvo.append(nova_operacao_efetuada)
    gerenciar_arquivos.arquivo_w(historico_salvo)

def historico_nova_operacao(lista_numeros, operacao, resultado):
    for valor in range(len(lista_numeros)):
        lista_numeros[valor] = str(lista_numeros[valor])

    operacao_realizada = f" {operacao} ".join(lista_numeros)

    return {operacao_realizada: resultado}

def menu_opcoes():
    print("\n[1]- Soma\n[2]- Subtração\n[3]- Divisão\n[4]- Multiplicação\n[5]- Ver histórico de operações\n[6]- Apagar histórico\n[7]- Sair\n")

def solicitar_numeros(simbolo_da_operacao):
    lista_numeros = []
    if simbolo_da_operacao == '/':
        dividendo, divisor = validadores.validar_numero(input("Informe o primeiro número: ")), validadores.validar_numero(input("Informe o segundo número: "))
        validadores.validar_divisor(divisor)
        lista_numeros.append(dividendo)
        lista_numeros.append(divisor)
        return lista_numeros
    
    while True:
        numero = input("Informe dois números ou mais (digite uma letra para finalizar): ")
        if numero.isalpha():
            break
        numero = validadores.validar_numero(numero)
        lista_numeros.append(numero)
    
    if len(lista_numeros) < 2:
        raise ValueError("Quantidade de números insuficiente para realizar a operação.\n")
    
    return lista_numeros

def realizar_operacao(operacao_selecionada, simbolo_da_operacao):
    try:
        lista_numeros = solicitar_numeros(simbolo_da_operacao)
    except (ValueError, ZeroDivisionError) as erro:
        print(f"\nERRO: {erro}")
        return False
    resultado = operacao_selecionada(lista_numeros)
    exibir_resultado_operacao(historico_nova_operacao(lista_numeros, simbolo_da_operacao, round(resultado, 2)))
    salvar_historico(historico_nova_operacao(lista_numeros, simbolo_da_operacao, round(resultado, 2)))

def exibir_resultado_operacao(operacao_realizada):
    operacao = list(operacao_realizada.keys())
    resultado = list(operacao_realizada.values())
    print(f"\n{operacao[0]} = {resultado[0]}")

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
    
    return resultado_operacao