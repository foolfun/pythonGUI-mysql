# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 15:18:54 2019

@author: zsl
"""

import random 
import pandas as pd

s='6217'
card_num =[]
flag= 20
while flag:
    s='6217'
    for i in range(19):
        s = s+str(random.randint(0,10))
    if s not in card_num:
        card_num.append(s)
        flag = flag-1

print(card_num)

df = pd.read_excel('./data.xlsx',sheet_name='Sheet1')
df['银行卡号'] = card_num
pd.DataFrame(df).to_excel('data.xlsx', sheet_name='Sheet1', index=False, header=True)

print('hello world')