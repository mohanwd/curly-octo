#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 19:23:19 2023

@author: mohankumar
"""

import requests
import pandas as pd
import moving_averages as mv
import regression as reg
import json


def getFromLocal():
    f = open('input.json')
    r = json.load(f)
    
    columns = r['dataset']['column_names']
    data = r['dataset']['data']

    df = pd.DataFrame(data, columns = columns)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df.Date.dt.strftime('%Y-%m')
    df = df.sort_values(by='Date')
    
    return df

def getDataFrame(url):
    
    r = requests.get(url)

    columns = r.json()['dataset']['column_names']
    data = r.json()['dataset']['data']
    
    df = pd.DataFrame(data, columns = columns)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df.Date.dt.strftime('%Y-%m')
    df.sort_values(by='Date')
    
    return df

def main():
    
    url = 'https://www.quandl.com/api/v3/datasets/FSE/BDT_X'
    #df = getDataFrame(url)
    df = getFromLocal()
    mv.getFigure(df).savefig('output/MovingAverages.png')
    
    df = getFromLocal()
    reg.reg_90_days(df).savefig('output/Line90Reg.png')
    reg.reg_30_days(df).savefig('output/Line30Reg.png')
    reg.reg_7_days(df).savefig('output/Line7Reg.png')
    

if __name__=="__main__":
    main()