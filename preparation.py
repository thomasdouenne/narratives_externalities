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
             'Q33': 'meat_carbon_footprint_argument_open',
             'Q34': 'airtravel_frequency_respondent',
             'Q37': 'airtravel_frequency_desirable',
             'Q38': 'airtravel_why_favorable_open',
             'Q39': 'airtravel_why_against_open',
             'Q40': 'airtravel_why_neutral_open',
             'Q41': 'airtravel_carbon_footprint_argument_open',
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
             'Q103.1': 'vehicle_thermal_pollutes_more_argument_open',
             'Q85': 'vaccine_respondent',
             'Q98.1': 'vaccine_third_dose_respondent',
             'Q88': 'vaccine_desirable',
             'Q89': 'vaccine_why_favorable_open',
             'Q90': 'vaccine_why_against_open',
             'Q91': 'vaccine_why_neutral_open',
             'Q92': 'vaccine_poor_country_argument_open',
             'Q93': 'vaccine_protecting_others_argument_open',
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
             'Q112_1': 'matrix_respondent_vaccine_protecting_others',
             'Q112_2': 'matrix_respondent_vaccine_imperfect_protecting_others',
             'Q112_3': 'matrix_respondent_vaccine_economic_activity',
             'Q112_4': 'matrix_respondent_vaccine_taxes_industry',
             'Q112_5': 'matrix_respondent_vaccine_poor_countries',          
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
             'Q113_1': 'matrix_french_vaccine_protecting_others',
             'Q113_2': 'matrix_french_vaccine_imperfect_protecting_others',
             'Q113_3': 'matrix_french_vaccine_economic_activity',
             'Q113_4': 'matrix_french_vaccine_taxes_industry',
             'Q113_5': 'matrix_french_vaccine_poor_countries',          
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
data_qualtrics_renamed['topic_vaccine'] = 1*(data_qualtrics_renamed['vaccine_respondent'].isna() == False)

data_qualtrics_renamed['matrix_respondent'] = 1*(data_qualtrics_renamed['matrix_respondent_meat_farmers_precarity'].isna() == False)
data_qualtrics_renamed['matrix_french'] = 1*(data_qualtrics_renamed['matrix_french_meat_farmers_precarity'].isna() == False)

data_qualtrics_renamed['survey_fully_completed'] = 1*(data_qualtrics_renamed['trust_scientists'].isna() == False)


##### Re-code certain variables

def matrix_respondent_num(answer):
    if answer == "Pas du tout pertinent":
        return -2
    elif answer == u'Peu pertinent':
        return -1
    elif answer == u'NSP (Ne sait pas, ne se prononce pas)':
        return 0
    elif answer == u'Assez pertinent':
        return 1
    elif answer == u'Très pertinent':
        return 2
    else:
        return 9999

variables_survey = list(data_qualtrics_renamed.columns)
matrix_respondent_variables = list()
for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
    for var in variables_survey:
        if 'matrix_respondent_{}'.format(topic) in var:
            matrix_respondent_variables.append(var)

for var in matrix_respondent_variables:
    data_qualtrics_renamed['{}_num'.format(var)] = data_qualtrics_renamed[var].apply(matrix_respondent_num)


def matrix_french_num(answer):
    if answer == 'Une très petite minorité':
        return -2
    elif answer == u'Une minorité':
        return -1
    elif answer == u'NSP (Ne sait pas, ne se prononce pas)':
        return 0
    elif answer == u'La moitié':
        return 0
    elif answer == u'La majorité':
        return 1
    elif answer == u'La très grande majorité':
        return 2
    else:
        return 9999

matrix_french_variables = list()
for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
    for var in variables_survey:
        if 'matrix_french_{}'.format(topic) in var:
            matrix_french_variables.append(var)

for var in matrix_french_variables:
    data_qualtrics_renamed['{}_num'.format(var)] = data_qualtrics_renamed[var].apply(matrix_french_num)


##### Create final dataframe with complete answers
df_complete_answers = data_qualtrics_renamed.query('survey_fully_completed == 1').copy()
df_variable_labels = df_complete_answers.head(2)
df_complete_answers = df_complete_answers.drop(df_complete_answers.index[[0,1]])

# Compute CO2 emissions from respondents' vehicles
df_complete_answers['average_fuel_consumption_vehicles'] = (
    df_complete_answers['fuel_consumption_only_vehicle'].fillna(0).apply(pd.to_numeric)
    + df_complete_answers['fuel_consumption_average_vehicle'].fillna(0).apply(pd.to_numeric)
    )
df_complete_answers['average_fuel_consumption_vehicles'] = df_complete_answers['average_fuel_consumption_vehicles'] + 6.5 * (df_complete_answers['average_fuel_consumption_vehicles'] == 0)

