from keras.models import load_model
import pandas as pd
import numpy as np
def bilstm(start,end,modol):
    print(modol)
    model = load_model('./model/'+modol)
    df = pd.read_csv("./csv-files/BTC-USD.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[df['Date'] >= start]
    df = df[df['Date'] <= end]
    df = df.reset_index(drop=True)
    date = pd.DataFrame(df[['Date']])
    indexes = df.index.values
    endindex = max(indexes)
    dc = pd.DataFrame(df[['Open', 'Close', 'High', 'Low']])
    predict = dc.iloc[endindex - 110:endindex - 10]
    date = date.iloc[endindex - 10:endindex]
    expecteddf = pd.DataFrame(df[['Date', 'Close']])
    expecteddf['Type'] = 'Observed'
    tm = [3667.54092308, 3671.81879714, 3769.26483999, 3557.91619642]
    ts = [3962.52179229, 3963.50740991, 4095.59464515, 3805.53750232]
    predict = (predict - tm) / ts
    predict = np.expand_dims(predict, axis = 0)
    pred = model.predict(predict)
    tmp = pred
    tmp = (tmp * ts[1]) + tm[1]
    dataframe = pd.DataFrame(tmp[0], columns=['Close'])
    dataframe1 = pd.concat([date.reset_index(drop=True), dataframe], axis=1)
    dataframe1['Type'] = 'Predicted'
    real = pd.concat([expecteddf, dataframe1]).reset_index(drop=True)
    return real


