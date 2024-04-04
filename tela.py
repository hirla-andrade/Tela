from datetime import datetime
from tkinter import *
#from relatorio_notas_rnce import *



class TelaBD:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.tituloContainer = Frame(master)
        self.tituloContainer["pady"] = 10
        self.tituloContainer.pack()

        self.datainiContainer = Frame(master)
        self.datainiContainer["padx"] = 20
        self.datainiContainer.pack()

        self.datafinContainer = Frame(master)
        self.datafinContainer["padx"] = 20
        self.datafinContainer.pack()

        self.botaoContainer = Frame(master)
        self.botaoContainer["pady"] = 20
        self.botaoContainer.pack()

        self.resultContainer = Frame(master)
        self.botaoContainer["pady"] = 20
        self.botaoContainer.pack()

        self.titulo = Label(self.tituloContainer, text="Consulta SQL")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        # Data inicial
        self.datainiLabel = Label(self.datainiContainer,text="Data Inicial", font=self.fontePadrao)
        self.datainiLabel.pack(side=LEFT)

        self.dataini = Entry(self.datainiContainer)
        self.dataini["width"] = 30
        self.dataini["font"] = self.fontePadrao
        self.dataini.pack(side=LEFT)

        # Data final
        self.datafinLabel = Label(self.datafinContainer, text="Data Final", font=self.fontePadrao)
        self.datafinLabel.pack(side=LEFT)

        self.datafin = Entry(self.datafinContainer)
        self.datafin["width"] = 30
        self.datafin["font"] = self.fontePadrao
        self.datafin.pack(side=LEFT)

        # Botão cuidado nesse campo aqi.
        self.btbuscar = Button(self.botaoContainer)
        self.btbuscar["text"] = "Buscar Dados"
        self.btbuscar["font"] = ("Calibri", "12")
        self.btbuscar["width"] = 20
        self.btbuscar["command"] = self.fazerConsulta
        self.btbuscar.pack()

        self.resultado = Label(self.resultContainer, text="", font=self.fontePadrao)
        self.resultado.pack()

        
    def fazerConsulta(self):
        data_inicial = self.dataini.get()
        data_final = self.datafin.get()
        return data_inicial, data_final
  

tela = Tk()
TelaBD(tela)
tela.mainloop()