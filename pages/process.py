# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown( '### Dataset and Model'),
        dcc.Markdown('##### The dataset was obtained off of the popular cannabis webcite leafly via symptom releif and perceived effects from reviews of individual strains. For the Baseline model Hybrid was predicted everytime for ~49% accuracy. The final model chosen was an Ordinally Encoded Decision Tree, as its ROC AUC score was best at 75%--more than beating baseline.'),
        dcc.Markdown('##### Several features were enginered; Tolerance, Energy, and Discomfort. These helped narrow in on strain types. Using Feature Importance graphs to judge, irrelevant features were discluded for the success of the model. '),
        html.Img(src='assets/Permutation.jpg',className='img-fluid',style={'height':'200px'}),

    ],
)

column2= dbc.Col(
    [
        dcc.Markdown('### Feature Importance'),
        html.Img(src='assets/FI4.jpg',className='img-fluid', style = {'height': '200px'}),
        html.Img(src='assets/Featureimportance2.jpg',className='img-fluid', style = {'height': '200px'}),
        dcc.Markdown('##### Feature Importance and Permutation Importance show the relative importance of the features to the overall model.')
    ]
)

layout = dbc.Row([column1,column2])
