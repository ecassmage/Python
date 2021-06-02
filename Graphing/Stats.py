import tkinter as tk
Large_Font = ("Verdana", 12)
mediumFont = ('Verdana', 9)


class Statistics:
    """This is IMPORTANT CLASS and makes this super easy to do."""
    def __init__(self):
        container = tk.Frame(width=1000, height=1000, bg='orange')
        container.pack()
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage,):  # New Pages are Added Here.
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label = tk.Label(self, text="StartPage", font=Large_Font)
        self.listBoxLabel = tk.Label(self, text='Highest Valued Stocks', font=mediumFont)
        self.listBox = tk.Listbox(self, bg='orange', width=150, height=40)
        # label.grid(row=0, column=1)
        self.listBox.grid(row=1, column=1)
        self.listBoxLabel.grid(row=1, column=0)


def adventOfNewList(bestCompanies, GUI):
    GUI.frames[StartPage].listBox.delete(0, 'end')
    for num, company in enumerate(bestCompanies):
        GUI.frames[StartPage].listBox.insert(
            "end",
            f"{num + 1}. "
            f"Company Name: {company.name}, \t\t\t\t"
            f"Market Value: {company.marketCap:.2f}, "
            f"Shares: {company.shares:.0f}, "
            f"Share Price: {company.currentValue:.2f}, "
            f"Company Age: {company.yearCurrent - company.yearCreated}, "
            f"Color: {company.color}"
        )
    return


def sort_values(companies, GUI):
    marketCapsTemp = {}
    marketCaps = {}
    for company in companies:
        if company.operational:
            marketCapsTemp.update({company.marketCap: company})
    bestMarkets = sorted(marketCapsTemp)
    for marketCap in reversed(bestMarkets):
        company = marketCapsTemp[marketCap]
        marketCaps.update({company: marketCap})
    del marketCapsTemp, bestMarkets
    adventOfNewList(marketCaps, GUI)


def main():
    a = Statistics()
    return a


if __name__ == "__main__":
    main()
