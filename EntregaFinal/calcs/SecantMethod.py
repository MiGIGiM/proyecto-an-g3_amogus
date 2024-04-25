from dataclasses import dataclass
import numpy as np
import pandas as pd

from calcs.Method import Method, MethodDetails
from data.classes import LatexSection

class SecantMethod(Method):
    def __init__(self, fn, xa, xb, tol):
        Method.__init__(self, fn)

        self.xa = xa
        self.xb = xb
        self.tol = tol

        self.keys = ["a","b","fa","fb","c","fc","err"]
        self.table_init(self.keys)

        self.calc()

    def Slope(self, x1, x2, f):
        if(x1 == x2):
            return 'Ingrese dos puntos distintos'
        else:
            m = (f(x2)-f(x1))/(x2-x1)
            return m

    def IntersectionX(self):
        m = self.Slope(self.xa, self.xb, self.fn)

        x = self.xa - (1/m)*self.fn(self.xa)
        return x

    def calc(self):
        try:
            i = 0
            tramo = self.abs_err(self.xa, self.xb)

            if(tramo <= self.tol):
                self.result = "no se puede encontrar raices para este intervalo"

            while not(tramo <= self.tol):
                i = i + 1
                c = self.IntersectionX()
                fc = self.fn(c)

                vals = [self.xa, self.xb, self.fn(self.xa), self.fn(self.xb), tramo, c, fc]
                self.table_filler(self.keys, vals)

                if(fc == 0):
                    self.result = c

                tramo = self.abs_err(c, self.xa)

                self.xb = self.xa
                self.xa = c

                self.result = c
                self.iterations = i
                self.error = tramo

        except ZeroDivisionError:
            self.result = "no se puede encontrar raices para este intervalo"

    def to_info(self):
        return [
            LatexSection("table", "Tabla de resultados", self.dataframe()),
            LatexSection("text", "Raíz", self.result),
            LatexSection("text", "Información adicional", f"Iteraciones: {self.iterations}, Error: {self.error}")
        ]
