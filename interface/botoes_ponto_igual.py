from customtkinter import CTkButton, CTk

class BotoesPontoIgual:
    def __init__(self, aplicacao: CTk):
        self.aplicacao = aplicacao

    def botoes_ponto_igual(self):
        self.ponto = CTkButton(
            master=self.aplicacao,
            text=".",
            font=("Arial", 20),
            fg_color="orange",
        )

        self.ponto.place(
            x=100,
            y=100,
            relwidth=0.14,
            relheight=0.09
        )

        self.igual = CTkButton(
            master=self.aplicacao,
            text="=", font=("Arial", 20),
            font=("Arial", 20),
            fg_color="orange"
        )

        self.igual.place(
            x=100,
            y=100,
            relwidth=0.14,
            relheight=0.09
        )