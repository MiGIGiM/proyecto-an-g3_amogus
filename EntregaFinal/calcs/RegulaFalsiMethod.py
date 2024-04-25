from dataclasses import dataclass
import numpy as np
import pandas as pd
from sympy import Interval, calculus, symbols

from calcs.Method import Method, MethodDetails
from data.classes import LatexSection

class RegulaFalsiMethod(Method):
    def __init__(self, fn, xa, xb, tol):
        Method.__init__(self, fn)

        self.xa = xa
        self.xb = xb
        self.tol = tol

        self.keys = ["a", "b", "fa", "fb", "c", "fc", "Error"]
        self.table_init(self.keys)

        self.can_calculate((xa, xb))

        self.calc()

    def can_calculate(self, params):
        x = symbols('x')
        a, b = params
        
        interval = Interval(a,b)
        dom = calculus.util.continuous_domain(self.fn(x), x, interval)
        if dom == interval:
            return

        raise Exception("No es posible calcular en ese rango")

    def aprox(self, p1, p2):
        fp1 = self.fn(p1).real
        fp2 = self.fn(p2).real

        c = p2 - fp2*(p1-p2)/(fp1-fp2)
        return c

    def calc(self):
        iterator = 0

        section = self.abs_err(self.xa, self.xb)

        if(section <= self.tol):
            self.result = "no se puede encontrar raices para este intervalo"

        while not(section <= self.tol):
            iterator = iterator + 1
            c = self.aprox(self.xa, self.xb)
            fc = self.fn(c)

            fa = self.fn(self.xa)
            fb = self.fn(self.xb)

            if isinstance(fa, complex) or isinstance(fb, complex):
                raise Exception("Python no es capaz de trabajar esa expresion sin usar numeros imaginarios")

            vals = [self.xa, self.xb, fa, fb, section, c, fc]
            self.table_filler(self.keys, vals)

            if(fc == 0):
                return c

            cambia = np.sign(self.fn(self.xa))*np.sign(fc)

            if (cambia > 0):
                section = self.abs_err(c, self.xa)
                self.xa = c
            else:
                section = self.abs_err(self.xb, c)
                self.xb = c
        
        self.result = c
        self.iterations = iterator
        self.error = section

    def to_info(self):
        return [
            LatexSection("table", "Tabla de resultados", self.dataframe()),
            LatexSection("text", "Raíz", self.result),
            LatexSection("text", "Información adicional", f"Iteraciones: {self.iterations}, Error: {self.error}")
        ]
