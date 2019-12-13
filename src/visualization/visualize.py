import numpy as np
import pandas as pd
from plotly.basedatatypes import BaseFigure
from plotly.graph_objs import Candlestick
from plotly.graph_objs._figure import Figure
from plotly import tools
from plotly.offline import init_notebook_mode, iplot, iplot_mpl


def generate_candle_plot(train_dataset,test_dataset,date_split='2016-01-01',
                         colors = ['green','red','darkgreen','darkred']):
    date_split = pd.to_datetime(date_split)

    train_date = train_dataset.set_index('Date')
    test_date = test_dataset.set_index('Date')
    data = [
            Candlestick(x=train_date.index, open=train_date.Open, high=train_date.High, 
                        low=train_date.Low, close=train_date.Close, name='train',
                        increasing_line_color= colors[0], decreasing_line_color= colors[1]),
            Candlestick(x=test_date.index, open=test_date.Open, high=test_date.High, 
                        low=test_date.Low, close=test_date.Close, name='test',
                       increasing_line_color= colors[2], decreasing_line_color= colors[3])
        ]
    layout = {
             'title': 'Apple stocks price evolution',
             'shapes': [
                 {'x0': date_split, 'x1': date_split, 
                  'y0': 0, 'y1': 1, 
                  'xref': 'x', 'yref': 'paper', 
                  'line': {'color': 'rgb(0,0,0)', 'width': 1}}
             ],
            'annotations': [
                {'x': date_split, 'y': 1.0, 'xref': 'x', 'yref': 'paper', 'showarrow': False, 
                 'xanchor': 'left', 'text': ' test data'},
                {'x': date_split, 'y': 1.0, 'xref': 'x', 'yref': 'paper', 'showarrow': False, 
                 'xanchor': 'right', 'text': 'train data '}
            ]
        }
    figure = Figure(data=data, layout=layout)
    figure.show()
