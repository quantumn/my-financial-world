import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
from matplotlib.finance import quotes_historical_yahoo
stocks = ('IBM', 'GE', 'WMT', 'C', 'AAPL')
begdate=(2013,1,1)
enddate=(2013,11,30)
def ret_vol(ticker):
    x = quotes_historical_yahoo(ticker,begdate,enddate,asobject=True,adjusted=True)
    logret = np.log(x.aclose[1:]/x.aclose[:-1])
    return(np.exp(sum(logret))-1,np.std(logret))
ret=[];vol=[]
for ticker in stocks:
    r,v=ret_vol(ticker)
    ret.append(r)
    vol.append(v*np.sqrt(252))
    
labels = ['{0}'.format(i) for i in stocks]
plt.xlabel('Volatility (annualized)')
plt.ylabel('Annual return')
plt.title('Return vs. volatility')
plt.subplots_adjust(bottom = 0.1)
color=np.array([ 0.18, 0.96, 0.75, 0.3, 0.9])
plt.scatter(vol, ret, marker = 'o', c=color,s = 1000,cmap=plt.get_cmap('Spectral'))
for label, x, y in zip(labels, vol, ret):
    plt.annotate(label,xy=(x,y),xytext=(-20,20),textcoords='offsetpoints',ha = 'right', va = 'bottom',bbox = dict(boxstyle = 'round,pad=0.5',
    fc = 'yellow', alpha = 0.5),arrowprops = dict(arrowstyle = '->',connectionstyle = 'arc3,rad=0'))
plt.show()