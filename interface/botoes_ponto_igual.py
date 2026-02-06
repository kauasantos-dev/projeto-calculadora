from .display_resultado import DisplayResultadoOperacoes
from customtkinter import CTkButton, CTk

class BotoesPontoIgual:
    def __init__(self, aplicacao: CTk, display_resultados: DisplayResultadoOperacoes):
        self.aplicacao = aplicacao
        self.display_resultados = display_resultados

    def botoes_ponto_igual(self):
        self.ponto = CTkButton(
            master=self.aplicacao, 
            text=".", 
            text_color='white',
            font=("Arial", 35),
            fg_color="orange",
            hover_color='#1C1C1C',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir(".")
        )

        self.ponto.place(
            relx=0.67,
            rely=0.57,
            relwidth=0.12,
            relheight=0.08
        )

        self.igual = CTkButton(
            master=self.aplicacao, 
            text="=", 
            text_color='white',
            font=("Arial", 25),
            fg_color="orange",
            hover_color='#1C1C1C',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir("=")
        )

        self.igual.place(
            relx=0.8,
            rely=0.57,
            relwidth=0.12,
            relheight=0.08
        )