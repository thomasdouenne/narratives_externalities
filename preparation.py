  # -*- coding: utf-8 -*-


"""
This script prepares the data collected from the Qualtrics pilot survey
on narratives and externalities to make it ready for analysis
"""

from __future__ import division


import pandas as pd


##### Read data from Qualtrics
data_qualtrics_raw = \
    pd.read_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_pilot_narratives_raw.csv', sep=',')


##### Re-label variables
data_qualtrics_renamed = data_qualtrics_raw.rename(
    columns={'StartDate': 'time_start',
             'EndDate': 'time_end',
             'Duration (in seconds)': 'total_time',
             'Q2': 'postal_code',
             'Q123': 'town_name',
             'Q3': 'sexe',
             'Q4': 'age_group',
             'Q5': 'employment_status',
             'Q6': 'profession_type',
             'Q7': 'diploma',
             'Q8': 'household_size',
             'Q11': 'nb_above_14',
             'Q9': 'income_respondent',
             'Q10': 'income_household',
             'Q24': 'meat_frequency_respondent',
             'Q26': 'meat_frequency_desirable',
             'Q27': 'meat_why_against_open',
             'Q28': 'meat_why_favorable_open',
             'Q120': 'meat_why_neutral_open',
             'Q32': 'meat_landscape_argument_open',
             'Q33': 'meat_carbon_argument_open',
             'Q34': 'airtravel_frequency_respondent',
             'Q37': 'airtravel_frequency_desirable',
             'Q38': 'airtravel_why_favorable_open',
             'Q39': 'airtravel_why_against_open',
             'Q40': 'airtravel_why_neutral_open',
             'Q41': 'airtravel_carbon_argument_open',
             'Q42': 'airtravel_open_mindedness_argument_open',
             'Q101': 'nb_vehicles',
             'Q102': 'nb_kilometers_no_vehicle',
             'Q104': 'fuel_type_only_vehicle',
             'Q103': 'fuel_consumption_only_vehicle',
             'Q109': 'nb_kilometers_only_vehicle',
             'Q106': 'fuel_type_main_vehicle',
             'Q107': 'fuel_type_second_vehicle',
             'Q108': 'fuel_consumption_average_vehicle',
             'Q105': 'nb_kilometers_all_vehicles',
             'Q98': 'vehicle_desirable_future',
             'Q99': 'vehicle_why_against_open',
             'Q111': 'vehicle_why_diesel_open',
             'Q100': 'vehicle_why_favorable_open',
             'Q101.1': 'vehicle_why_neutral_open',
             'Q102.1': 'vehicle_electric_pollutes_more_argument_open',
             'Q103.1': 'vehicle_thermiaue_pollutes_more_argument_open',
             'Q85': 'vaccin_respondent',
             'Q98.1': 'vaccin_third_dose_respondent',
             'Q88': 'vaccin_desirable',
             'Q89': 'vaccin_why_favorable_open',
             'Q90': 'vaccin_why_against_open',
             'Q91': 'vaccin_why_neutral_open',
             'Q92': 'vaccin_poor_country_argument_open',
             'Q93': 'vaccin_protecting_others_argument_open',
             'Q56_1': 'matrix_respondent_meat_farmers_precarity',
             'Q56_2': 'matrix_respondent_meat_natural',
             'Q56_3': 'matrix_respondent_meat_nutrients',
             'Q56_4': 'matrix_respondent_meat_animal_welfare',
             'Q56_5': 'matrix_respondent_meat_global_warming',
             'Q56_6': 'matrix_respondent_meat_cancer',   
             'Q57_1': 'matrix_respondent_airtravel_global_warming',
             'Q57_2': 'matrix_respondent_airtravel_freerider',
             'Q57_3': 'matrix_respondent_airtravel_open_mindedness',
             'Q57_4': 'matrix_respondent_airtravel_against_progress',      
             'Q114_1': 'matrix_respondent_vehicle_air_pollution',
             'Q114_2': 'matrix_respondent_vehicle_nuisance_city',
             'Q114_3': 'matrix_respondent_vehicle_small_share_cc',
             'Q114_4': 'matrix_respondent_vehicle_batteries',
             'Q114_5': 'matrix_respondent_vehicle_nuclear',
             'Q112_1': 'matrix_respondent_vaccin_protecting_others',
             'Q112_2': 'matrix_respondent_vaccin_imperfect_protecting_others',
             'Q112_3': 'matrix_respondent_vaccin_economic_activity',
             'Q112_4': 'matrix_respondent_vaccin_taxes_industry',
             'Q112_5': 'matrix_respondent_vaccin_poor_countries',          
             'Q125_Page Submit': 'matrix_respondent_timer',
             'Q64_1': 'matrix_french_meat_farmers_precarity',
             'Q64_2': 'matrix_french_meat_natural',
             'Q64_3': 'matrix_french_meat_nutrients',
             'Q64_4': 'matrix_french_meat_animal_welfare',
             'Q64_5': 'matrix_french_meat_global_warming',
             'Q64_6': 'matrix_french_meat_cancer',   
             'Q65_1': 'matrix_french_airtravel_global_warming',
             'Q65_2': 'matrix_french_airtravel_freerider',
             'Q65_3': 'matrix_french_airtravel_open_mindedness',
             'Q65_4': 'matrix_french_airtravel_against_progress',      
             'Q115_1': 'matrix_french_vehicle_air_pollution',
             'Q115_2': 'matrix_french_vehicle_nuisance_city',
             'Q115_3': 'matrix_french_vehicle_small_share_cc',
             'Q115_4': 'matrix_french_vehicle_batteries',
             'Q115_5': 'matrix_french_vehicle_nuclear',
             'Q113_1': 'matrix_french_vaccin_protecting_others',
             'Q113_2': 'matrix_french_vaccin_imperfect_protecting_others',
             'Q113_3': 'matrix_french_vaccin_economic_activity',
             'Q113_4': 'matrix_french_vaccin_taxes_industry',
             'Q113_5': 'matrix_french_vaccin_poor_countries',          
             'Q126_Page Submit': 'matrix_french_timer',
             'Q13': 'trust_others',
             'Q14_1': 'life_satisfaction_scale',
             'Q16': 'trust_government',
             'Q17': 'political_leaning',
             'Q18': 'media_for_news',
             'Q116': 'social_networks_frequency',
             'Q20': 'cc_cause',
             'Q21': 'cc_consequences',
             'Q22': 'cc_responsible',
             'Q121': 'trust_scientists',
             'Q63': 'open_box_end'
             }
          ).copy()

