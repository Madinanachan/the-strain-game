# Imports from 3rd party libraries
# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load 
import pandas as pd

pipeline=load('assets/pipeline.joblib')

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [   
        dcc.Markdown('#### Main Complaint'),
        dcc.Dropdown(
            id='Main Complaint',
            options = [
                {'label':'Anxiety','value':'Anxiety'},
                {'label':'Depression','value':'Depression'},
                {'label':'Insomnia','value':'Insomnia'},
                {'label':'Pain','value':'Pain'},
                {'label':'Stress','value':'Stress'},
                ],
            value='Pain',
            className='mb-5',
            ),

            dcc.Markdown('#### Desired Effect 1'),
            dcc.Dropdown(
            id='Desired Effect 1',
            options = [
                {'label':'Creative','value':'Creative'},
                {'label':'Energetic','value':'Energetic'},
                {'label':'Euphoric','value':'Euphoric'},
                {'label':'Happy','value':'Happy'},
                {'label':'Relaxed','value':'Relaxed'},
                {'label':'Sleepy','value':'Sleepy'},
                {'label':'Uplifted','value':'Uplifted'},
                ],
            value='Happy',
            className='mb-5',
            ),

            dcc.Markdown('#### Desired Effect 2'),
            dcc.Dropdown(
            id='Desired Effect 2',
            options = [
                {'label':'Aroused','value':'Aroused'},
                {'label':'Creative','value':'Creative'},
                {'label':'Energetic','value':'Energetic'},
                {'label':'Euphoric','value':'Euphoric'},
                {'label':'Giggly','value':'Giggly'},
                {'label':'Happy','value':'Happy'},
                {'label':'Relaxed','value':'Relaxed'},
                {'label':'Sleepy','value':'Sleepy'},
                {'label':'Uplifted','value':'Uplifted'},
                ],
            value='Relaxed',
            className='mb-5',
            ),

            """
        
            Enter your preferences and find your strain type!

            """
        
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('#### Tolerance'),
            dcc.Dropdown(
            id='Tolerance',
            options = [
                {'label':'High','value':'High'},
                {'label':'Normal','value':'Normal'},
                {'label':'Low','value':'Low'},
                ],
            value='Normal',
            className='mb-5',
            ),

            dcc.Markdown('#### Energy'),
            dcc.Dropdown(
            id='Energy',
            options = [
                {'label':'Sedating','value':'Sedating'},
                {'label':'Energizing','value':'Energizing'},
                {'label':'none','value':'none'},
                ],
            value='none',
            className='mb-5',
            ),

            dcc.Markdown('#### Discomfort'),
            dcc.Dropdown(
            id='Discomfort',
            options = [
                {'label':'Physical','value':'Physical'},
                {'label':'Cerebral','value':'Cerebral'},
                {'label':'none','value':'none'},
                
                ],
            value='none',
            className='mb-5',
            ),

    ]
)

column3 = dbc.Col(
    [
        html.H2('Strain Type',className='lead'),
        html.Div(id='prediction-content',className='lead'),
        html.Div(id='prediction-image') 

    ]
)

layout = dbc.Row([column1, column2, column3])
@app.callback(
    Output('prediction-content','children'),
    [Input('Main Complaint','value'), Input('Desired Effect 1', 'value'), Input('Desired Effect 2','value'),
    Input('Tolerance','value'), Input('Energy','value'), Input('Discomfort','value')]
)
def prediction (maincmpl,eff1,eff2,Tolerance,Energy,Discomfort):
  df=pd.DataFrame(
      columns=['Secondary Symptom','Main Effect','Secondary Effect','THC Level','Mood', 'Pain Type'],
      data = [[maincmpl,eff1,eff2,Tolerance,Energy,Discomfort]]
  )
  y_pred=pipeline.predict(df)[0]
  return f'{y_pred}'

@app.callback(
    Output('prediction-image','children'),
    [Input('Main Complaint','value'), Input('Desired Effect 1', 'value'), Input('Desired Effect 2','value'),
    Input('Tolerance','value'), Input('Energy','value'), Input('Discomfort','value')]
)
def prediction (maincmpl,eff1,eff2,Tolerance,Energy,Discomfort):
    df=pd.DataFrame(
      columns=['Secondary Symptom','Main Effect','Secondary Effect','THC Level','Mood', 'Pain Type'],
      data = [[maincmpl,eff1,eff2,Tolerance,Energy,Discomfort]]
  )
    y_pred=pipeline.predict(df)[0]
    if y_pred == 'Indica':
        return html.Img(src='assets/Indica.jpg',className='img-fluid', style = {'height': '300px'})
    elif y_pred =='Sativa':
        return html.Img(src='assets/sativa.jpg',className='img-fluid', style = {'height': '300px'})
    else:
        return html.Img(src='assets/hybrid.jpg',className='img-fluid', style = {'height': '300px'})
