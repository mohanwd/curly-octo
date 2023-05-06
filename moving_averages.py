#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 19:44:28 2023

@author: mohankumar
"""
import pandas as pd

def getFigure(df):
    
    #Calculating Monthly Averages
    df_ma = df
    df_ma = df_ma.groupby(df_ma.Date.dt.strftime('%Y-%m')).Close.agg(['mean'])

    #Calculating 90, 30 & 7 Days Moving Averages
    df_ra = df
    df_ra.set_index(['Month','Date'], inplace=True)
    df_ra = df_ra['Close'].to_frame()
    df_ra['MA'] = df_ra.mean(axis=0)
    df_ra['MA90'] = df_ra['Close'].rolling(90).mean()
    df_ra['MA30'] = df_ra['Close'].rolling(30).mean()
    df_ra['MA07'] = df_ra['Close'].rolling(7).mean()

    #Merging `Rolling Averages` and `Monthly Average`
    df_ra.reset_index(drop=False,inplace=True)
    df_ma.reset_index(drop=False,inplace=True)

    df_ma.rename(columns = {'Date':'Month'}, inplace = True)
    df_ma.rename(columns = {'mean':'MonthlyAvg'}, inplace = True)

    df_avg = pd.merge(df_ra, df_ma, on='Month')
    df_avg.set_index(['Date'], inplace=True)


    #Plotting Graph
    plot_graph = df_avg[['MA30','MA90','MA07','MonthlyAvg']].plot(label='Liquidity',figsize=(16, 8),title='Monthly and Moving Averages Chart for 90,30 & 7 days').get_figure()
    
    return plot_graph
    