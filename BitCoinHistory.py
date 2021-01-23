import requests
import pandas as pd
import matplotlib.pyplot as plt
from PIL import  Image

url = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2017-09-01&end=2020-09-25"
result = requests.get(url)
print(result.json())
myDict = result.json();
print(myDict)

dates = myDict["bpi"].keys()
prices = myDict["bpi"].values()

df = pd.DataFrame({'dates': dates, 'prices': prices}, columns={'dates', 'prices'})
print(df)
df['dates'] = pd.to_datetime(df['dates'], format='%Y-%m-%d')


plt.plot(df['dates'],df['prices'])
plt.title('Bitcoin history')
plt.xlabel('Time period')
plt.ylabel("Value of BitCoin in USD")
plt.show()







