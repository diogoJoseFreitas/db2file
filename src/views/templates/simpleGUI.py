import tkinter as tk
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


if __name__ == "__main__":
    layout = [
        [label(text="Nome do Arquivo"), textInput()], 
        [label(text="Data Início"), dateInput(days_from_today=-30), label(text="Data Fim"), dateInput()],
        [label(text="linha 2")]
    ]
    main = Window(layout=layout)

    main.mainloop()