from customtkinter import CTkButton, CTk
from .display_resultado import DisplayResultadoOperacoes

class OperadoresCalculadora:
    def __init__(self, aplicacao: CTk, display_resultados: DisplayResultadoOperacoes):
        self.aplicacao = aplicacao
        self.display_resultados = display_resultados

    def operadores_aritmeticos(self):
        self.divisao = CTkButton(
            master=self.aplicacao, 
            text="÷", 
            text_color='white',
            font=("Arial", 25),
            fg_color="orange",
            hover_color='#1C1C1C',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir("÷")
        )

        self.divisao.place(
            relx=0.8,
            rely=0.39,
            relwidth=0.12,
            relheight=0.08
        )

        self.multiplicacao = CTkButton(
            master=self.aplicacao, 
            text="×", 
            text_color='white',
            font=("Arial", 25),
            fg_color="orange",
            hover_color='#1C1C1C',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir("×")
        )

        self.multiplicacao.place(
            relx=0.67,
            rely=0.39,
            relwidth=0.12,
            relheight=0.08
        )

        self.subtracao = CTkButton(
            master=self.aplicacao, 
            text="-", 
            text_color='white',
            font=("Arial", 25),
            fg_color="orange",
            hover_color='#1C1C1C',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir("-")
        )

        self.subtracao.place(
            relx=0.8,
            rely=0.3,
            relwidth=0.12,
            relheight=0.08
        )

        self.soma = CTkButton(
            master=self.aplicacao, 
            text="+", 
            text_color='white',
            font=("Arial", 25),
            fg_color="orange",
            hover_color='#1C1C1C',
            corner_radius=30, 
            command=lambda: self.display_resultados.inserir("+")
        )

        self.soma.place(
            relx=0.67,
            rely=0.3,
            relwidth=0.12,
            relheight=0.08
        )

        self.raiz_quadrada = CTkButton(
            master=self.aplicacao, 
            text="√ⁿ", 
            text_color='white',
            font=("Arial", 25),
            fg_color="orange",
            hover_color='#1C1C1C',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir("√ⁿ")
        )

        self.raiz_quadrada.place(
            relx=0.8,
            rely=0.48,
            relwidth=0.12,
            relheight=0.08
        )

        self.potencia = CTkButton(
            master=self.aplicacao, 
            text="xⁿ", 
            text_color='white',
            font=("Arial", 25),
            fg_color="orange",
            hover_color='#1C1C1C',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir("xⁿ")
        )

        self.potencia.place(
            relx=0.67,
            rely=0.48,
            relwidth=0.12,
            relheight=0.08
        )