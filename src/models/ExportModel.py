from os import path

class ExportModel:
    def __init__(self, filepath:str):
        self.filepath = filepath
    
    def validateFile(self) -> bool:
        return path.isfile(self.filepath)
        
    def export(self) -> str:
        pass