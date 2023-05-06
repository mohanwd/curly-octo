#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 23:58:36 2023

@author: mohankumar
"""
import pandas as pd
from datetime import datetime,timedelta
import seaborn as sns
import matplotlib.pyplot as plt


def plot_reg_graph(N_DAYS_AGO,df):
    
    max_date = df["Date"].max().date()
    start_date = max_date - timedelta(days=N_DAYS_AGO)  
    data_df = df[df['Date'] >= pd.to_datetime(start_date)]
    data_df.set_index(['Date'], inplace=True)
    data_df.index = data_df.index.map(pd.Timestamp.toordinal)
    
    # convert the regression line start date to ordinal
    x1 = pd.to_datetime(start_date).toordinal()
    data_df = data_df[['Close']]    
    
    # data slice for the regression line
    data=data_df.loc[x1:].reset_index()
    
    # plot the Adj Close data
    ax1 = data_df.plot(y='Close', c='k', figsize=(15, 6), grid=True, legend=False,
                  title=f'Close with Regression Line from {start_date}  - {N_DAYS_AGO} Days')
    
    # add a regression line
    sns.regplot(data=data, x='Date', y='Close', ax=ax1, color='magenta', scatter_kws={'s': 7}, label='Linear Model', scatter=False)
    
    ax1.set_xlim(data_df.index[0], data_df.index[-1])
    
    # convert the axis back to datetime
    xticks = ax1.get_xticks()
    labels = [pd.Timestamp.fromordinal(int(label)).date() for label in xticks]
    ax1.set_xticks(xticks)
    ax1.set_xticklabels(labels)
    
    ax1.legend()
    
    return ax1.get_figure()

def reg_90_days(df):
    pg = plot_reg_graph(90,df)
    return pg

def reg_30_days(df):
    pg = plot_reg_graph(30,df)
    return pg

def reg_7_days(df):
    pg = plot_reg_graph(7,df)
    return pg


