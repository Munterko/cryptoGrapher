import PyInstaller
from datetime import datetime
import yfinance
import mplfinance

def safeInt(number, safeMinimum=1):
    try:
        r = int(number)
    except:
        r = safeMinimum
    return r

def getCryptoGraph(startDate, endDate, ticker):
    startDate = startDate.split('-')
    start_date = datetime(safeInt(startDate[0],2019), safeInt(startDate[1]), safeInt(startDate[2]))
    endDate = endDate.split('-')
    end_date = datetime(safeInt(endDate[0],2020), safeInt(endDate[1]), safeInt(endDate[2]))
    data = yfinance.download(f'{ticker}-USD', start=start_date, end=end_date)
    mplfinance.plot(data,type='candle',mav=(3,6,9),volume=True,show_nontrading=True)



while True:
    ticker = input('provide a ticker for the crypto you want graphed e.g. ETH, BTC, BNB  ')
    sdate = input('provide a start year or a date in YYYY-MM-DD or YYYY-MM format  ') +'--'
    edate = input('provide a end year or a date in YYYY-MM-DD or YYYY-MM format  ') +'--'
    getCryptoGraph(sdate, edate, ticker)
    
    wantMore = input('Want another graph? y/n  ')
    if str.lower(wantMore) == 'n':
        exit()
