from customtkinter import CTkButton, CTk, CTkToplevel, CTkLabel, CTkFrame, CTkTextbox
from .display_resultado import DisplayResultadoOperacoes
from cfgcalculadora import uteis
from tkinter import messagebox

class GerenciarHistorico:
    def __init__(self, janela_principal: CTk, display_resultados: DisplayResultadoOperacoes):
        self.janela_principal = janela_principal
        self.display_resultados = display_resultados
    
    def botoes_gerenciar_historico(self):
        self.ver_historico = CTkButton(
            master=self.janela_principal,
            text='Ver Histórico', 
            text_color='white',
            font=('Arial', 16),
            fg_color='orange', 
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
        
        self.apagar_historico = CTkButton(
            master=self.janela_principal,
            text='Apagar Histórico',
            text_color='white',
            font=('Arial', 16),
            fg_color='#360909',
            hover_color='#620707', 
            corner_radius=30,
            command=self.mostrar_mensagem_historico_apagado
        )

        self.apagar_historico.place(
            relx=0.1,
            rely=0.66,
            relwidth=0.38,
            relheight=0.09
        )

        self.limpar_display = CTkButton(
            master=self.janela_principal,
            text='Limpar',
            text_color='white',
            font=('Arial', 16),
            fg_color='orange',
            hover_color='#1C1C1C',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir(None)
        )

        self.limpar_display.place(
            relx=0.23,
            rely=0.57,
            relwidth=0.25,
            relheight=0.08
        )
    
    def exibir_historico(self):
        self.janela_exibir_historico = CTkToplevel(self.janela_principal, fg_color='black')
        self.janela_exibir_historico.title('Histórico de Operações')
        self.janela_exibir_historico.geometry('950x580')
        self.janela_exibir_historico.resizable(True, True)
        self.janela_exibir_historico.minsize(width=320, height=350)
        self.janela_exibir_historico.maxsize(width=1220, height=780)
        
        self.cabecalho = CTkLabel(
            master=self.janela_exibir_historico,
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
            master=self.janela_exibir_historico,
            fg_color='orange',
            height=4,
            corner_radius=30
        )
        self.linha_horizontal.place(
            relx=0.061,
            rely=0.167,
            relwidth=0.87
        )

        self.mostrar_historico = CTkTextbox(
            master=self.janela_exibir_historico,
            fg_color='black',
            text_color='white',
            font=('Arial', 20)
        )
        self.mostrar_historico.place(
            relx=0.061,
            rely=0.25,
            relwidth=0.87,
            relheight=0.5
        )
        self.mostrar_historico.insert(
            index='0.0', 
            text=uteis.ver_historico()
        )
        self.mostrar_historico.configure(state='disabled')

    def mostrar_mensagem_historico_apagado(self):
        historico_apagado = uteis.apagar_historico()
        if historico_apagado:
            messagebox.showinfo(title='Histórico de Operações', message='Histórico apagado com sucesso!')
        else:
            messagebox.showwarning(title='Histórico de Operações', message='O histórico de operações já está vazio.')