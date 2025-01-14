import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta


class Window(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None, geometry='400x300', layout = [[],[]]):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry(geometry)
        self.setLayout(self, layout)

    def setLayout(self, master, layout, frame_pack_args={'fill':'x', 'anchor':'n', 'pady':2}):
        frame = tk.Frame(master)
        for index, item in enumerate(layout):
            if isinstance(item, list):
                self.setLayout(frame, item)
            else:
                item.create(frame, ipadx=5)
        frame.pack(**frame_pack_args)
    
    def start(self):
        self.mainloop()
    
    def stop(self):
        self.destroy()


class label(tk.Label):
    def __init__(self, text = "", cnf = None, *, activebackground = None, activeforeground = None, anchor = "center", background = None, bd = None, bg = None, bitmap = "", border = None, borderwidth = None, compound = "none", cursor = "", disabledforeground = None, fg = None, font = "TkDefaultFont", foreground = None, height = 0, highlightbackground = None, highlightcolor = None, highlightthickness = 0, image = "", justify = "center", name = None, padx = 1, pady = 1, relief = "flat", state = "normal", takefocus = 0,  textvariable = None, underline = -1, width = 0, wraplength = 0):
        self.kwargs = {  # Store all provided arguments
            k: v for k, v in locals().items() if k != "self" and v is not None
        }
    
    def create(self, master = None, cnf = None, *, after = None, anchor=None, before=None, expand = False, fill= None, side='left', ipadx= 0, ipady= 0, padx: int | tuple[int, int] = 0,  pady: int | tuple[int, int] = 0, in_=None, **kwargs):
        super().__init__(master=master, **self.kwargs)

        args = {k: v for k, v in locals().items() if k not in ["self", 'master', 'kwargs', '__class__'] and v is not None}
        self.pack(**args)


class textInput(tk.Entry):
    def __init__(self, value = '', cnf = None, *, background = None, bd = None, bg = None, border = None, borderwidth = None, cursor = "xterm", disabledbackground = None, disabledforeground = None, exportselection = True, fg = None, font = "TkTextFont", foreground = None, highlightbackground = None, highlightcolor = None, highlightthickness = None, insertbackground = None, insertborderwidth = 0, insertofftime = 300, insertontime = 600, insertwidth = None, invalidcommand = "", invcmd = "", justify = "left", name = None, readonlybackground = None, relief = "sunken", selectbackground = None, selectborderwidth = None, selectforeground = None, show = "", state = "normal", takefocus = "", textvariable = None, validate = "none", validatecommand = "", vcmd = "", width = 5, xscrollcommand = ""):
        self.kwargs = {  # Store all provided arguments
            k: v for k, v in locals().items() if k not in ["self", 'value'] and v is not None
        }
        self.value = value
    
    def create(self, master = None, cnf = None, *, after = None, anchor=None, before=None, expand = True, fill= 'x', side='left', ipadx= 0, ipady= 0, padx: int | tuple[int, int] = (0, 5),  pady: int | tuple[int, int] = 0, in_=None, **kwargs):
        super().__init__(master=master, **self.kwargs)

        args = {k: v for k, v in locals().items() if k not in ["self", 'master', 'kwargs', '__class__'] and v is not None}
        self.pack(**args)
        self.setValue(self.value)

    def setValue(self, text=''):
        self.delete(0, tk.END)
        self.insert(0, text)

