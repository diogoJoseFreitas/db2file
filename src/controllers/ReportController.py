from views.FormView import FormView

class ReportController():
    def __init__(self):
        self.form = FormView()
    
    def showForm(self):
        self.form.show()
    
    def getFormResult(self) -> dict:
        return self.form.getResult()

if __name__ == "__main__":
    controller = ReportController()
    controller.showForm()
    print(controller.getFormResult())