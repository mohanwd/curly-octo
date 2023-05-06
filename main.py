#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 19:23:19 2023

@author: mohankumar
"""

import requests
import pandas as pd
import json
from scripts import moving_averages as mv
from scripts import regression as reg
from scripts import indicator as ind


def getDataFrame(url):
    data = []
    columns = []
    r = requests.get(url)
    
    if r.status_code == 200:
        columns = r.json()['dataset']['column_names']
        data = r.json()['dataset']['data']
    else:
        #Gettting data from Local, Server is busy
        f = open('input.json')
        r = json.load(f)
        columns = r['dataset']['column_names']
        data = r['dataset']['data']
    
    df = pd.DataFrame(data, columns = columns)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df.Date.dt.strftime('%Y-%m')
    df = df.sort_values(by='Date')
    
    return df

def main():
    
    #Data is fetched from URL provided and converted to data frame
    #Server has been down for some time hence added a local file for development
    url = 'https://www.quandl.com/api/v3/datasets/FSE/BDT_X'
    df = getDataFrame(url)
    
    #Calculating, Plotting Moving & Monthly averages (Assuming everything has to be plotted in single graph)
    mv.getFigure(df).savefig('output/MovingAverages.png')
    
    #Plotting regression lines for last 90,30 & 7 days
    df = getDataFrame(url)
    reg.reg_90_days(df).savefig('output/Line90Reg.png')
    reg.reg_30_days(df).savefig('output/Line30Reg.png')
    reg.reg_7_days(df).savefig('output/Line7Reg.png')
    
    # Calculating & Plotting Markers for consecutive 5 positive and 4 negative days
    df["value_minus_4"] = df["Close"].shift(4)
    df["value_minus_3"] = df["Close"].shift(3)
    df["value_minus_2"] = df["Close"].shift(2)
    df["value_minus_1"] = df["Close"].shift(1)
    
    ind.postive_indicator(df).savefig('output/PositiveMarker.png')
    ind.negative_indicator(df).savefig('output/NegativeMarker.png')
    
    #All the outputs have been saved as png format in working location's `output` directory

if __name__=="__main__":
    main()