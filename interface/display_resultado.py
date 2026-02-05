from customtkinter import CTk, CTkFrame, StringVar, CTkLabel
from cfgcalculadora import validacoes

class DisplayResultadoOperacoes:
    def __init__(self, aplicacao: CTk):
        self.aplicacao = aplicacao
        self.valor_display = StringVar()
        self.valor_display.set("0")

    def frame_resultado_operacoes(self):
        self.frame_resultados = CTkFrame(
            master=self.aplicacao, 
            fg_color="black",
        )

        self.frame_resultados.place(
            relx=0.1, 
            rely=0.05,
            relwidth=0.8, 
            relheight=0.16
        )

        self.display = CTkLabel(
            self.frame_resultados,
            textvariable=self.valor_display,
            fg_color="black",
            text_color="white",
            anchor="e",
            font=("Arial", 30),
        )

        self.display.place(
            relwidth=1,
            relheight=1
        )
    
    def inserir(self, valor):
        valor_atual = self.valor_display.get()
        resultado_validacao_operacao = validacoes.validar_operacao(valor, valor_atual)
        if resultado_validacao_operacao:
            self.valor_display.set(resultado_validacao_operacao)
        else:
            self.valor_display.set(valor_atual + str(valor))