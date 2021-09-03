from datetime import datetime
import yfinance
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import pandas as pd
from tkinter import *
matplotlib.use("TkAgg")


def safeInt(number, safeMinimum=1):
    try:
        r = int(number)
    except:
        r = safeMinimum
    return r

def  getCryptoGraph(frameName, ticker, startDate, endDate):   #, chartType= 'candle', tradVolume=True
    canvas = ""
    startDate = (str(startDate) + "---").split('-')
    endDate = (str(endDate) + "---").split('-')

    start_date = datetime(safeInt(startDate[0],2019), safeInt(startDate[1]), safeInt(startDate[2]))
    end_date = datetime(safeInt(endDate[0],2020), safeInt(endDate[1]), safeInt(endDate[2]))

    cryptoData = pd.DataFrame(yfinance.download(f'{ticker}-USD', start= start_date, end= end_date))

    f = Figure(figsize=(5,5), dpi=100)
    graph = f.add_subplot(111)
    graph.plot(cryptoData.loc[start_date:end_date, 'Close'])

    canvas = FigureCanvasTkAgg(f, frameName)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH,  expand=True)

    toolbar = NavigationToolbar2Tk(canvas, frameName)
    toolbar.update()
    canvas._tkcanvas.pack(side=TOP, fill=BOTH,  expand=True)


