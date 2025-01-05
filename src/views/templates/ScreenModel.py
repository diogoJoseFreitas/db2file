import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry


class ScreenModel(tk.Tk):
    STYLE_DEFAULTS = {
        "width": 15,
        }
    GRID_DEFAULTS = {
        "position": (0, 0),
        "padx": 5,
        "pady": 5,
        "columnspan": 1,
        "rowspan": 1,
        "sticky": "w",
        }

    def __init__(self, title="", window_size="300x200", **kw):
        super().__init__(**kw)
        self.title(title)
        self.geometry(window_size)

    def show(self):
        self.mainloop()

    def _update_params(self, defaults:dict, custom_params:dict) -> dict[str, any]:
        result = defaults.copy()
        for k, v in custom_params.items():
            if k in result:
                result[k] = v
        return result

    def _grid(self, widget:tk.Entry, **kwargs):
        kwargs = self._update_params(self.GRID_DEFAULTS, kwargs)
        kwargs.update(row=kwargs["position"][0], column=kwargs["position"][1])
        del kwargs["position"]
        widget.grid(kwargs)
        return widget

    def label(self, text = "", **kwargs):
        kwargs.update(width=None)

        style_params = self._update_params(self.STYLE_DEFAULTS, kwargs)
        wdgt = tk.Label(master=self, text=text, **style_params)
        self._grid(wdgt, **kwargs)
    
    def textInput(self, **kwargs) -> tk.Entry:

        style_params = self._update_params(self.STYLE_DEFAULTS, kwargs)
        inp = tk.Entry(self, **style_params)

        self._grid(inp, **kwargs)
        return inp
    
    def dateInput(self, date_pattern="dd/mm/yyyy", **kwargs) -> DateEntry:
        kwargs.update(width=10)
        style_params = self._update_params(self.STYLE_DEFAULTS, kwargs)
        inp = DateEntry(self, date_pattern=date_pattern, **style_params)

        self._grid(inp, **kwargs)
        return inp
    
    def button(self, text = "", command = None, **kwargs):
        
        style_params = self._update_params(self.STYLE_DEFAULTS, kwargs)
        inp = tk.Button(self, text=text, command=command, **style_params)

        self._grid(inp, **kwargs)
    
    def combobox(self, values=[], default_value=0, **kwargs):

        style_params = self._update_params(self.STYLE_DEFAULTS, kwargs)
        inp = ttk.Combobox(self, values=values, **style_params)
        inp.set(values[default_value])
        
        self._grid(inp, **kwargs)
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