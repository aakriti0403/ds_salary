# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 20:56:39 2021

@author: HP
"""

import glassdoor_scrapper as gs
import pandas as pd

path="C:/Users/HP/Documents/ds_salary/chromedriver"
df=gs.get_jobs('data scientist',15,False,path,15)
df.to_csv('glassdoor_jobs.csv',index=False)
