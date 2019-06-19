import datetime
from yahoo_fin import stock_info
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd 
import numpy as np
from plotkey import plotly_var

plotly.tools.set_credentials_file(username=plotly_var.username, api_key=plotly_var.key)

now =  datetime.datetime.now()

today_date = now.strftime("%d/%m/%Y")
few_days = stock_info.get_data('amd' , start_date = '01/05/2018')
price_list = few_days['close'].tolist() 
index = few_days.index.tolist()

trace0 = go.Scatter(
    x = index,
    y = price_list,
    name = 'AMD close price',
    line = dict(
        color = ('rgb(0, 0, 24)'),
        width = 2)
)

trace1 = go.Scatter(
    x = index,
    y = few_days['high'].tolist(),
    name = 'AMD close price',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 2,
        dash = 'dash'
        )
)

trace2 = go.Scatter(
    x = index,
    y = few_days['low'].tolist(),
    name = 'AMD close price',
    line = dict(
        color = ('rgb(20, 225, 24)'),
        width = 2,
        dash = 'dash')
)

data = [trace0, trace1, trace2]
layout = dict(title = 'Stock price',
              xaxis = dict(title = 'Date'),
              yaxis = dict(title = 'Price USD'),
              )

fig = dict(data=data, layout=layout)

plotly.offline.plot(fig, filename='styled-line')
