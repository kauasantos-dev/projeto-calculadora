from customtkinter import CTkButton, CTk
from display_resultado import DisplayResultadoOperacoes

class OperadoresCalculadora:
    def __init__(self, aplicacao: CTk, display_resultados: DisplayResultadoOperacoes):
        self.aplicacao = aplicacao
        self.display_resultados = display_resultados

    def operadores_aritmeticos(self):
        self.divisao = CTkButton(
            master=self.aplicacao, 
            text="÷", 
            font=("Arial", 25),
            fg_color="orange",
            command=lambda: self.display_resultados.inserir("÷")
        )

        self.divisao.place(
            x=100,
            y=100,
            relwidth=0.14,
            relheight=0.09
        )

        self.multiplicacao = CTkButton(
            master=self.aplicacao, 
            text="×", 
            font=("Arial", 25), 
            fg_color="orange", 
            command=lambda: self.display_resultados.inserir("×")
        )

        self.multiplicacao.place(
            x=100,
            y=100,
            relwidth=0.14,
            relheight=0.09
        )

        self.subtracao = CTkButton(
            master=self.aplicacao, 
            text="-", 
            font=("Arial", 25),
            fg_color="orange", 
            command=lambda: self.display_resultados.inserir("-")
        )

        self.subtracao.place(
            x=100,
            y=100,
            relwidth=0.14,
            relheight=0.09
        )

        self.soma = CTkButton(
            master=self.aplicacao, 
            text="+", 
            font=("Arial", 25),
            fg_color="orange", 
            command=lambda: self.display_resultados.inserir("+")
        )

        self.soma.place(
            x=100,
            y=100,
            relwidth=0.14,
            relheight=0.09
        )

        self.raiz_quadrada = CTkButton(
            master=self.aplicacao, 
            text="√ⁿ", 
            font=("Arial", 18),
            fg_color="orange",
            command=lambda: self.display_resultados.inserir("√ⁿ")
        )

        self.raiz_quadrada.place(
            x=100,
            y=100,
            relwidth=0.14,
            relheight=0.09
        )

        self.potencia = CTkButton(
            master=self.aplicacao, 
            text="xⁿ", 
            font=("Arial", 18),
            fg_color="orange", 
            command=lambda: self.display_resultados.inserir("xⁿ")
        )

        self.potencia.place(
            x=100,
            y=100,
            relwidth=0.14,
            relheight=0.09
        )