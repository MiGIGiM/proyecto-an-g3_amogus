from tkinter import *

from data.classes import MethodInfo

class SidePanel:
    secant = MethodInfo("Secante", "secante")
    muller = MethodInfo("Muller", "muller")
    newton = MethodInfo("Newton en C", "newton")
    regulaFalsi = MethodInfo("Falsa posicion (Regula Falsi)", "regula-falsi")

    def __init__(self, root, frame, invoker) -> None:
        self.root = root
        self.frame = frame

        # Label for side panel
        Label(self.frame, text="Metodos").grid(row=0, column=0)

        # Wrapping buttons
        Button(
            self.frame,
            text=self.secant.disp,
            relief="raised",
            command=lambda: invoker(self.secant)
        ).grid(row=1, column=0, sticky="nsew")

        Button(
            self.frame,
            text=self.muller.disp,
            relief="raised",
            command=lambda: invoker(self.muller)
        ).grid(row=2, column=0, sticky="nsew")

        Button(
            self.frame,
            text=self.newton.disp,
            relief="raised",
            command=lambda: invoker(self.newton)
        ).grid(row=3, column=0, sticky="nsew")

        Button(
            self.frame,
            text=self.regulaFalsi.disp,
            relief="raised",
            command=lambda: invoker(self.regulaFalsi)
        ).grid(row=4, column=0, sticky="nsew")
