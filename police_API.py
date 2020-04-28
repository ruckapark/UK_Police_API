# -*- coding: utf-8 -*-
"""
Spyder Editor

This is an example for retrieving data from a free access UK API

The output is a function that can be used to locate crime data depending on the given parameters
"""

import requests
import json

parameters = {'lat' : 52.59,'lng' : -3.85} #machynlleth wales - my old home
api_address = "https://data.police.uk/api/crimes-street/all-crime"

response = requests.get(api_address, params = parameters)
text = json.dumps(response.json(), indent = 2)

data = json.loads(text)
categories = [crime['category'] for crime in data]

#%%

import pandas as pd

def plot_crime_types(lat,lng):
    """
    Display table of crime types for a given point in the UK
    """
    
    parameters = {'lat':lat,'lng':lng}
    api_address = "https://data.police.uk/api/crimes-street/all-crime"
    
    response = requests.get(api_address, params = parameters)
    text = json.dumps(response.json(), indent = 2)
    
    data = json.loads(text)
    df = pd.DataFrame(data)
    print(df['category'].value_counts())