from views.templates.simpleGUI import *

class newFormView():
    def __init__(self):
        self.data_inicio = dateInput()
        self.int_data_inicio = numberInput(1, command=lambda: self.data_inicio.setFromToday(self.int_data_inicio.get()))
        self.data_fim = dateInput()
        self.int_data_fim = numberInput( command=lambda: self.data_inicio.setFromToday(self.int_data_inicio.get()))
        self.fornecedores = textInput()
        self.pasta = textInput()
        self.cod_distrib = textInput()
        self.ftp_host = textInput()
        self.login = textInput()
        self.senha = textInput()
        
        
        