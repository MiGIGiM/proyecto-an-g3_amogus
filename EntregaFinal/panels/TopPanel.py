from tkinter import *

class TopPanel:
    def __init__(self, root, frame, title, fn_invoker) -> None:
        self.root = root
        self.frame = frame

        self.title = StringVar()
        self.title.set(title)

        self.label = Label(self.frame, textvariable=self.title).grid(row=0, column=2, columnspan=2, sticky="n")
        
        Label(self.frame, text="Ecuacion:").grid(row=1, column=2, columnspan=2)

        self.fn_entry = Entry(self.frame, relief="raised")
        self.fn_entry.grid(row=2, column=1, columnspan=3)
        
        self.reportGenerator = Button(
            self.frame,
            text="Calcular",
            relief="raised",
            command= lambda: fn_invoker(self.fn_entry.get())
        ).grid(row=2, column=4)

    def modify_title(self, newTitle):
        self.title.set(newTitle)
