import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta


class Window(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None, geometry='400x300', layout = [[],[]]):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry(geometry)
        self.setLayout(self, layout)

    def setLayout(self, master, layout):
        frame = tk.Frame(master)
        for index, item in enumerate(layout):
            if isinstance(item, list):
                self.setLayout(frame, item)
            else:
                item.create(frame, ipadx=5)
        frame.pack(fill='x', anchor='n')


class label(tk.Label):
    def __init__(self, cnf = None, *, activebackground = None, activeforeground = None, anchor = "center", background = None, bd = None, bg = None, bitmap = "", border = None, borderwidth = None, compound = "none", cursor = "", disabledforeground = None, fg = None, font = "TkDefaultFont", foreground = None, height = 0, highlightbackground = None, highlightcolor = None, highlightthickness = 0, image = "", justify = "center", name = None, padx = 1, pady = 1, relief = "flat", state = "normal", takefocus = 0, text = "", textvariable = None, underline = -1, width = 0, wraplength = 0):
        self.kwargs = {  # Store all provided arguments
            k: v for k, v in locals().items() if k != "self" and v is not None
        }
    
    def create(self, master = None, cnf = None, *, after = None, anchor=None, before=None, expand = False, fill= None, side='left', ipadx= 0, ipady= 0, padx: int | tuple[int, int] = 0,  pady: int | tuple[int, int] = 0, in_=None, **kwargs):
        super().__init__(master=master, **self.kwargs)

        args = {k: v for k, v in locals().items() if k not in ["self", 'master', 'kwargs', '__class__'] and v is not None}
        self.pack(**args)


class textInput(tk.Entry):
    def __init__(self, cnf = None, *, background = None, bd = None, bg = None, border = None, borderwidth = None, cursor = "xterm", disabledbackground = None, disabledforeground = None, exportselection = True, fg = None, font = "TkTextFont", foreground = None, highlightbackground = None, highlightcolor = None, highlightthickness = None, insertbackground = None, insertborderwidth = 0, insertofftime = 300, insertontime = 600, insertwidth = None, invalidcommand = "", invcmd = "", justify = "left", name = None, readonlybackground = None, relief = "sunken", selectbackground = None, selectborderwidth = None, selectforeground = None, show = "", state = "normal", takefocus = "", textvariable = None, validate = "none", validatecommand = "", vcmd = "", width = 20, xscrollcommand = ""):
        self.kwargs = {  # Store all provided arguments
            k: v for k, v in locals().items() if k != "self" and v is not None
        }
    
    def create(self, master = None, cnf = None, *, after = None, anchor=None, before=None, expand = True, fill= 'x', side='left', ipadx= 0, ipady= 0, padx: int | tuple[int, int] = (0, 5),  pady: int | tuple[int, int] = 0, in_=None, **kwargs):
        super().__init__(master=master, **self.kwargs)

        args = {k: v for k, v in locals().items() if k not in ["self", 'master', 'kwargs', '__class__'] and v is not None}
        self.pack(**args)

    def setValue(self, text=''):
        self.delete(0, tk.END)
        self.insert(0, text)


class dateInput(DateEntry):
    def __init__(self,date_pattern="dd/mm/yyyy", days_from_today:int=0, width=10, **kw):
        temp = dict(locals().items())
        temp.update(**kw)
        temp.pop("kw")
        self.date = datetime.today() + timedelta(days=days_from_today)
        self.kwargs = {
            k: v for k, v in temp.items() if k != "self" and v is not None
        }
    
    def create(self, master = None, cnf = None, *, after = None, anchor=None, before=None, expand = False, fill= None, side='left', ipadx= 0, ipady= 0, padx: int | tuple[int, int] = (0, 5),  pady: int | tuple[int, int] = 0, in_=None, **kwargs):
        super().__init__(master=master, **self.kwargs)
        self.set_date(self.date)
        args = {k: v for k, v in locals().items() if k not in ["self", 'master', 'kwargs', '__class__'] and v is not None}
        self.pack(**args)


class button(tk.Button):
    def __init__(self, cnf = None, *, activebackground = None, activeforeground = None, anchor = "center", background = None, bd = None, bg = None, bitmap = "", border = None, borderwidth = None, command = "", compound = "none", cursor = "", default = "disabled", disabledforeground = None, fg = None, font = "TkDefaultFont", foreground = None, height = 0, highlightbackground = None, highlightcolor = None, highlightthickness = 1, image = "", justify = "center", name = None, overrelief = "", padx = None, pady = None, relief = None, repeatdelay = None, repeatinterval = None, state = "normal", takefocus = "", text = "", textvariable = None, underline = -1, width = 0, wraplength = 0):
        self.kwargs = {  # Store all provided arguments
            k: v for k, v in locals().items() if k != "self" and v is not None
        }

    def create(self, master = None, cnf = None, *, after = None, anchor=None, before=None, expand = False, fill= None, side='left', ipadx= 0, ipady= 0, padx: int | tuple[int, int] = (0, 5),  pady: int | tuple[int, int] = 0, in_=None, **kwargs):
        super().__init__(master=master, **self.kwargs)
        args = {k: v for k, v in locals().items() if k not in ["self", 'master', 'kwargs', '__class__'] and v is not None}
        self.pack(**args)

class comBox():
    def __init__(self, *, values = [], background = None, class_ = "", cursor = "", exportselection = True, font = None, foreground = None, height = 10, invalidcommand = None, justify = "left", name = None, postcommand = "", show=None, state = "normal", style = "", takefocus = None, validate = None, validatecommand = None, width = 20, xscrollcommand = None):
        self.kwargs = {  # Store all provided arguments
            k: v for k, v in locals().items() if k not in ["self", "values"] and v is not None
        }
        self.values = values

    def create(self, master = None, cnf = None, *, after = None, anchor=None, before=None, expand = False, fill= None, side='left', ipadx= 0, ipady= 0, padx: int | tuple[int, int] = (0, 5),  pady: int | tuple[int, int] = 0, in_=None, **kwargs):
        # self.text_variable = tk.StringVar()
        self.combobox = ttk.Combobox(master=master,**self.kwargs)
        args = {k: v for k, v in locals().items() if k not in ["self", 'master', 'kwargs', '__class__'] and v is not None}
        self.combobox.pack(**args)
        self.combobox['values'] = self.values

if __name__ == "__main__":
    nome = textInput()
    layout = [
        [label(text="Nome do Arquivo"), nome], 
        [label(text="Data Início"), dateInput(days_from_today=-30), label(text="Data Fim"), dateInput()],
        [comBox(values=['.json', '.csv'])],
        [label(text="Enviar:"), button(text="Enviar", command=lambda: nome.setValue("Hello World"))]
    ]
    main = Window(layout=layout)

    teste = ttk.Combobox(main)
    teste.pack()
    teste['values'] = ['teste', 'teste2']

    # Explicit combobox creation and packing
    combox_instance = comBox(values=['.json', '.csv'])
    combox_instance.create(main)


    main.mainloop()
