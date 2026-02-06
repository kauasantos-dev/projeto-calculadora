from customtkinter import CTkButton, CTk, CTkToplevel, CTkLabel, CTkFrame
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
            fg_color='#360909',
            hover_color="#620707", 
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
            corner_radius=30,
            command=self.exibir_historico
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
    
    def exibir_historico(self):
        self.ver_historico = CTkToplevel(self.aplicacao, fg_color='black')
        self.ver_historico.title('Histórico de Operações')
        self.ver_historico.geometry('950x580')
        self.ver_historico.resizable(True, True)
        self.ver_historico.minsize(width=320, height=350)
        self.ver_historico.maxsize(width=1220, height=780)
        
        self.cabecalho = CTkLabel(
            master=self.ver_historico,
            text='Histórico de Operações',
            text_color='white',
            font=('Arial', 30),
            fg_color='black',
            anchor='s'
        )
        self.cabecalho.place(
            relx=0.06,
            rely=0.1,
        )
    
        self.linha_horizontal = CTkFrame(
            master=self.ver_historico,
            fg_color='white',
            height=4,
            corner_radius=30
        )
        self.linha_horizontal.place(
            relx=0.061,
            rely=0.165,
            relwidth=0.87
        )