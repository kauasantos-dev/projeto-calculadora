from customtkinter import CTkButton, CTk
from .display_resultado import DisplayResultadoOperacoes

class GerenciarHistorico:
    def __init__(self, aplicacao: CTk, display_resultados: DisplayResultadoOperacoes):
        self.aplicacao = aplicacao
        self.display_resultados = display_resultados
    
    def historico_operacoes(self):
        self.apagar_historico = CTkButton(
            master=self.aplicacao,
            text='Apagar Histórico',
            text_color='white',
            font=('Arial', 16),
            fg_color='orange',
            hover_color='#1C1C1C', 
            corner_radius=30
        )

        self.apagar_historico.place(
            relx=0.1,
            rely=0.66,
            relwidth=0.38,
            relheight=0.09
        )

        self.ver_historico = CTkButton(
            master=self.aplicacao,
            text="Ver Histórico", 
            text_color='white',
            font=("Arial", 16),
            fg_color="orange", 
            hover_color='#1C1C1C',
            corner_radius=30
        )

        self.ver_historico.place(
            relx=0.67,
            rely=0.66,
            relwidth=0.25,
            relheight=0.09
        )

        self.apagar_display = CTkButton(
            master=self.aplicacao,
            text="Limpar",
            text_color='white',
            font=("Arial", 16),
            fg_color="orange",
            hover_color='#1C1C1C',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir(None)
        )

        self.apagar_display.place(
            relx=0.23,
            rely=0.57,
            relwidth=0.25,
            relheight=0.08
        )
