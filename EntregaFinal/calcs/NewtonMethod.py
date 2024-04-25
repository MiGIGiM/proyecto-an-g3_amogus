import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cmath

from calcs.Method import Method, MethodDetails
from data.classes import LatexSection

class NewtonMethod(Method):
    # Class constructor
    def __init__(self, fn, z0, n_max, tol, dir):
        # Parent class constructor
        Method.__init__(self, fn)
        self.z0 = z0

        x = sp.symbols('x')
        self.dir = dir

        # Creates a lambdify version of diff of fn, if not lambdify sympy crashes when evaluating complex
        self.fprime = sp.lambdify(x, self.fn(x).diff(x))

        # Keys for dataframe
        self.keys = [
            "z_n", "f(z_n)", "df(fz_n)", "z_(n+1)", "Error"
        ]

        # Inits table with the keys given (see parent method)
        self.table_init(self.keys)

        self.n_max = n_max
        self.tol = tol

        self.fractal = None
        self.plot = None

        self.calc()

    def validate_newton_method(self, fprime, z0):
        if fprime(z0) == 0:
            return False, 0

    def calc(self):
        i = 0
        z0 = self.z0

        if not self.validate_newton_method(self.fprime, z0):
            while True:
                f_z0 = self.fn(z0)
                df_z0 = self.fprime(z0)
                z = z0 - (f_z0 / df_z0)
                df_z = self.fprime(z)
                error = self.abs_err(z0, z)

                vals = [z0, f_z0, df_z0, z, error]
                self.table_filler(self.keys, vals)

                if error < self.tol or i + 1 == self.n_max or df_z == 0:
                    break

                z0 = z
                i += 1
                global root
                root = z0

        self.graph = self.plot_fractal(self.fn, self.fprime, 300, self.tol)
        self.plot = self.plot_polar()

        self.result = root
        self.iterations = i
        self.error = error

    def newton_fractal(self, z0, f, frime, tol):
        z = z0
        for i in range(500):
            dz = f(z) / frime(z)
            if abs(dz) < tol:
                return z
            z -= dz
        return False

    def plot_fractal(self, f, fprime, n, tol, domain=(-10, 10, -10, 10)):
        roots = []
        m = np.zeros((n, n))

        def get_root_index(roots, r):

            try:
                return np.where(np.isclose(roots, r, atol=tol))[0][0]
            except IndexError:
                roots.append(r)
                return len(roots) - 1

        xmin, xmax, ymin, ymax = domain
        for ix, x in enumerate(np.linspace(xmin, xmax, n)):
            for iy, y in enumerate(np.linspace(ymin, ymax, n)):
                z0 = x + y * 1j
                r = self.newton_fractal(z0, f, fprime, tol)
                if r:
                    ir = get_root_index(roots, r)
                    m[iy, ix] = ir

        plt.imshow(m, cmap="viridis", origin='lower')
        plt.axis('off')
        plt.savefig(f"{self.dir}_graph.png", bbox_inches='tight')

        return f"{self.dir}_graph.png"

    def plot_polar(self):
        magnitude, angle = cmath.polar(100)

        plt.figure()
        plt.polar([0, angle], [0, magnitude], marker='o', color='r')
        plt.savefig(f"{self.dir}_polar.png", bbox_inches='tight')

        return f"{self.dir}_polar.png"

    def to_info(self):
        return [
            LatexSection("table", "Tabla de resultados", self.dataframe()),
            LatexSection("text", "Raíz", self.result),
            LatexSection("text", "Información adicional", f"Iteraciones: {self.iterations}, Error: {self.error}"),
            LatexSection("plot", "Fractal", self.graph),
            LatexSection("plot", "Gráfica", self.plot),
        ]
