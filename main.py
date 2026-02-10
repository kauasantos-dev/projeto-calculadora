from customtkinter import *
from interface.botoes_numeros import NumerosCalculadora
from interface.botoes_operadores import OperadoresCalculadora
from interface.ver_apagar_historico import GerenciarHistorico
from interface.botoes_ponto_igual import BotoesPontoIgual
from interface.display_resultado import DisplayResultadoOperacoes

class Calculadora(CTk):
    def __init__(self):
        super().__init__()
        self.janela_principal()
        self.display_resultados = DisplayResultadoOperacoes(self)
        self.display_resultados.frame_resultado_operacoes()
        NumerosCalculadora(self, self.display_resultados).valores()
        OperadoresCalculadora(self, self.display_resultados).operadores_aritmeticos()
        GerenciarHistorico(self, self.display_resultados).botoes_gerenciar_historico()
        BotoesPontoIgual(self, self.display_resultados).botoes_ponto_igual()
        self.mainloop()
    
    def janela_principal(self):
        self._set_appearance_mode("light")
        self.configure(fg_color="black")
        self.title("Calculadora")
        self.geometry("550x580")
        self.resizable(True, True)
        self.minsize(width=320, height=350)
        self.maxsize(width=720, height=880)

calculadora = Calculadora()
