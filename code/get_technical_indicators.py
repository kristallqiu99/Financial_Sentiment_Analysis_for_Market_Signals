import pandas as pd
import numpy as np
import talib

gme = pd.read_csv('../data/gme.csv')


def get_indicators(df):
    mom = talib.MOM(df.Close, timeperiod=10).to_numpy().reshape(len(df), 1)
    rsi = talib.RSI(df.Close, timeperiod=14).to_numpy().reshape(len(df), 1)
    natr = talib.NATR(df.High, df.Low, df.Close,
                      timeperiod=14).to_numpy().reshape(len(df), 1)
    cci = talib.CCI(df.High, df.Low, df.Close,
                    timeperiod=14).to_numpy().reshape(len(df), 1)
    obv = talib.OBV(df.Close, df.Volume).to_numpy().reshape(len(df), 1)
    adx = talib.ADX(df.High, df.Low, df.Close,
                    timeperiod=14).to_numpy().reshape(len(df), 1)
    aroondown, aroonup = talib.AROON(df.High, df.Low, timeperiod=14)
    aroondown = aroondown.to_numpy().reshape(len(df), 1)
    aroonup = aroonup.to_numpy().reshape(len(df), 1)

    return np.concatenate([mom, rsi, natr, cci, obv, adx], axis=1)


indicators = ['mom', 'rsi', 'natr', 'cci', 'obv', 'adx']
gme.loc[:, indicators] = get_indicators(gme)

gme['increase'] = (gme.Close > gme.Open).astype(int)

gme = gme.sort_values(['Date']).fillna(method='bfill')

gme.to_csv('../../data/csv/gme_indicators.csv', index=False)
