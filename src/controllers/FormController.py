from views.FormView import FormView

class FormController():
    def __init__(self):
        self.form = FormView()
    
    def showForm(self):
        self.form.show()
    
    def getFormResult(self) -> dict:
        return self.form.getResult()

if __name__ == "__main__":
    controller = FormController()
    controller.showForm()
    print(controller.getFormResult())