from abc import abstractmethod
from tkinter import *

from calcs.Method import Method
from calcs.MullerMethod import MullerMethod
from calcs.NewtonMethod import NewtonMethod
from calcs.RegulaFalsiMethod import RegulaFalsiMethod

from calcs.SecantMethod import SecantMethod
from data.classes import LatexSection

class MainPanel:
    method_calc: Method
    fn: str

    def __init__(self, root, frame, slug, onLoad) -> None:
        self.root = root
        self.frame = frame

        if onLoad is not None:
            onLoad()

    @abstractmethod
    def calc_init(self, params):
        pass

class SecantPanel(MainPanel):
    def __init__(self, root, frame, onLoad):
        MainPanel.__init__(self, root, frame, "Secante", onLoad)

        Label(self.frame, text="Valor para xa:").grid(row=1, column=1)
        self.xa_entry = Entry(self.frame, relief="raised")
        self.xa_entry.grid(row=1,column=2,columnspan=3)

        Label(self.frame, text="Valor para xb:").grid(row=2, column=1)
        self.xb_entry = Entry(self.frame, relief="raised")
        self.xb_entry.grid(row=2, column=2,columnspan=3)

        Label(self.frame, text="Tolerancia:").grid(row=3, column=1)
        self.tol_entry = Entry(self.frame, relief="raised")
        self.tol_entry.grid(row=3, column=2, columnspan=3)

    def calc_init(self, params):
        fn, directory = params

        xa = float(self.xa_entry.get())
        xb = float(self.xb_entry.get())
        tol = float(self.tol_entry.get())

        self.method_calc = SecantMethod(fn, xa, xb, tol)
        
        return "Secante", [LatexSection("math", "Ecuación", fn)] + (self.method_calc.to_info())

class MullerPanel(MainPanel):
    def __init__(self, root, frame, onLoad):
        MainPanel.__init__(self, root, frame, "Muller", onLoad)

        Label(self.frame, text="Valor para x0:").grid(row=0, column=1)
        self.x0_entry = Entry(self.frame, relief="raised")
        self.x0_entry.grid(row=0,column=2,columnspan=3)

        Label(self.frame, text="Valor para x1:").grid(row=1, column=1)
        self.x1_entry = Entry(self.frame, relief="raised")
        self.x1_entry.grid(row=1, column=2,columnspan=3)
        
        Label(self.frame, text="Valor para x2:").grid(row=2, column=1)
        self.x2_entry = Entry(self.frame, relief="raised")
        self.x2_entry.grid(row=2, column=2,columnspan=3)

        Label(self.frame, text="Tolerancia:").grid(row=3, column=1)
        self.tol_entry = Entry(self.frame, relief="raised")
        self.tol_entry.grid(row=3, column=2, columnspan=3)

    def calc_init(self, params):
        fn, directory = params

        x0 = float(self.x0_entry.get())
        x1 = float(self.x1_entry.get())
        x2 = float(self.x2_entry.get())
        
        tol = float(self.tol_entry.get())

        self.method_calc = MullerMethod(fn, x0, x1, x2, tol)

        return "Muller", [LatexSection("math", "Ecuación", fn)] + (self.method_calc.to_info())

class RegulaFalsiPanel(MainPanel):
    def __init__(self, root, frame, onLoad):
        MainPanel.__init__(self, root, frame, "Regula Falsi", onLoad)

        Label(self.frame, text="Valor para xa:").grid(row=1, column=1)
        self.xa_entry = Entry(self.frame, relief="raised")
        self.xa_entry.grid(row=1,column=2,columnspan=3)

        Label(self.frame, text="Valor para xb:").grid(row=2, column=1)
        self.xb_entry = Entry(self.frame, relief="raised")
        self.xb_entry.grid(row=2, column=2,columnspan=3)

        Label(self.frame, text="Tolerancia:").grid(row=3, column=1)
        self.tol_entry = Entry(self.frame, relief="raised")
        self.tol_entry.grid(row=3, column=2, columnspan=3)

    def calc_init(self, params):
        fn, directory = params

        xa = float(self.xa_entry.get())
        xb = float(self.xb_entry.get())
        tol = float(self.tol_entry.get())

        self.method_calc = RegulaFalsiMethod(fn, xa, xb, tol)

        return "Regula Falsi", [LatexSection("math", "Ecuación", fn)] + (self.method_calc.to_info())

class NewtonPanel(MainPanel):
    def __init__(self, root, frame, onLoad):
        MainPanel.__init__(self, root, frame, "Newton en C", onLoad)

        Label(self.frame, text="Valor para z0:").grid(row=0, column=1)
        self.z0_entry = Entry(self.frame, relief="raised")
        self.z0_entry.grid(row=0,column=2,columnspan=3)

        Label(self.frame, text="Valor para n_max:").grid(row=1, column=1)
        self.nmax_entry = Entry(self.frame, relief="raised")
        self.nmax_entry.grid(row=1, column=2,columnspan=3)

        Label(self.frame, text="Tolerancia:").grid(row=3, column=1)
        self.tol_entry = Entry(self.frame, relief="raised")
        self.tol_entry.grid(row=3, column=2, columnspan=3)

    def calc_init(self, params):
        fn, directory = params

        z0 = complex(self.z0_entry.get())
        n_max = int(self.nmax_entry.get())
        tol = float(self.tol_entry.get())

        self.method_calc = NewtonMethod(fn, z0, n_max, tol, directory)

        return "Newton en C", [LatexSection("math", "Ecuación", fn)] + (self.method_calc.to_info())
