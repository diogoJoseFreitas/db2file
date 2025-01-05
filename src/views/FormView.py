from models.ScreenModel import ScreenModel as sc

class FormView(sc):
    def __init__(self):
        super().__init__("Gerador de Relatório por data", "500x300")
        self.label("Data Início:", (0, 0))
        self.data_inicio = self.dateInput((0, 1))
        self.label("Data Fim:", (0, 2))
        self.data_fim = self.dateInput((0, 3))
        self.button("Enviar", self.generateReport, (1, 1), colspan=2)
    
    def generateReport(self):
        inicio = self.data_inicio.get_date()
        fim = self.data_fim.get_date()
        if inicio>fim:
            self.alert("Erro de inserção", "A data de Início deve ser inferior a Data Final para gerar relatóro.")
        print("-="*15)
        print("Relatório atual:")
        print("Data de Início: ", self.data_inicio.get_date())
        print("Data Final: ", self.data_fim.get_date())
        print("-="*15)

if __name__ =="__main__":
    form = FormView()
    form.show()