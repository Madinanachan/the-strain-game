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
        dcc.Markdown('### An Interesting Trend'),
        dcc.Markdown('##### Some data is not always helpful-- this was exemplified by one of the features I tried to scrape from Leafly. Turns out the most treated complaint pot smokers have is Stress. No Matter what else they had going on; depression, insomnia, anxiety, pain-- one thing remained true. They were all stressed and treating it with cannabis.'),
        html.Img(src='assets/Stressedout.jpg',className='img-fluid', style = {'height': '400px'})

    ],
)

layout = dbc.Row([column1])