##### Create handy variables
data_qualtrics_renamed['topic_meat'] = 1*(data_qualtrics_renamed['meat_frequency_respondent'].isna() == False)
data_qualtrics_renamed['topic_airtravel'] = 1*(data_qualtrics_renamed['airtravel_frequency_respondent'].isna() == False)
data_qualtrics_renamed['topic_vehicle'] = 1*(data_qualtrics_renamed['vehicle_desirable_future'].isna() == False)
data_qualtrics_renamed['topic_vaccin'] = 1*(data_qualtrics_renamed['vaccin_respondent'].isna() == False)

data_qualtrics_renamed['matrix_respondent'] = 1*(data_qualtrics_renamed['matrix_respondent_meat_farmers_precarity'].isna() == False)
data_qualtrics_renamed['matrix_french'] = 1*(data_qualtrics_renamed['matrix_french_meat_farmers_precarity'].isna() == False)

data_qualtrics_renamed['survey_fully_completed'] = 1*(data_qualtrics_renamed['trust_scientists'].isna() == False)


##### Re-code certain variables

def meat_frequency_respondent_num(answer):
    if answer == "Jamais":
        return 0
    elif answer == u'Très occasionnellement':
        return 1
    elif answer == u'1 à 2 repas par semaine':
        return 2
    elif answer == u'3 à 5 repas par semaine':
        return 3
    elif answer == u'Environ un repas par jour':
        return 4
    elif answer == u'Presque à chaque repas':
        return 5
    else:
        return 9999

data_qualtrics_renamed['meat_frequency_respondent_num'] = data_qualtrics_renamed['meat_frequency_respondent'].apply(meat_frequency_respondent_num) 


def meat_frequency_desirable_num(answer):
    if answer == "jamais":
        return 0
    elif answer == u'très occasionnellement':
        return 1
    elif answer == u'1 à 2 repas par semaine':
        return 2
    elif answer == u'3 à 5 repas par semaine':
        return 3
    elif answer == u'environ un repas par jour':
        return 4
    elif answer == u'presque à chaque repas':
        return 5
    elif answer == u'NSP (Ne sait pas, ne se prononce pas).':
        return 99
    else:
        return 9999

data_qualtrics_renamed['meat_frequency_desirable_num'] = data_qualtrics_renamed['meat_frequency_desirable'].apply(meat_frequency_desirable_num) 


##### Create final dataframe with complete answers
df_complete_answers = data_qualtrics_renamed.query('survey_fully_completed == 1').copy()
df_variable_labels = df_complete_answers.head(2)
df_complete_answers = df_complete_answers.drop(df_complete_answers.index[[0,1]])



##### Save dataframe
data_qualtrics_renamed.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_pilot_narratives_prepared_full.csv', sep=',')
df_complete_answers.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_pilot_narratives_prepared.csv', sep=',')
df_variable_labels.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_pilot_narratives_labels.csv', sep=',')
