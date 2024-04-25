from email.policy import strict
from turtle import width
from pandas import DataFrame, set_option
from pylatex import Document, Section, Subsection, Tabular, Figure, Math
from sympy import latex, sec, symbols
from data.classes import LatexSection
from time import time
from utils.Fs import remove_file


class PdfTools:
    def __init__(self, sections: "list[LatexSection]", main_title: str, location: str) -> None:
        geometry_options = { "tmargin": "1in", "lmargin": "1in" }
        self.doc = Document(geometry_options=geometry_options)

        with self.doc.create(Section(main_title)):
            print(sections)
            for section in sections:
                mode, title, data = section
                if mode == "text":
                    self.write_subsection(title, lambda: self.write_text(data))
                if mode == "math":
                    self.write_subsection(title, lambda: self.write_math(data))
                elif mode == "graph":
                    self.write_subsection(title, lambda: self.write_graph(data))
                elif mode == "plot":
                    self.write_subsection(title, lambda: self.write_plot(data))
                elif mode == "table":
                    self.write_subsection(title, lambda: self.write_table(data))

        self.doc.generate_pdf(filepath=location, clean_tex=True, compiler="pdflatex")

    def export_table(self, dataframe: DataFrame, filename: str):
        remove_file(f"{filename}.csv")
        remove_file(f"{filename}.html")

        dataframe.to_csv(f"{filename}.csv")
        dataframe.to_html(f"{filename}.html")

    def write_text(self, text: str):
        self.doc.append(text)

    def write_math(self, text: str):
        with self.doc.create(Math(inline=False, escape=False)) as math:
            x = symbols('x')
            eq = latex(eval(text))

            print(eq)
            math.append(eq)

    def write_subsection(self, name, command):
        with self.doc.create(Subsection(name)):
            command()

    def write_table(self, df: DataFrame):
        width = 10

        with self.doc.create(Tabular('Table', width=width, booktabs=True)) as table:
            table.add_hline()
            table.add_row(list(df.columns), strict=False)
            table.add_hline()

            for row in df.index:
                table.add_row(list(df.loc[row,:]), strict=False)
            
            table.add_hline()

    def write_plot(self, plot_filename):
        with self.doc.create(Figure(position="h!")) as plot:
            plot.add_image(plot_filename, width="400px")

    def write_graph(self, graph_filename):
        with self.doc.create(Figure(position="h!")) as graph:
            graph.add_image(graph_filename, width="400px")