df_complete_answers['total_nb_kilometers'] = (
    df_complete_answers['nb_kilometers_no_vehicle'].fillna(0).apply(pd.to_numeric)
    + df_complete_answers['nb_kilometers_only_vehicle'].fillna(0).apply(pd.to_numeric)
    + df_complete_answers['nb_kilometers_all_vehicles'].fillna(0).apply(pd.to_numeric)
    )

df_complete_answers['co2_intensity_vehicles'] = (
    0.00250 * (df_complete_answers['nb_vehicles'] == 'Aucun') # TODO: 0.00250 is an arbitrary number
    + 0.00228 * (df_complete_answers['fuel_type_only_vehicle'] == 'Essence')
    + 0.00265 * (df_complete_answers['fuel_type_only_vehicle'] == 'Diesel')
    + 0.0005 * (df_complete_answers['fuel_type_only_vehicle'] == u'Électrique ou hybride.')
    + 0.00250 * (df_complete_answers['fuel_type_only_vehicle'] == u'Autre')
    + (2/3) * 0.00228 * (df_complete_answers['fuel_type_main_vehicle'] == 'Essence')
    + (2/3) * 0.00265 * (df_complete_answers['fuel_type_main_vehicle'] == 'Diesel')
    + (2/3) * 0.0005 * (df_complete_answers['fuel_type_main_vehicle'] == u'Électrique ou hybride.') # TODO: 0.0005 is an arbitrary number
    + (2/3) * 0.00250 * (df_complete_answers['fuel_type_main_vehicle'] == u'Autre') # TODO: 0.0025 is an arbitrary number
    + (1/3) * 0.00228 * (df_complete_answers['fuel_type_second_vehicle'] == 'Essence')
    + (1/3) * 0.00265 * (df_complete_answers['fuel_type_second_vehicle'] == 'Diesel')
    + (1/3) * 0.0005 * (df_complete_answers['fuel_type_second_vehicle'] == u'Électrique ou hybride.') # TODO: 0.0005 is an arbitrary number
    + (1/3) * 0.00250 * (df_complete_answers['fuel_type_second_vehicle'] == u'Autre') # TODO: 0.0025 is an arbitrary number
    )

df_complete_answers['co2_emissions_vehicles'] = (
    df_complete_answers['total_nb_kilometers'] * 0.01 * df_complete_answers['average_fuel_consumption_vehicles'] * df_complete_answers['co2_intensity_vehicles']
    )

df_complete_answers['co2_quintile'] = (
    1 * (df_complete_answers['topic_vehicle'] == 1)
    + 1 * (df_complete_answers['co2_emissions_vehicles'] > (df_complete_answers[df_complete_answers['topic_vehicle']==1]['co2_emissions_vehicles'].quantile(0.2)))
    + 1 * (df_complete_answers['co2_emissions_vehicles'] > (df_complete_answers[df_complete_answers['topic_vehicle']==1]['co2_emissions_vehicles'].quantile(0.4)))
    + 1 * (df_complete_answers['co2_emissions_vehicles'] > (df_complete_answers[df_complete_answers['topic_vehicle']==1]['co2_emissions_vehicles'].quantile(0.6)))
    + 1 * (df_complete_answers['co2_emissions_vehicles'] > (df_complete_answers[df_complete_answers['topic_vehicle']==1]['co2_emissions_vehicles'].quantile(0.8)))
    )

df_complete_answers['km_quintile'] = (
    1 * (df_complete_answers['topic_vehicle'] == 1)
    + 1 * (df_complete_answers['total_nb_kilometers'] > (df_complete_answers[df_complete_answers['topic_vehicle']==1]['total_nb_kilometers'].quantile(0.2)))
    + 1 * (df_complete_answers['total_nb_kilometers'] > (df_complete_answers[df_complete_answers['topic_vehicle']==1]['total_nb_kilometers'].quantile(0.4)))
    + 1 * (df_complete_answers['total_nb_kilometers'] > (df_complete_answers[df_complete_answers['topic_vehicle']==1]['total_nb_kilometers'].quantile(0.6)))
    + 1 * (df_complete_answers['total_nb_kilometers'] > (df_complete_answers[df_complete_answers['topic_vehicle']==1]['total_nb_kilometers'].quantile(0.8)))
    )


df_complete_answers['electric_or_hybrid_dummy'] = (
    1 * (df_complete_answers['fuel_type_only_vehicle'] == u'Électrique ou hybride.')
    + 1 * (df_complete_answers['fuel_type_main_vehicle'] == u'Électrique ou hybride.')
    + 1 * (df_complete_answers['fuel_type_second_vehicle'] == u'Électrique ou hybride.')
    - 1 * (df_complete_answers['fuel_type_main_vehicle'] == u'Électrique ou hybride.') * (df_complete_answers['fuel_type_second_vehicle'] == u'Électrique ou hybride.')
    )

##### Save dataframe
data_qualtrics_renamed.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_pilot_narratives_prepared_full.csv', sep=',')
df_complete_answers.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_pilot_narratives_prepared.csv', sep=',')
df_variable_labels.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_pilot_narratives_labels.csv', sep=',')
