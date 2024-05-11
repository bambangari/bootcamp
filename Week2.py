import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Get data CSV
df = pd.read_csv('HistoricalData.csv')
#Cek Info file
print(df.info())

# Calculate Moving Averages Close/Last and open
df["Close/Last"] = df["Close/Last"].str.replace('$'," ").astype(float)
df["Open"] = df["Open"].str.replace('$'," ").astype(float)
ma = df[['Date','Close/Last','Open']]
ma_r = ma.iloc[::-1] #reverse row

windows = ma_r['Close/Last'].expanding()
moving_average = windows.mean()
#print(moving_average.tolist())
ma_r['MV_close'] = moving_average.tolist()

windows = ma_r['Open'].expanding()
moving_average = windows.mean()
#print(moving_average.tolist())
ma_r['MV_open'] = moving_average.tolist()

print(ma_r)

#example plot https://github.com/KeithGalli/matplotlib_tutorial/blob/master/Matplotlib%20Tutorial.ipynb
plt.figure(figsize=(10,6))
plt.title('Moving Averages Apple Inc. Common Stock (AAPL)', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.plot(ma_r['Date'], ma_r['MV_open'], 'b.-', label='Open')
plt.plot(ma_r['Date'], ma_r['MV_close'], 'r.-', label='Close')

plt.xticks(ma_r['Date'][::2].tolist())
plt.tick_params(axis='x', labelrotation=30)

plt.xlabel('Date')
plt.ylabel('US Dollars')

plt.legend()
plt.show()

