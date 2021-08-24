  
# -*- coding: utf-8 -*-


"""
This script ...
"""

from __future__ import division


import pandas as pd
import numpy as np


# Read data from Insee
data_qualtrics_raw = \
    pd.read_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_raw.csv', sep=',')


##### Survey key statictics

# Average response time:
# Median response time:

donnees_qualtrics.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_treated.csv', sep=',')