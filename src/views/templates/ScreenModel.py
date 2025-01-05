import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry


class ScreenModel(tk.Tk):
    PADX = 5
    PADY = 5
    WIDTH = 25

    def __init__(self, title="", window_size="300x200", **kw):
        super().__init__(**kw)
        self.title(title)
        self.geometry(window_size)

    def show(self):
        self.mainloop()

    def label(self, text = "", positon=(0, 0), width=None, padx=PADX, pady= PADY, colspan=1, rowspan = 1, sticky="w", **kwargs):
        tk.Label(master=self, text=text, width=width, **kwargs).grid(row=positon[0], column=positon[1], padx=padx, pady=pady, columnspan=colspan, rowspan=rowspan, sticky=sticky)
    
    def textInput(self, positon=(0, 0), width=WIDTH, padx=PADX, pady= PADY, colspan=1, rowspan = 1, **kwargs) -> tk.Entry:
        inp = tk.Entry(self, width=width, **kwargs)
        inp.grid(row=positon[0], column=positon[1], padx=padx, pady=pady, columnspan=colspan, rowspan=rowspan, sticky="w")
        return inp
    
    def dateInput(self, positon=(0, 0), width=10, padx=PADX, pady= PADY, colspan=1, rowspan = 1, date_pattern="dd/mm/yyyy", **kwargs) -> DateEntry:
        inp = DateEntry(self, width=width, date_pattern=date_pattern)
        inp.grid(row=positon[0], column=positon[1], padx=padx, pady=pady, columnspan=colspan, rowspan=rowspan, sticky="w")
        return inp
    
    def button(self, text = "", command = None, positon=(0, 0), width=WIDTH, padx=PADX, pady= PADY, colspan=1, rowspan = 1, **kwargs):
        tk.Button(self, text=text, command=command, width=width, **kwargs).grid(row=positon[0], column=positon[1], padx=padx, pady=pady, columnspan=colspan, rowspan=rowspan, sticky="w")
    
    def combobox(self, values=[], positon=(0, 0), default_value=0, width=5, padx=PADX, pady= PADY, colspan=1, rowspan = 1, **kwargs):
        inp = ttk.Combobox(self, values=values, width=width,**kwargs)
        inp.set(values[default_value])
        inp.grid(row=positon[0], column=positon[1], padx=padx, pady=pady, columnspan=colspan, rowspan=rowspan, sticky="w")
        return inp
    
    def alert(self, title="", message=""):
        messagebox.showinfo(title, message)


if __name__ == "__main__":
    # Teste de execução
    root = ScreenModel("Teste", "500x300")
    root.label("Nome: ", (0, 0))
    root.textInput((0, 1))
    root.label("Data de Nascimento: ", (1, 0))
    root.dateInput((1, 1))
    root.button("Terminate", lambda: root.alert("teste", "teste"), (2, 1))
    root.show()