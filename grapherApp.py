from tkinter import *   
from tkinter import ttk, messagebox
from dataGrabAndPlot import getCryptoGraph


class cryptoGrapher:
    def __init__(self, master):
        '''
        Date inputs to be changed for more practical input object types such as LabeledScale or Spinbox.
        '''

        #Title and description
        ttk.Label(master, text = "crypthGrapher", background='dark blue', foreground='white').grid(column=2, row=1)
        ttk.Label(master, text= 'This is a GUI aplication that creates custom graphs of crypto prices. Dates should be provided either as a year or in a YYYY-MM-DD format.', wraplength= 200, justify= CENTER).grid(column=2, row=2)
        
        #Ticker text field
        ttk.Label(master, text="Ticker").grid(column= 1, row=3)
        self.ticker = StringVar()
        ttk.Entry(master, textvariable= self.ticker, justify= CENTER).grid(column= 1, row=4)
        self.ticker.set('ETH')      #Displays ETH as an default value in the entry field

        #Start-date text field
        ttk.Label(master, text="Beginning date", justify= CENTER).grid(column= 2, row=3)
        self.startDate = ttk.Entry(master)
        self.startDate.grid(column= 2, row=4)
        
        #End-date text field
        ttk.Label(master, text="End date", justify= CENTER).grid(column= 3, row=3)
        self.endDate = ttk.Entry(master)
        self.endDate.grid(column= 3, row=4)
        
        #Trading-volume check button
        self.volume = BooleanVar()
        ttk.Checkbutton(master, text="Trading volume", variable=self.volume, onvalue=True, offvalue=False).grid(column=2, row=5)
        self.volume.set(True)

        #Drop-down char type selection
        ttk.Label(master, text="Char type").grid(column= 1, row= 5)
        self.charType = StringVar()
        ttk.Combobox(master, values=['line', 'candle', 'ohlc', 'pnf', 'renko'], validate= 'all', textvariable= self.charType).grid(column= 1, row= 6)
        self.charType.set('line')

        # #Debugging button
        # self.check = ttk.Button(master, text='debug', command= lambda: messagebox.showinfo("status", self.ticker.get())).grid(column=3, row=5)
    
        #Buttons in the last row
        ttk.Button(master, text = 'App status', command= lambda: messagebox.showinfo('App status', "version 0.2 - those graphs will get fancy one day!")).grid(column=1, row=7)
        ttk.Button(master, text = 'Create graph', command= lambda: getCryptoGraph(self.ticker.get(), self.startDate.get(),self.endDate.get(), tradVolume= self.volume.get(), chartType= self.charType.get() )).grid(column=2, row=7)
        ttk.Button(master, text = 'Quit', command= master.destroy).grid(column= 3, row=7)
        

    def validate():
        #Validates user inputs like dates or char type and produces a message box if there is a problem
        pass



def main(): 
    root = Tk()
    app = cryptoGrapher(root)
    root.mainloop()


if __name__=="__main__":
    main()