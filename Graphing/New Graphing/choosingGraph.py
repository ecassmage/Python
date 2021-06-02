import tkinter as tk


class ControlPanel:
    def __init__(self):
        self.tk = tk.Tk()
        self.tkFrame = tk.Frame()
        self.tkFrame.pack()
        self.menu = tk.Menu(self.tkFrame)

        self.menuReal = tk.Menu(self.menu, tearoff=0)
        self.menuReal.add_command(label="New", command=None)
        self.menuReal.add_command(label="Open", command=None)
        self.menuReal.add_command(label="Save", command=None)
        self.menuReal.add_command(label="Save as...", command=None)
        self.menuReal.add_command(label="Close", command=None)
        self.menu.add_cascade(label="Real People", menu=self.menuReal)
        self.tk.config(menu=self.menu)
        # self.graphs = {}
        # self.Pages = [
        #
        # ]
        # for newGraph in self.Pages:
        #     graph = newGraph(self.tkFrame, self)
        #     self.graphs[newGraph] = graph
        #     graph.grid(row=0, column=0, sticky='nsew')
        # self.showFrame()


a = ControlPanel()
a.tkFrame.mainloop()
