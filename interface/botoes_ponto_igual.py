from customtkinter import CTkButton, CTk

class BotoesPontoIgual:
    def __init__(self, aplicacao: CTk):
        self.aplicacao = aplicacao

    def botoes_ponto_igual(self):
        self.ponto = CTkButton(
            master=self.aplicacao, 
            text=".", 
            text_color='white',
            font=("Arial", 25),
            fg_color="orange",
            hover_color='#1C1C1C',
            corner_radius=30
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
            corner_radius=30
        )

        self.igual.place(
            relx=0.8,
            rely=0.57,
            relwidth=0.12,
            relheight=0.08
        )