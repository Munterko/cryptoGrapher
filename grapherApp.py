from tkinter import *   
from tkinter import ttk, messagebox
from dataGrabAndPlot import getCryptoGraph, safeInt


class cryptoGrapher:

    def __init__(self, master):
        self.label = ttk.Label(master, text = "crypthGrapher", background='dark blue', foreground='white').grid(column=2, row=1)
        self.label = ttk.Label(master, text= 'this is a GUI aplication that creates custom graphs of crypto prices. Dates should be provided either as a year or in a YYYY-MM-DD format', wraplength= 200, justify= CENTER).grid(column=2, row=2)
        ttk.Label(master, text="Ticker").grid(column= 1, row=3)
        self.ticker = ttk.Entry(master)
        self.ticker.grid(column= 1, row=4)
        ttk.Label(master, text="Beginning date").grid(column= 2, row=3)
        self.startDate = ttk.Entry(master)
        self.startDate.grid(column= 2, row=4)
        ttk.Label(master, text="End date").grid(column= 3, row=3)
        self.endDate = ttk.Entry(master)
        self.endDate.grid(column= 3, row=4)
        button = ttk.Button(master, text = 'App status', command=self.showMessage).grid(column=1, row=5)
        button = ttk.Button(master, text = 'Create graph', command= lambda: getCryptoGraph(self.startDate.get(),self.endDate.get(),self.ticker.get())).grid(column=2, row=5)
        quitButton = ttk.Button(master, text = 'Quit', command= master.destroy).grid(column= 3, row=5)

    def showMessage(self):
        messagebox.showinfo('App status', "version 0.1 - work in progress")


def main(): 
    root = Tk()
    app = cryptoGrapher(root)
    root.mainloop()


if __name__=="__main__":
    main()