def soma(lista_numeros):
    soma = 0
    for numero in lista_numeros:
        soma += numero
    return soma

def subtracao(lista_numeros):
    resultado = lista_numeros[0]
    for i in range(1, len(lista_numeros)):
        resultado -= lista_numeros[i]
    return resultado

def divisao(lista_numeros):
    return lista_numeros[0] / lista_numeros[1]

def multiplicacao(lista_numeros):
    mult = 1
    for numero in lista_numeros:
        mult *= numero
    return mult

def potenciacao(lista_numeros):
    return lista_numeros[0] ** lista_numeros[1]

def radiciacao(lista_numeros):
    return lista_numeros[1] ** (1 / lista_numeros[0])