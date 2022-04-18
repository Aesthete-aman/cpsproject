#!/usr/bin/env python
# coding: utf-8

# # CP - System Project (Heroku + Python Deployment File)

# <h3> Importing the Libraries </h3>

# In[5]:


#Importing the libraries
import pandas as pd
import numpy as np
import dash

from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


# <h3> Dash Frontend Code </h3>

# In[7]:


# Initializing the Dash Object
app = dash.Dash(__name__)
server = app.server
app.title = 'Clinical Prediction System'

app.layout = html.Div([
    html.H1(children='This is my Sample Website'),
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic', children='Enter a value and press submit')])

@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value'))

def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(value,n_clicks)

# Run app and display result inline in the notebook
app.run_server()


# In[ ]:




