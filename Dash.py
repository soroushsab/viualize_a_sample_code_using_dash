#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader.data as web
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(children=[
    html.Div(children=[
        html.Meta(charSet="utf-8"),
        html.Meta(name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"),
        html.Meta(httpEquiv="x-ua-compatible" content="ie=edge"),
        html.Title(title='Soroush Dash'),
    ]),

    html.Div(children=[],className="row")
    
    html.Div(children=[],className="row")

])



if __name__ == '__main__':
    app.run_server()


# In[ ]:


import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.Div(
        html.H3('first dash app and you can type something : ')
                       ),
    html.Div(['type here : ',
              dcc.Input(id="inputa", type="number"),
              html.Span(' type here : '),
              dcc.Input(id="inputb", type="number"),
              html.Span(' type here : '),
              dcc.Input(id="inputc", type="number"),
              html.Hr(),
    html.H3(id='outpout1')])
])

@app.callback(
    Output('outpout1', 'children'),
    [Input("inputa", "value"), Input("inputb", "value"), Input("inputc", "value")],
             )

def rewrite (a, b, c):
    return a, b, c

if __name__ == '__main__':
    app.run_server()


# In[ ]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader.data as web
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(children=[
    html.Div(
        html.H3('pair companies comparision : ',
                style={'margin':'10px','padding':'10px' })
                       ),

              html.Hr(),

html.Div(children=[
        html.Div([
        html.Span(' first code  : '),
        dcc.Input(id="inputcode1", type="text"
                 , style = {'border': '0px', 'borderRadius': '5px','padding':'5px','margin':'5px'}),
        ],className="col-lg"),

        html.Div([
        html.Span(' second code : '),
        dcc.Input(id="inputcode2", type="text"
                 , style = {'border': '0px', 'borderRadius': '5px','padding':'5px','margin':'5px'}),
        ],className="col-lg"),
        html.Div([
        html.Span(' start date : '),
        dcc.Input(id="inputst", type="text"
                 , style = {'border': '0px', 'borderRadius': '5px','padding':'5px','margin':'5px'}),
        ],className="col-lg"),
        html.Div([
        html.Span(' end date : '),
        dcc.Input(id="inputend", type="text"
                 , style = {'border': '0px', 'borderRadius': '5px','padding':'5px','margin':'5px'}),
        ],className="col-lg")

],className="row"),
html.Div(children=[
        html.Div([
            html.Div('soroush')
        ],className="col-lg-4 col-md-6 col-sm border border-dark"),
        html.Div([html.Div('soroush')],className="col-lg-4 col-md-6 col-sm border border-dark"),
        html.Div([html.Div('soroush')],className="col-lg-4 col-md-6 col-sm border border-dark")
],className="row"),
html.Div(children=[
        html.Div([html.Div('soroush')],className="col-lg-6 col-md col-sm border border-dark"),
        html.Div([html.Div('soroush')],className="col-lg-6 col-md col-sm border border-dark"),
],className="row"),

html.Div('@footer'),


], style={
    'margin': '35px',
    'background' : '#F6EFEB',
    'borderRadius' : '7px',
'boxShadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)'
},
    className='text-center')


@app.callback(
    [Output('outpout1', 'children'),Output('outpout2', 'children'),Output('outpout3', 'children'),Output('outpout4', 'children')],
    [Input("inputcode1", "value"),Input("inputcode2", "value"), Input("inputst", "value"), Input("inputend", "value"),Input("inputshift", "value")],
             )
def HistoryGraph(a,d, b, c,e):
    if [a,d, b, c] is None:
        raise PreventUpdate

    company1 = a
    starting = b
    ending = c
    company2 = d
    mm = e
    df1 = web.DataReader(company1, data_source='yahoo', start=starting, end=ending)
    df2 = web.DataReader(company2, data_source='yahoo', start=starting, end=ending)

    correlation = df1['Close'].corr(df2['Close'])
    figure1 = dcc.Graph(
        id='example-graph1',
        figure={'data': [{'x': df1.index, 'y': df1.Close, 'type': 'bar', 'name': company1},
                         {'x': df2.index, 'y': df2.Close,'type': 'bar', 'name': company2},
                         {'x': df2.index, 'y': df2.Close.shift(mm) ,'type': 'bar', 'name': company2+'-shift'}],
                'layout': {
                    'title': company1
                }

                })

    figure3=dcc.Graph(
        id='example-graph3',
        figure={'data': [{'x': df1.index, 'y': df1.Close/df1.Close[0] ,'type': 'line', 'name': company1},
                         {'x': df2.index, 'y': df2.Close/df2.Close[0] ,'type': 'line', 'name': company2}],
                'layout': {
                    'title': "{0} and  {1}".format(company1,company2),

                                    }
                }),

    figure2 = dcc.Graph(
        id='example-graph2',
        figure={'data': [{'x': df2.index, 'y': df2.Close, 'type': 'line', 'name': company2},
                         {'x': df2.index, 'y': df1.Close, 'type': 'line', 'name': company1}],
                'layout': {
                    'title': company2,

                }
                })
    return figure1, figure2, figure3, correlation


if __name__ == '__main__':
    app.run_server()







# In[ ]:




