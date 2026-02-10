from customtkinter import CTkButton, CTk
from .display_resultado import DisplayResultadoOperacoes

class NumerosCalculadora:
    def __init__(self, janela_principal: CTk, display_resultados: DisplayResultadoOperacoes):
        self.janela_principal = janela_principal
        self.display_resultados = display_resultados

    def valores(self):
        self.numero7 = CTkButton(
            master=self.janela_principal, 
            text='7',
            text_color='white',
            font=('Arial', 20),
            fg_color='#1C1C1C',
            corner_radius=30,
            hover_color='orange',
            command=lambda: self.display_resultados.inserir(7)
        )

        self.numero7.place(
            relx=0.1,
            rely=0.3,
            relwidth=0.12,
            relheight=0.08
       )
        
        self.numero8 = CTkButton(
            master=self.janela_principal, 
            text='8', 
            text_color='white',
            font=('Arial', 20),
            fg_color='#1C1C1C',
            hover_color='orange',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir(8)
        )

        self.numero8.place(
            relx=0.23,
            rely=0.3,
            relwidth=0.12,
            relheight=0.08
        )

        self.numero9 = CTkButton(
            master=self.janela_principal, 
            text='9', 
            text_color='white',
            font=('Arial', 20),
            fg_color='#1C1C1C',
            hover_color='orange',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir(9)
        )
        self.numero9.place(
            relx=0.36,
            rely=0.3,
            relwidth=0.12,
            relheight=0.08
        )

        self.numero4 = CTkButton(
            master=self.janela_principal, 
            text='4',
            text_color='white',
            font=('Arial', 20), 
            fg_color='#1C1C1C',
            hover_color='orange',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir(4)
        )

        self.numero4.place(
            relx=0.1,
            rely=0.39,
            relwidth=0.12,
            relheight=0.08
        )

        self.numero5 = CTkButton(
            master=self.janela_principal, 
            text='5', 
            text_color='white',
            font=('Arial', 20),
            fg_color='#1C1C1C',
            hover_color='orange',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir(5)
        )

        self.numero5.place(
            relx=0.23,
            rely=0.39,
            relwidth=0.12,
            relheight=0.08
        )

        self.numero6 = CTkButton(
            self.janela_principal, 
            text='6', 
            text_color='white',
            font=('Arial', 20),
            fg_color='#1C1C1C',
            hover_color='orange',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir(6)
            )
        
        self.numero6.place(
            relx=0.36,
            rely=0.39,
            relwidth=0.12,
            relheight=0.08
        )

        self.numero1 = CTkButton(
            master=self.janela_principal, 
            text='1',
            text_color='white',
            font=('Arial', 20), 
            fg_color='#1C1C1C',
            hover_color='orange',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir(1)
        )
        self.numero1.place(
            relx=0.1,
            rely=0.48,
            relwidth=0.12,
            relheight=0.08
        )

        self.numero2 = CTkButton(
            master=self.janela_principal, 
            text='2',
            text_color='white', 
            font=('Arial', 20), 
            fg_color='#1C1C1C',
            hover_color='orange',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir(2)
        )
        self.numero2.place(
            relx=0.23,
            rely=0.48,
            relwidth=0.12,
            relheight=0.08
        )

        self.numero3 = CTkButton(
            master=self.janela_principal, 
            text='3', 
            text_color='white',
            font=('Arial', 20),
            fg_color='#1C1C1C',
            hover_color='orange',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir(3)
        )
        self.numero3.place(
            relx=0.36,
            rely=0.48,
            relwidth=0.12,
            relheight=0.08
        )

        self.numero0 = CTkButton(
            master=self.janela_principal, 
            text='0',
            text_color='white', 
            font=('Arial', 20),
            fg_color='#1C1C1C',
            hover_color='orange',
            corner_radius=30,
            command=lambda: self.display_resultados.inserir(0)
        )

        self.numero0.place(
            relx=0.1,
            rely=0.57,
            relwidth=0.12,
            relheight=0.08
        )