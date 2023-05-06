#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 13:11:02 2023

@author: mohankumar
"""


import pandas as pd

def postive_indicator(df):
    df_pos = df[(df['value_minus_4'] < df['value_minus_3']) & (df['value_minus_3'] < df['value_minus_2']) & 
        (df['value_minus_2'] < df['value_minus_1']) & (df['value_minus_1'] < df['Close'])]
    df_pos['pos_ind'] = True
    df_pos = df_pos[['Date','pos_ind']]
    df = pd.merge(df, df_pos, on='Date', how='left')
    df = df[['Date','Close','pos_ind']]
    df = df.fillna(False)
    
    pg = df[df.pos_ind].plot(kind="line", x="Date", y="Close",c='grey',markerfacecolor='green', marker="^",figsize=(35, 20),title=f'Plotting 5 consecutive days of prices going up').get_figure()
    return pg
    

def negative_indicator(df):
    df_neg = df[(df['value_minus_3'] > df['value_minus_2']) & (df['value_minus_2'] > df['value_minus_1']) &
       (df['value_minus_1'] > df['Close'])]
    df_neg['neg_ind'] = True
    df_neg = df_neg[['Date','neg_ind']]
    df = pd.merge(df, df_neg, on='Date', how='left')
    df = df[['Date','Close','neg_ind']]
    df = df.fillna(False)
    pg = df[df.neg_ind].plot(kind="line", x="Date", y="Close",c='grey',markerfacecolor='red', marker="v",figsize=(35, 20),title=f'Plotting 4 consecutive days of prices going down').get_figure()
    return pg








