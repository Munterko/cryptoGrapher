from tkinter import *
from tkinter import ttk, messagebox
from dataGrabAndPlot import getCryptoGraph


class cryptoGrapher:
    def __init__(self, master):
        master.title('cryptoGrapher')
        #master.iconbitmap('/') #set bugRepWindow icon
        master.geometry(f'{master.winfo_screenwidth()}x{master.winfo_screenheight()}')
        master.minsize(1250,200)

        head = ttk.Frame(master)
        body = ttk.Frame(master, relief=SUNKEN)
        graph = ttk.Frame(master, relief=SUNKEN)
        foot = ttk.Frame(master, relief=RIDGE, height=200, width=100)
        # graphTools = ttk.Frame(master)
        
        head.place(relx=0, y=0, relwidth=1, height=35)
        body.place(relx=0,y=35, relwidth=1, height=60)
        graph.place(relx=0, y=95, relwidth=1, relheight=1, height=-190)
        foot.place(relx=0, rely=1, y=-95, relwidth=1, height=95)
        

        ttk.Label(head, text = 'This is a GUI aplication that creates custom graphs of crypto prices. Dates should be provided either as a year or in a YYYY-MM-DD format.').pack(side = LEFT, anchor=W, padx=20, expand=True)#f'{self.ticker} from {self.startDate} to {self.endDate}').pack() 
        self.fscreen = BooleanVar()
        ttk.Button(head, text = 'Fullscreen mode', command= lambda: self.fullscreenMode(master)).pack(side = RIGHT, anchor=E, padx=20, expand=False)
        ttk.Button(head, text = 'Report a bug', command=lambda: self.bugRep(master)). pack(side = RIGHT, anchor=E, expand=False)


        # Variable controlling layout details of all elements in the Body Frame
        lBodyLayout = {'side':LEFT, 'padx':20}
        rBodyLayout = {'side':RIGHT, 'padx':20, 'ipadx': 10, 'ipady':10}


        tickerField = Frame(body)
        tickerField.pack(lBodyLayout)
        ttk.Label(tickerField, text="Ticker").pack()
        self.ticker = StringVar()
        ttk.Entry(tickerField, textvariable= self.ticker, justify= CENTER).pack()
        self.ticker.set('ETH')      #Displays ETH as an default value in the entry field

        startDateField = Frame(body)
        startDateField.pack(lBodyLayout)
        ttk.Label(startDateField, text="Beginning date", justify= CENTER).pack()
        self.startDate = ttk.Entry(startDateField)
        self.startDate.pack()
        
        endDateField = Frame(body)
        endDateField.pack(lBodyLayout)
        ttk.Label(endDateField, text="End date", justify= CENTER).pack()
        self.endDate = ttk.Entry(endDateField)
        self.endDate.pack()
        
        dropDownField = Frame(body)
        dropDownField.pack(lBodyLayout)
        ttk.Label(dropDownField, text="Char type").pack()
        self.charType = StringVar()
        ttk.Combobox(dropDownField, values=['line', 'candle', 'ohlc', 'pnf', 'renko'], validate= 'all', textvariable= self.charType).pack()
        self.charType.set('line')

        self.volume = BooleanVar()
        ttk.Checkbutton(body, text="Trading volume", variable=self.volume, onvalue=True, offvalue=False).pack(lBodyLayout)
        self.volume.set(True)


        ttk.Button(body, text = 'Quit', command= master.destroy).pack(rBodyLayout)
        ttk.Button(body, text = 'App status', command= lambda: messagebox.showinfo('App status', "version 0.3 - Ugly layout, but a layout!")).pack(rBodyLayout)
        ttk.Button(body, text = 'Create graph', command= lambda: getCryptoGraph(self.ticker.get(), self.startDate.get(),self.endDate.get(), tradVolume= self.volume.get(), chartType= self.charType.get() )).pack(rBodyLayout)
        
        ttk.Label(graph, text= 'Graph placeholder').pack(side=TOP)
        ttk.Label(graph, text= 'Graph placeholder').pack(side=BOTTOM)
        ttk.Label(foot, text= 'Foot placeholder').pack(side=TOP)
        ttk.Label(foot, text= 'Foot placeholder').pack(side=BOTTOM)

    def fullscreenMode(self, master):
        pass
    

    def bugRep(self, master):
        bugRepWindow = Toplevel(master)
        bugRepWindow.title('Report a bug')
        bugRepWindow.geometry('350x250')
        ttk.Label(bugRepWindow, text= 'Not jet implemented').pack(anchor=CENTER, pady=75)
        ttk.Button(bugRepWindow, text= 'Close', command= bugRepWindow.destroy).pack(anchor=SE, side=BOTTOM, padx=5, pady=10)
        '''
        To be written
        '''

        
    def validate():
        #Validates user inputs like dates or char type and produces a message box if there is a problem
        pass



def main(): 
    root = Tk()
    app = cryptoGrapher(root)
    root.mainloop()


if __name__=="__main__":
    main()