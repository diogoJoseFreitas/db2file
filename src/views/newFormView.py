from views.templates.simpleGUI import *

from os import path
import pandas as pd

class newFormView():
    def __init__(self):
        
        self.filename = 'data.csv'
        
        self.dt_inicio = dateInput()
        self.n_dt_inicio = numberInput(1, command=lambda: self.dt_inicio.setFromToday(-1*int(self.n_dt_inicio.get())))
        self.dt_fim = dateInput()
        self.n_dt_fim = numberInput( command=lambda: self.dt_inicio.setFromToday(self.n_dt_inicio.get()))
        self.fornecedores = textInput()
        self.pasta = textInput()
        self.cod_distrib = numberInput('00000000', width=10)
        self.ftp_host = textInput()
        self.login = textInput()
        self.senha = textInput()
        self.segmento = button('Segmento', command= lambda: print("Segmento Pressed"), width=10)
        self.log = button('log', command= lambda: print("log Pressed"), width=10)
        self.gerar_planilha = button('Gerar planilha de validação', command= lambda: print("gerar_planilha Pressed"))
        self.gerar_arquivos = button('gerar_arquivos', command= lambda: print("gerar_arquivos Pressed"))
        self.salvar = button("Salvar", command= lambda: self.updateData())
        
        self.layout = [
        [label("Período:"), self.dt_inicio, self.n_dt_inicio, label("a"), self.dt_fim, self.n_dt_fim],
        [label('Fornecedores:', width=15), self.fornecedores],
        [label('Pasta:*', width=15), self.pasta],
        [label('Cod. Distrib.', width=15), self.cod_distrib],
        [label('ftp host', width=15), self.ftp_host],
        [label('Login', width=15), self.login],
        [label('Senha', width=15), self.senha],
        [self.segmento],
        [self.log, self.gerar_planilha, self.gerar_arquivos, self.salvar]
        ]
        self.window = Window(layout=self.layout, geometry="420x250")
        self.loadData()
        
        self.window.start()
    
    def getForm(self) -> dict:
        formData = {
            'n_dt_inicio': [self.n_dt_inicio.get()],
            'n_dt_fim': [self.n_dt_fim.get()],
            'fornecedores':[self.fornecedores.get()],
            'pasta':[self.pasta.get()],
            'cod_distrib': [self.cod_distrib.get()],
            'ftp_host': [self.ftp_host.get()],
            'login':[self.login.get()],
            'senha': [self.senha.get()],
        }
        return formData
    
    def updateData(self):
        filepath = r'C:\Users\tecdisa\Documents\git-repositories\db2file\src\data'
        
        data = self.getForm()
        df = pd.DataFrame(data)
        df.to_csv(self.filename, index=False)
    
    def loadData(self):
        try:
            df = pd.read_csv(self.filename)
            data = dict(df.iloc[0])
        except:
            data = {
            'n_dt_inicio': 0,
            'n_dt_fim': 0,
            'fornecedores':'',
            'pasta':'',
            'cod_distrib': 0,
            'ftp_host': '',
            'login':'',
            'senha': '',
        }
        
        self.dt_inicio.setFromToday(-1*int(data['n_dt_inicio'])) 
        self.n_dt_inicio.set(data['n_dt_inicio'])
        self.dt_fim.setFromToday(data['n_dt_fim'])
        self.n_dt_fim.set(data['n_dt_fim'])
        self.fornecedores.setValue(data['fornecedores'])
        self.pasta.setValue(data['pasta'])
        self.cod_distrib.set(data['cod_distrib'])
        self.ftp_host.setValue(data['ftp_host'])
        self.login.setValue(data['login'])
        self.senha.setValue(data['senha'])
        
            
        
        
if __name__ == "__main__":
    teste = newFormView()
        