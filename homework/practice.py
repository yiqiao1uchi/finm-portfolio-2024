import pandas as pd
df = pd.read_csv('')

#EDA
df.duplicated(['Date', 'Ticker']).sum()
df.drop_duplicates(['Date', 'Ticker'], keep='last')
df['Date'] = pd.to_datetime(df['Date'])

df['Ticker'].unique()
df.loc[df['Position']>0, 'Position'].describe()
(df['Position']>0).mean()

import matplotlib.pyplot as plt
plt.figure(figsize = (12, 6))
t1 = df[df['Ticker'] == 'Ticker1']
plt.plot(t1['Date'], t1['Position'], label='T1')
plt.title('')
plt.xlabel('')
plt.legend()
plt.show()

#Exposure Analysis
import numpy as np
daily = (df.groupby('Date').agg(
    long = ('Position', lambda p: p[p>0].sum()),
    short = ('Position', lambda p: -p[p<0].sum())
)
)
daily['net'] = daily['long'] - daily['short']
daily['gross'] = daily['long'] + daily['short']
daily['hedge ratio'] = daily['net'].abs()/daily['gross'].replace([np.nan, np.inf], 0)

#plot net and gross exposure
plt.figure(figsize = (12, 6))
plt.plot(daily.index,daily['net'], label='net')
plt.plot(daily.index, daily['gross_exposure'], label='gross')
plt.title('')
plt.xlabel('')
plt.legend()
plt.show()

#hedge ratio histogram
plt.hist(daily['hedge ratio'], bins = 30, color = '', edgecolor='')
plt.title("Distribution of Daily Hedge Ratios (|Net|/Gross)")
plt.xlabel("Hedge Ratio"); plt.ylabel("Frequency")
plt.tight_layout(); plt.show()

#neutrality
(daily['hedge ratio'] < 0.02).sum()
roll_hedge = daily['hedge ratio'].rolling(5).mean()
(roll_hedge < 0.02).sum()

# Fee analysis
df['fee'] = df['Position']*df['Position'].abs()
daily_fee = df.groupby('Date')['fee'].sum()
cum_fee = daily_fee.cumsum()

plt.plot(daily_fee.index, daily_fee.values, label='daily fee')
plt.plot(cum_fee.index, cum_fee.values, label='cum fee')
...
plt.legend()

df.groupby('Ticker')['fee'].sum().sort_values(ascending= False).rename('Ticker total fee')
# max share daily
df.loc[df['fee'].idmax(), ['Ticker', 'Position']]


import pandas as pd

df  = pd.read_csv('')

# EDA 
df.duplicated(['Date', 'Ticker']).sum()
df.drop_duplicates(['Date', 'Ticker'], keep = 'last')

df['Date'] = pd.to_Datetime(df['Date'])
df['Ticker'].unique()
df.loc[df['Poition']>0, 'Position'].describe()

import matplotlib.pyplot as plt
olt.figure(figsize =(12,6))
t1 = df[df['Ticker'] =='Ticker1']
ply.plot(t1)

import numpy as np
daily = (df.groupby['Date'].agg(
    long = ('Position', lambda p: p[p>0].sum()),
    short 
)

)