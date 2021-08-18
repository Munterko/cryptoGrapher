from datetime import datetime
import yfinance
import mplfinance

def safeInt(number, safeMinimum=1):
    try:
        r = int(number)
    except:
        r = safeMinimum
    return r

def getCryptoGraph(ticker, startDate, endDate, chartType= 'candle', tradVolume=True):
    startDate = (str(startDate) + "---").split('-')
    endDate = (str(endDate) + "---").split('-')

    start_date = datetime(safeInt(startDate[0],2019), safeInt(startDate[1]), safeInt(startDate[2]))
    end_date = datetime(safeInt(endDate[0],2020), safeInt(endDate[1]), safeInt(endDate[2]))

    data = yfinance.download(f'{ticker}-USD', start= start_date, end= end_date)
    mplfinance.plot(data, type= chartType, mav= (3,6,9),volume= tradVolume, show_nontrading= True)



