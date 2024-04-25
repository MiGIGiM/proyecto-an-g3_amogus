import math
import pandas as pd

from calcs.Method import Method, MethodDetails
from data.classes import LatexSection

class MullerMethod(Method):
    def __init__(self, fn, x0, x1, x2, tol):
        Method.__init__(self, fn)
        
        self.x0 = x0
        self.x1 = x1
        self.x2 = x2
        
        self.tol = tol

        self.keys = [ "x_a", "x_b", "x_c", "a", "b", "c", "x_r", "Error" ]
        self.table_init(self.keys)

        self.calc()

    def calc(self):
        res = 0
        iterations = 0

        while (True):
            iterations = iterations + 1
            
            f1 = self.fn(self.x0)
            f2 = self.fn(self.x1)
            f3 = self.fn(self.x2)

            d1 = f1 - f3
            d2 = f2 - f3
            
            h1 = self.x0 - self.x2
            h2 = self.x1 - self.x2
            
            a0 = f3
            a1 = (((d2 * pow(h1, 2)) - (d1 * pow(h2, 2))) / ((h1 * h2) * (h1 - h2)))
            a2 = (((d1 * h2) - (d2 * h1)) / ((h1 * h2) * (h1 - h2))) 

            x = ((-2 * a0) / (a1 + abs(math.sqrt(a1 * a1 - 4 * a0 * a2))))
            y = ((-2 * a0) / (a1 - abs(math.sqrt(a1 * a1 - 4 * a0 * a2))))

            # Tomando raiz mas cercana x0 x_2
            if (x >= y):
                res = x + self.x2
            else:
                res = y + self.x2
                
            # Calculando error
            err = self.abs_err(res, self.x2)

            # Guardando datos en las listas
            vals = [self.x0, self.x1, self.x2, a0, a1, a2, res, err]
            self.table_filler(self.keys, vals)

            self.x0 = self.x1
            self.x1 = self.x2
            self.x2 = res
            self.error = err
            self.iterations = iterations

            if (err <= self.tol):
                self.result = res
                break

    def to_info(self):
        return [
            LatexSection("table", "Tabla de resultados", self.dataframe()),
            LatexSection("text", "Raíz", self.result),
            LatexSection("text", "Información adicional", f"Iteraciones: {self.iterations}, Error: {self.error}")
        ]

