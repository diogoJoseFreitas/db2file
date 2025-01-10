from views.templates.guiInterfaceTemplate import guiInterfaceTemplate as git
from datetime import datetime
from dateutil.relativedelta import relativedelta

class FormView(git):
    def __init__(self):
        super().__init__("Gerador de Relatório por data", "400x200")
        
        self.filepath = self.textInput("Escolha um arquivo", position = (0,0), columnspan=3, sticky='ew', width = 50, padx=(5, 0))
        self.button('...', lambda : self.fileInput(self.filepath), width=3, sticky='w', position=(0, 3), padx=0)

        self.label("Data Início:", position=(1, 0))
        self.start_date = self.dateInput(position=(1, 1), sticky="w")
        self.start_date.set_date((datetime.today() - relativedelta(months=1)))

        self.label("Data Fim:", position=(1, 2))
        self.end_date = self.dateInput(position=(1, 3), sticky="w")

        self.label("Formato de exportação:", position=(2, 1), columnspan=2)
        self.exportTo = self.combobox([".csv", ".json"], position=(2, 3), width=5, sticky="w")

        self.button("Enviar", self.generateReport, position=(3, 1), columnspan=2, sticky="nsew")

        self.result = {}
    
    def getResult(self) -> dict:
        return self.result

    def generateReport(self):
        start = self.start_date.get_date()
        end = self.end_date.get_date()

        if start>end:
            self.alert("Erro de inserção", "A data de Início deve ser inferior a Data Final para gerar relatóro.")
        else:
            self.result ={
                "start_date": start,
                "end_date": end,
                "export_to": self.exportTo.get(),
                "file_path":self.filepath.get(),
            }
            
            self.destroy()

if __name__ =="__main__":
    form = FormView()
    form.show()