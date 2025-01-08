from models.ExportModel import ExportModel


class ExportToCsv(ExportModel):
    def __init__(self, filepath):
        super().__init__(filepath)
    
    def export(self):
        if self.validateFile():
            print("Arquivo validado, exportando arquivo CSV...")
        pass
    