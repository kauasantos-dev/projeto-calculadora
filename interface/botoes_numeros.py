from customtkinter import CTkButton, CTk
from display_resultado import DisplayResultadoOperacoes

class NumerosCalculadora:
    def __init__(self, aplicacao: CTk, display_resultados: DisplayResultadoOperacoes):
        self.aplicacao = aplicacao
        self.display_resultados = display_resultados

    def valores(self):
        self.numero7 = CTkButton(
            master=self.aplicacao, 
            text="7", 
            font=("Arial", 16),
            fg_color="white",
            command=lambda: self.display_resultados.inserir(7)
        )

        self.numero7.place(
            x=300,
            y=200,
            relwidth=0.2,
            relheight=0.01
       )
        
        self.numero8 = CTkButton(
            master=self.aplicacao, 
            text="8", 
            font=("Arial", 16),
            fg_color="white",
            command=lambda: self.display_resultados.inserir(8)
        )

        self.numero8.place(
            x=300,
            y=200
        )

        self.numero9 = CTkButton(
            master=self.aplicacao, 
            text="9", 
            font=("Arial", 16),
            fg_color="white", 
            width=300,
            height=200,
            command=lambda: self.display_resultados.inserir(9)
        )
        self.numero9.place(
            x=300,
            y=200
        )

        self.numero4 = CTkButton(
            master=self.aplicacao, 
            text="4", 
            font=("Arial", 16), 
            fg_color="white",
            command=lambda: self.display_resultados.inserir(4)
        )

        self.numero4.place(
            x=300,
            y=200,
        )

        self.numero5 = CTkButton(
            master=self.aplicacao, 
            text="5", 
            font=("Arial", 16),
            fg_color="white",
            command=lambda: self.display_resultados.inserir(5)
        )

        self.numero5.place(
            x=300,
            y=200
        )

        self.numero6 = CTkButton(
            self.aplicacao, 
            text="6", 
            font=("Arial", 16),
            fg_color="white",
            command=lambda: self.display_resultados.inserir(6)
            )
        
        self.numero6.place(
            x=300,
            y=200,
        )

        self.numero1 = CTkButton(
            master=self.aplicacao, 
            text="1", 
            font=("Arial", 16), 
            fg_color="white",
            command=lambda: self.display_resultados.inserir(1)
        )
        self.numero1.place(
            x=300,
            y=200
        )

        self.numero2 = CTkButton(
            master=self.aplicacao, 
            text="2", 
            font=("Arial", 16), 
            fg_color="black",
            command=lambda: self.display_resultados.inserir(2)
        )
        self.numero2.place(
            x=300,
            y=200
        )

        self.numero3 = CTkButton(
            master=self.aplicacao, 
            text="3", 
            font=("Arial", 16),
            fg_color="white",
            command=lambda: self.display_resultados.inserir(3)
        )
        self.numero3.place(
            x=300,
            y=200
        )

        self.numero0 = CTkButton(
            master=self.aplicacao, 
            text="0", 
            font=("Arial", 16),
            fg_color="white",
            command=lambda: self.display_resultados.inserir(0)
        )

        self.numero0.place(
            x=300,
            y=200
        )