  # -*- coding: utf-8 -*-


"""
This script analyzes the data collected from the Qualtrics pilot survey on narratives and externalities
"""

from __future__ import division


import pandas as pd


##### Read data from Qualtrics
df_pilot = \
    pd.read_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_pilot_narratives_prepared.csv', sep=',', index_col=0)


##### Survey key statictics
print(df_pilot['total_time'].quantile(0.9) / 60) # Median response time
print(len(df_pilot['total_time'])) # Number of respondents


##### Meat
df_meat = df_pilot.query('topic_meat == 1').copy()

items_respondents_meat = [u'Jamais', u'Très occasionnellement', u'1 à 2 repas par semaine',
             u'3 à 5 repas par semaine', u'Environ un repas par jour', u'Presque à chaque repas']
items_desirable_meat = [u'jamais', u'très occasionnellement', u'1 à 2 repas par semaine',
             u'3 à 5 repas par semaine', u'environ un repas par jour',
             u'presque à chaque repas', u'NSP (Ne sait pas, ne se prononce pas).']

for item in items_respondents_meat:
    print(item, ":", float(len(df_meat[df_meat.meat_frequency_respondent == item])) / len(df_meat))

for item in items_desirable_meat:
    print(item, ":", float(len(df_meat[df_meat.meat_frequency_desirable == item])) / len(df_meat))

df_transition_matrix_meat_frequency = pd.DataFrame(index=items_desirable_meat, columns=items_respondents_meat, dtype=float)
for respondent in items_respondents_meat:
    for desirable in items_desirable_meat:
        df_transition_matrix_meat_frequency[respondent][desirable] = \
            float(len(df_meat[df_meat.meat_frequency_respondent == respondent][df_meat.meat_frequency_desirable == desirable])) / len(df_meat[df_meat.meat_frequency_respondent == respondent])

pd.options.display.float_format = '{:.1%}'.format
#print(df_transition_matrix_meat_frequency.to_latex(caption='Matrix of opinions on meat consumption'))


##### Air travel
df_airtravel = df_pilot.query('topic_airtravel == 1').copy()

items_respondents_airtravel = [u'Non, je ne le prend pas ou plus', u'Oui, moins d\'une fois par an',
                     u'Oui, environ une fois (aller-retour) par an', u'Oui, environ deux fois (aller-retour) par an',
                     u'Oui, plus de deux fois (aller-retour) par an']
items_desirable_airtravel = [u'jamais', u'au moins une fois dans leur vie',
                   u'environ une fois par an', u'plusieurs fois par an',
                   'le plus souvent possible', u'NSP (Ne sait pas, ne se prononce pas).']

for item in items_respondents_airtravel:
    print(item, ":", float(len(df_airtravel[df_airtravel.airtravel_frequency_respondent == item])) / len(df_airtravel))

for item in items_desirable_airtravel:
    print(item, ":", float(len(df_airtravel[df_airtravel.airtravel_frequency_desirable == item])) / len(df_airtravel))

df_transition_matrix_airtravel_frequency = pd.DataFrame(index=items_desirable_airtravel, columns=items_respondents_airtravel, dtype=float)
for respondent in items_respondents_airtravel:
    for desirable in items_desirable_airtravel:
        df_transition_matrix_airtravel_frequency[respondent][desirable] = \
            float(len(df_airtravel[df_airtravel.airtravel_frequency_respondent == respondent][df_airtravel.airtravel_frequency_desirable == desirable])) / len(df_airtravel[df_airtravel.airtravel_frequency_respondent == respondent])

#print(df_transition_matrix_airtravel_frequency.to_latex(caption='Matrix of opinions on air travel consumption'))


##### Vehicles
df_vehicle = df_pilot.query('topic_vehicle == 1').copy()

print(df_vehicle['total_nb_kilometers'].mean())
print(df_vehicle['total_nb_kilometers'].quantile(0.75))

print(df_vehicle['co2_emissions_vehicles'].mean())
print(df_vehicle['co2_emissions_vehicles'].quantile(0.25))

items_desirable_vehicle = [u'de cesser de les utiliser très rapidement (d\'ici 2030 ou avant)', u'de cesser de les utiliser progressivement (d\'ici 2040 ou 2050)',
                           u'de cesser d\'utiliser les véhicules diesel mais pas les véhicule essence', u'de continuer à les utiliser tant que des progrès majeurs ne sont pas fait vis-à-vis des véhicules électriques',
                           u'de continuer à les utiliser aussi longtemps que le pétrole est disponible', u'NSP (Ne sait pas, ne se prononce pas).']

for item in items_desirable_vehicle:
    print(item, ":", float(len(df_vehicle[df_vehicle.vehicle_desirable_future == item])) / len(df_vehicle))

df_transition_matrix_vehicle = pd.DataFrame(index=items_desirable_vehicle, columns=range(1,6), dtype=float)
for respondent in range(1,6):
    for desirable in items_desirable_vehicle:
        df_transition_matrix_vehicle[respondent][desirable] = \
            float(len(df_vehicle[df_vehicle.co2_quintile == respondent][df_vehicle.vehicle_desirable_future == desirable])) / len(df_vehicle[df_vehicle.co2_quintile == respondent])

#print(df_transition_matrix_vehicle.to_latex(caption='Matrix of opinions on the future of thermic vehicles'))


##### Vaccin
df_vaccin = df_pilot.query('topic_vaccin == 1').copy()

items_respondents_vaccin = [u'Oui, j\'ai déjà reçu deux injections', u'Oui, j\'ai reçu la première injection',
                            u'Non, mais j\'ai déjà mon rendez-vous pour la première injection',
                            u'Non, mais je compte le faire à un moment donné', u'Non, le vaccin m\'est déconseillé pour des raisons personnelles',
                            u'Non, je ne souhaite pas être vacciné', u'Je préfère ne pas répondre à cette question']
items_desirable_vaccin = [u'tous les Français se fassent vacciner à partir de 12 ans', u'tous les Français se fassent vacciner à partir de 18 ans',
                          u'seules les personnes à risque se fassent vacciner', u'les Français évitent de se faire vacciner',
                          u'chacun décide de se faire vacciner en fonction de ses propres opinions et facteurs de risque',
                          u'NSP (Ne sait pas, ne se prononce pas).']

for item in items_respondents_vaccin:
    print(item, ":", float(len(df_vaccin[df_vaccin.vaccin_respondent == item])) / len(df_vaccin))

for item in items_desirable_vaccin:
    print(item, ":", float(len(df_vaccin[df_vaccin.vaccin_desirable == item])) / len(df_vaccin))

df_transition_matrix_vaccin = pd.DataFrame(index=items_desirable_vaccin, columns=items_respondents_vaccin, dtype=float)
for respondent in items_respondents_vaccin:
    for desirable in items_desirable_vaccin:
        df_transition_matrix_vaccin[respondent][desirable] = \
            float(len(df_vaccin[df_vaccin.vaccin_respondent == respondent][df_vaccin.vaccin_desirable == desirable])) / len(df_vaccin[df_vaccin.vaccin_respondent == respondent])

#print(df_transition_matrix_vaccin.to_latex(caption='Matrix of opinions on covid vaccin'))
