from views.templates.guiInterfaceTemplate import guiInterfaceTemplate as git

class FormView(git):
    def __init__(self):
        super().__init__("Gerador de Relatório por data", "500x300")
        self.label("Data Início:", position=(0, 0))
        self.start_date = self.dateInput(position=(0, 1))
        self.label("Data Fim:", position=(0, 2))
        self.end_date = self.dateInput(position=(0, 3))
        self.label("Formato de exportação:", position=(1, 1), columnspan=2)
        self.exportTo = self.combobox([".csv", ".json"], position=(1, 3), width=5)
        self.button("Enviar", self.generateReport, position=(2, 1), columnspan=2, sticky="nsew")
    
    def generateReport(self):
        start = self.start_date.get_date()
        end = self.end_date.get_date()
        if start>end:
            self.alert("Erro de inserção", "A data de Início deve ser inferior a Data Final para gerar relatóro.")
        print("-="*15)
        print("Relatório atual:")
        print("Data de Início:", self.start_date.get_date())
        print("Data Final:", self.end_date.get_date())
        print("Formato do arquivo gerado:", self.exportTo.get())
        print("-="*15)

if __name__ =="__main__":
    form = FormView()
    form.show()