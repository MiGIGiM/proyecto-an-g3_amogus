from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from panels.MainPanel import MullerPanel, NewtonPanel, RegulaFalsiPanel, SecantPanel

from panels.SidePanel import SidePanel
from panels.TopPanel import TopPanel

from data.classes import Dims, MethodInfo
from utils.PdfTools import PdfTools

class MainWindow:
    # Initialized attrs for window dimensions
    height = 400
    width = 600

    def __init__(self) -> None:
        self.root = Tk()
        
        # Creating grid for main window
        for i in range(6):
            self.root.columnconfigure(i, weight=1, minsize=self.width / 6)
            self.root.rowconfigure(i, weight=1, minsize=self.height / 6)

        # Configuring title
        self.root.wm_title("Raices de funciones irracionales")
        
        # Init main frame
        self.mainFrame = None

        # Config panels
        self.sidepanel_init()
        self.toppanel_init()
        self.mainpanel_lifecycle(MethodInfo("Secante", "secante"))
        
    def start(self):
        self.root.mainloop()

    def sidepanel_init(self):
        # Side Panel data
        """
            - First we set dimensions for the side panel (left)
            - Then we instantiate a frame that'll containt the SidePanel obj
            - We configure it as an unique column with 5 rows
            - We grid that item in it's parent (window or root)
        """
        sideDims = Dims(self.width / 6, self.height)
        self.sideFrame = Frame(self.root, height=sideDims.height, width=sideDims.width)
        
        self.sideFrame.columnconfigure(0, weight=1, minsize=sideDims.width)
        
        for i in range (5):
            self.sideFrame.rowconfigure(i, weight=1, minsize=self.height / 5)

        self.sideFrame.grid(row=0, column=0, rowspan=6, columnspan=1)

        # Side Panel instantiation
        self.sidePanel = SidePanel(self.root, self.sideFrame, self.mainpanel_lifecycle)

    def toppanel_init(self):
        # Top Panel data

        # As we did with side panel, this one will go with 2 rows and all the remaining cols
        topDims = Dims((self.width / 6 ) * 5, (self.height / 6) * 2)
        self.topFrame = Frame(self.root)

        # Top Panel has 3 rows and 6 cols
        for i in range(3):
            self.topFrame.rowconfigure(i, weight=1, minsize=topDims.height / 3)

        for i in range(6):
            self.topFrame.columnconfigure(i, weight=1, minsize=topDims.width / 6)

        self.topFrame.grid(row=0, column=1, sticky="nsew", rowspan=2, columnspan=5)

        # Top Panel instantiation
        self.topPanel = TopPanel(self.root, self.topFrame, "NO-DEFAULT", self.method_invoker)

    def mainpanel_lifecycle(self, method):
        # Main Panel data

        # Frame will be destroyed every time it has already been created
        if self.mainFrame is not None:
            self.mainFrame.destroy()

        # As we did with side panel, this one will go with two rows and all the remaining rows and cols
        mainDims = Dims((self.width / 6 ) * 5, (self.height / 6) * 4)
        self.mainFrame = Frame(self.root)

        for i in range(5):
            self.mainFrame.rowconfigure(i, weight=1, minsize=mainDims.height / 5)

        for i in range(6):
            self.mainFrame.columnconfigure(i, weight=1, minsize=mainDims.width / 6)

        self.mainFrame.grid(row=2, column=1, sticky="nsew", rowspan=4, columnspan=5)

        # Top Panel instantiation
        self.mainPanel = self.mainpanel_invoker(method)

    def mainpanel_invoker(self, method):
        # Init an object for the new invoked panel
        if method.slug == "muller":
            return MullerPanel(self.root, self.mainFrame, lambda: self.topPanel.modify_title(method.disp))
        if method.slug == "regula-falsi":
            return RegulaFalsiPanel(self.root, self.mainFrame, lambda: self.topPanel.modify_title(method.disp))
        if method.slug == "newton":
            return NewtonPanel(self.root, self.mainFrame, lambda: self.topPanel.modify_title(method.disp))
        else:
            return SecantPanel(self.root, self.mainFrame, lambda: self.topPanel.modify_title(method.disp))
    
    def method_invoker(self, fn_string):
    
        location = None

        while location is None:
            location = filedialog.asksaveasfilename()

        title, info = self.mainPanel.calc_init((fn_string, location))

        PdfTools(info, title, location)
        
        