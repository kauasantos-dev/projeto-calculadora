from tkinter import Button, Tk
from .display_resultado import DisplayResultadoOperacoes

class GerenciarHistorico:
    def __init__(self, aplicacao: Tk, display_resultados: DisplayResultadoOperacoes):
        self.aplicacao = aplicacao
        self.display_resultados = display_resultados
    
    def historico_operacoes(self):
        self.ver_historico = Button(
            self.aplicacao,
            text="Ver Histórico", 
            font=("Arial", 12),
            background="orange", 
            fg="white",
            bd=1,
            relief="raised"
        )

        self.ver_historico.place(
            relx=0.61,
            rely=0.70,
            relwidth=0.29,
            relheight=0.09
        )

        self.apagar_historico = Button(
            self.aplicacao,
            text="Apagar Histórico", 
            font=("Arial", 12),
            background="orange", 
            fg="white",
            bd=1,
            relief="raised"
        )

        self.apagar_historico.place(
            relx=0.1,
            rely=0.70,
            relwidth=0.44,
            relheight=0.09
        )

        self.apagar_display = Button(
            self.aplicacao,
            text="Limpar",
            font=("Arial", 12),
            background="orange",
            fg="white",
            bd=1,
            relief="raised",
            command=lambda: self.display_resultados.inserir(None)
        )

        self.apagar_display.place(
            relx=0.61,
            rely=0.60,
            relwidth=0.29,
            relheight=0.09
        )
