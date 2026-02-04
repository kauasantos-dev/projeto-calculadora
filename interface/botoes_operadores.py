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
            relx=0.6,
            rely=0.6,
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
            relx=0.6,
            rely=0.8,
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
            relx=0.6,
            rely=0.7,
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
            relx=0.6,
            rely=0.6,
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
            relx=0.6,
            rely=0.9,
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
            relx=0.6,
            rely=0.95,
            relwidth=0.14,
            relheight=0.09
        )