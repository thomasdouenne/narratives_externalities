# -*- coding: utf-8 -*-


"""
This script creates a .csv file that matches all French cities to their zip code ('code postal')
For each of them, it provides information about the region they belong to (5 categories)
as well as the size of their urban unit (5 categories).
"""

from __future__ import division


import pandas as pd
import numpy as np




# Read data from Insee
code_insee_code_postal = pd.read_csv(r'C:\Users\thoma\Documents\Github\narratives_externalities\preparation_survey\correspondance-code-insee-code-postal.csv', sep=';')
code_insee_caracteristiques = pd.read_csv(r'C:\Users\thoma\Documents\Github\narratives_externalities\preparation_survey\table-appartenance-geo-communes-21.csv', sep=';')

code_insee_caracteristiques.columns = code_insee_caracteristiques.iloc[4]
code_insee_caracteristiques = code_insee_caracteristiques.iloc[5:]

code_insee_code_postal = code_insee_code_postal.rename(
    columns={'Code INSEE': 'code_insee', 'Code Postal': 'code_postal'}
    )
code_insee_code_postal = code_insee_code_postal[['code_insee', 'code_postal', 'Commune']]

code_insee_caracteristiques = code_insee_caracteristiques.rename(
    columns={'CODGEO': 'code_insee', 'REG': 'code_region', 'TUU2017': 'tuu'}
    )
code_insee_caracteristiques = code_insee_caracteristiques[['code_insee', 'code_region', 'tuu']]


# Merge the two datasets
dataframe = pd.merge(code_insee_code_postal,code_insee_caracteristiques,
                     on="code_insee", how="left")

# Create simple variables for region (5 categories) and size of urban unit (5 categories)
dataframe.insert(loc = 5, column = 'quota_region', value=0)
dataframe.insert(loc = 6, column = 'quota_tuu', value=0)
dataframe['code_region'] = pd.to_numeric(dataframe['code_region'])
dataframe['tuu'] = pd.to_numeric(dataframe['tuu'])

dataframe['quota_region'] = (
    1 * (dataframe['code_region'] == 11) # IDF
    + 2 * ((dataframe['code_region'] == 75) + (dataframe['code_region'] == 76)) # SO
    + 3 * ((dataframe['code_region'] == 24) + (dataframe['code_region'] == 28) + (dataframe['code_region'] == 52) + (dataframe['code_region'] == 53)) # NO
    + 4 * ((dataframe['code_region'] == 27) + (dataframe['code_region'] == 32) + (dataframe['code_region'] == 44)) # NE
    + 5 * ((dataframe['code_region'] == 84) + (dataframe['code_region'] == 93) + (dataframe['code_region'] == 94)) # SE
    )

dataframe['quota_tuu'] = (
    1 * (dataframe['tuu'] == 0)
    + 2 * ((dataframe['tuu'] == 1) + (dataframe['tuu'] == 2) + (dataframe['tuu'] == 3))
    + 3 * ((dataframe['tuu'] == 4) + (dataframe['tuu'] == 5))
    + 4 * ((dataframe['tuu'] == 6) + (dataframe['tuu'] == 7))
    + 5 * (dataframe['tuu'] == 8)
    )

# Clean zip code when there are several for a given city
dataframe['nombre_codes_postaux'] = dataframe['code_postal'].str.count('/') +1
reps = [val for val in dataframe.nombre_codes_postaux]
dataframe = dataframe.loc[np.repeat(dataframe.index.values, reps)]

dataframe['rank'] = dataframe.groupby(['Commune', 'code_postal']).cumcount()+1
dataframe['code_postal_unique'] = dataframe.apply(lambda dataframe: dataframe['code_postal'][0+(dataframe['rank']-1)*6:5+(dataframe['rank']-1)*6], axis=1)
dataframe['code_postal_unique'] = dataframe['code_postal'].where(dataframe['code_postal_unique'].str.len() != 5, other=dataframe['code_postal_unique'])

# Keep only relevant variables and save to csv
donnes_quota_commune = dataframe[['code_postal_unique', 'Commune', 'quota_region', 'quota_tuu']]
donnes_quota_commune = donnes_quota_commune.sort_values(by=['code_postal_unique'])
donnes_quota_commune.to_csv(r'C:\Users\thoma\Documents\Github\narratives_externalities\preparation_survey\table_communes.csv', sep=';')