class numberInput(ttk.Spinbox):
    def __init__(self, value = 0, *, background = None, command = "", cursor = "", exportselection = None, font = None, foreground = None, format = "%0.0f", from_ = 0, increment = 1, invalidcommand = None, justify = None, name = None, show=None, state = "normal", style = "", takefocus = None, textvariable = None, to = 50, validate = "none", validatecommand = "", values = None, width = 3, wrap = False, xscrollcommand = ""):
        self.kwargs = {  # Store all provided arguments
            k: v for k, v in locals().items() if k not in ["self", 'value'] and v is not None
        }
        self.value = value
        
    def create(self, master = None, cnf = None, *, after = None, anchor=None, before=None, expand = True, fill= 'x', side='left', ipadx= 0, ipady= 0, padx: int | tuple[int, int] = (0, 5),  pady: int | tuple[int, int] = 0, in_=None, **kwargs):
        super().__init__(master=master, **self.kwargs)

        args = {k: v for k, v in locals().items() if k not in ["self", 'master', 'kwargs', '__class__'] and v is not None}
        self.pack(**args)
        self.set(self.value)
    
    def setValue(self, number=0):
        self.delete(0, tk.END)
        self.insert(0, number)
    


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
    
    def setFromToday(self, days_from_today=0):
        new_date = datetime.today() + timedelta(int(days=days_from_today))
        self.set_date(new_date)


class button(tk.Button):
    def __init__(self, text = "", command = "", cnf = None, *, activebackground = None, activeforeground = None, anchor = "center", background = None, bd = None, bg = None, bitmap = "", border = None, borderwidth = None,  compound = "none", cursor = "", default = "disabled", disabledforeground = None, fg = None, font = "TkDefaultFont", foreground = None, height = 0, highlightbackground = None, highlightcolor = None, highlightthickness = 1, image = "", justify = "center", name = None, overrelief = "", padx = None, pady = None, relief = None, repeatdelay = None, repeatinterval = None, state = "normal", takefocus = "",  textvariable = None, underline = -1, width = 0, wraplength = 0):
        self.kwargs = {  # Store all provided arguments
            k: v for k, v in locals().items() if k != "self" and v is not None
        }

    def create(self, master = None, cnf = None, *, after = None, anchor=None, before=None, expand = False, fill= None, side='left', ipadx= 0, ipady= 0, padx: int | tuple[int, int] = (0, 5),  pady: int | tuple[int, int] = 0, in_=None, **kwargs):
        super().__init__(master=master, **self.kwargs)
        args = {k: v for k, v in locals().items() if k not in ["self", 'master', 'kwargs', '__class__'] and v is not None}
        self.pack(**args)

class comBox():
    def __init__(self, values = [], width=5):
        self.kwargs = {  # Store all provided arguments
            k: v for k, v in locals().items() if k != "self" and v is not None
        }
        self.values = values

    def create(self, master = None, cnf = None, after = None, anchor=None, before=None, expand = False, fill= None, side='left', ipadx= 0, ipady= 0, padx: int | tuple[int, int] = (0, 5),  pady: int | tuple[int, int] = 0, in_=None, **kwargs):
        self.combobox = ttk.Combobox(master, **self.kwargs)
        
        args = {k: v for k, v in locals().items() if k not in ["self", 'master', 'kwargs', '__class__'] and v is not None}
        self.combobox.pack(**args)

if __name__ == "__main__":
    nome = textInput()
    # layout = [
    #     [label(text="Nome do Arquivo"), nome], 
    #     [label(text="Data Início"), dateInput(days_from_today=-30), label(text="Data Fim"), dateInput()],
    #     [label(text="Formato de Saída"), comBox(values=['.json', '.csv'])],
    #     [label(text="Enviar:"), button(text="Enviar", command=lambda: nome.setValue("Hello World"))]
    # ]
    
    teste = dateInput()
    number = numberInput(1, command=lambda: teste.setFromToday(-1*int(number.get())))
    layout = [
        [label("Período:"), teste, number, label("a"), dateInput(), numberInput(1)],
        [label('Fornecedores:'), textInput()],
        [label('Pasta:*'), textInput()],
        [label('Cod. Distrib.'), textInput('00000000')],
        [label('ftp host'), textInput('')],
        [label('Login'), textInput('')],
        [label('Senha'), textInput('')],
    ]
    main = Window(layout=layout)
    
    main.setLayout(main, 
        [[button('Segmento')],
        [button('Log'), button('Gerar planilha de validação'), button('Gerar arquivos')]],
        {'fill': 'x', 'anchor': 'n', 'pady': 2}
        )
    
    main.mainloop()
