from tkinter import Button, Tk
from .display_resultado import DisplayResultadoOperacoes

class OperadoresCalculadora:
    def __init__(self, aplicacao: Tk, display_resultados: DisplayResultadoOperacoes):
        self.aplicacao = aplicacao
        self.display_resultados = display_resultados

    def operadores_aritmeticos(self):
        self.divisao = Button(
            self.aplicacao, 
            text="÷", 
            font=("Arial", 25),
            background="orange", 
            fg="white",
            bd=1,
            relief="raised",
            command=lambda: self.display_resultados.inserir("÷")
        )

        self.divisao.place(
            relx=0.76,
            rely=0.30,
            relwidth=0.14,
            relheight=0.09
        )

        self.multiplicacao = Button(
            self.aplicacao, 
            text="×", 
            font=("Arial", 25), 
            background="orange", 
            fg="white",
            bd=1,
            relief="raised",
            command=lambda: self.display_resultados.inserir("×")
        )

        self.multiplicacao.place(
            relx=0.61,
            rely=0.30,
            relwidth=0.14,
            relheight=0.09
        )

        self.subtracao = Button(
            self.aplicacao, 
            text="-", 
            font=("Arial", 25),
            background="orange", 
            fg="white",
            bd=1,
            relief="raised",
            command=lambda: self.display_resultados.inserir("-")
        )

        self.subtracao.place(
            relx=0.76,
            rely=0.40,
            relwidth=0.14,
            relheight=0.09
        )

        self.soma = Button(
            self.aplicacao, 
            text="+", 
            font=("Arial", 25),
            background="orange", 
            fg="white",
            bd=1,
            relief="raised",
            command=lambda: self.display_resultados.inserir("+")
        )

        self.soma.place(
            relx=0.61,
            rely=0.40,
            relwidth=0.14,
            relheight=0.09
        )

        self.raiz_quadrada = Button(
            self.aplicacao, 
            text="√ⁿ", 
            font=("Arial", 18),
            background="orange", 
            fg="white",
            bd=1,
            relief="raised",
            command=lambda: self.display_resultados.inserir("√ⁿ")
        )

        self.raiz_quadrada.place(
            relx=0.61,
            rely=0.50,
            relwidth=0.14,
            relheight=0.09
        )

        self.potencia = Button(
            self.aplicacao, 
            text="xⁿ", 
            font=("Arial", 18),
            background="orange", 
            fg="white",
            bd=1,
            relief="raised",
            command=lambda: self.display_resultados.inserir("xⁿ")
        )

        self.potencia.place(
            relx=0.76,
            rely=0.50,
            relwidth=0.14,
            relheight=0.09
        )