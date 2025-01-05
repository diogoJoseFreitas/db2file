from views.templates.guiInterfaceTemplate import guiInterfaceTemplate as git
from datetime import datetime
from dateutil.relativedelta import relativedelta

class FormView(git):
    def __init__(self):
        super().__init__("Gerador de Relatório por data", "500x300")

        self.label("Data Início:", position=(0, 0))
        self.start_date = self.dateInput(position=(0, 1))
        self.start_date.set_date((datetime.today() - relativedelta(months=1)))

        self.label("Data Fim:", position=(0, 2))
        self.end_date = self.dateInput(position=(0, 3))

        self.label("Formato de exportação:", position=(1, 1), columnspan=2)
        self.exportTo = self.combobox([".csv", ".json"], position=(1, 3), width=5)

        self.button("Enviar", self.generateReport, position=(2, 1), columnspan=2, sticky="nsew")

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
                "exportTo": self.exportTo.get()
            }
            
        self.destroy()

if __name__ =="__main__":
    form = FormView()
    form.show()