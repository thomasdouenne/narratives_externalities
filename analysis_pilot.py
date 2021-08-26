  # -*- coding: utf-8 -*-


"""
This script analyzes the data collected from the Qualtrics pilot survey on narratives and externalities
"""

from __future__ import division


import pandas as pd

pd.options.display.float_format = '{:.1%}'.format # pandas df display numbers in %.

##### Read data from Qualtrics
data_pilot = {}

data_pilot['full'] = \
    pd.read_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_pilot_narratives_prepared.csv', sep=',', index_col=0)

data_pilot['meat'] = data_pilot['full'].query('topic_meat == 1').copy()
data_pilot['airtravel'] = data_pilot['full'].query('topic_airtravel == 1').copy()
data_pilot['vehicle'] = data_pilot['full'].query('topic_vehicle == 1').copy()
data_pilot['vaccine'] = data_pilot['full'].query('topic_vaccine == 1').copy()
data_pilot['matrix_respondent'] = data_pilot['full'].query('matrix_respondent == 1').copy()
data_pilot['matrix_french'] = data_pilot['full'].query('matrix_french == 1').copy()


##### Survey key statictics
dict_survey_statistics = {}

vehicle_use_variables = ['total_nb_kilometers', 'co2_emissions_vehicles']
dict_survey_statistics['vehicle_use'] = pd.DataFrame(index=vehicle_use_variables,
                                                      columns=['mean', 'percentile_25', 'percentile_50', 'percentile_75'])
for var in vehicle_use_variables:
    dict_survey_statistics['vehicle_use']['mean'][var] = data_pilot['vehicle'][var].mean()
    dict_survey_statistics['vehicle_use']['percentile_25'][var] = data_pilot['vehicle'][var].quantile(0.25)
    dict_survey_statistics['vehicle_use']['percentile_50'][var] = data_pilot['vehicle'][var].quantile(0.5)
    dict_survey_statistics['vehicle_use']['percentile_75'][var] = data_pilot['vehicle'][var].quantile(0.75)
del vehicle_use_variables, var

time_variables = ['total_time', 'matrix_respondent_timer', 'matrix_french_timer']
dict_survey_statistics['time'] = pd.DataFrame(index=time_variables,
                                    columns=['mean', 'percentile_10', 'percentile_25',
                                             'percentile_50', 'percentile_75', 'percentile_90'])
for var in time_variables:
    dict_survey_statistics['time']['mean'][var] = data_pilot['full'][var].mean() / 60
    dict_survey_statistics['time']['percentile_10'][var] = data_pilot['full'][var].quantile(0.10) / 60
    dict_survey_statistics['time']['percentile_25'][var] = data_pilot['full'][var].quantile(0.25) / 60
    dict_survey_statistics['time']['percentile_50'][var] = data_pilot['full'][var].quantile(0.5) / 60
    dict_survey_statistics['time']['percentile_75'][var] = data_pilot['full'][var].quantile(0.75) / 60
    dict_survey_statistics['time']['percentile_90'][var] = data_pilot['full'][var].quantile(0.90) / 60
del time_variables, var

sub_samples_variables = ['total', 'topic_meat', 'topic_airtravel', 'topic_vehicle', 'topic_vaccine',
                         'matrix_respondent', 'matrix_french']
dict_survey_statistics['nb_respondents'] = pd.DataFrame(index=sub_samples_variables,
                                                      columns=['number', 'percentage'])
for var in sub_samples_variables:
    if var == 'total':
        dict_survey_statistics['nb_respondents']['number'][var] = len(data_pilot['full'])
        dict_survey_statistics['nb_respondents']['percentage'][var] = float(len(data_pilot['full'])) / len(data_pilot['full'])
    else:
        dict_survey_statistics['nb_respondents']['number'][var] = len(data_pilot['full'].query('{} == 1'.format(var)))
        dict_survey_statistics['nb_respondents']['percentage'][var] = \
            float(len(data_pilot['full'].query('{} == 1'.format(var)))) / len(data_pilot['full'])
del sub_samples_variables, var

dict_survey_statistics['socio_demographics'] = {}

dict_survey_statistics['socio_demographics']['sexe'] = {}
dict_survey_statistics['socio_demographics']['sexe']['woman'] = float(len(data_pilot['full'][data_pilot['full']['sexe']=='Féminin'])) / len(data_pilot['full'])
dict_survey_statistics['socio_demographics']['sexe']['man'] = float(len(data_pilot['full'][data_pilot['full']['sexe']=='Masculin'])) / len(data_pilot['full'])

dict_survey_statistics['socio_demographics']['age_group'] = {}
for age in [u'18 à 24 ans', u'25 à 34 ans', u'35 à 49 ans', u'50 à 64 ans', u'65 ans ou plus']:
    dict_survey_statistics['socio_demographics']['age_group'][age] = \
        float(len(data_pilot['full'][data_pilot['full']['age_group']=='{}'.format(age)])) / len(data_pilot['full'])
del age

dict_survey_statistics['socio_demographics']['employment_status'] = {}
for status in [u'Fonctionnaire', u'CDI', u'CDD', u'Intérimaire ou contrat précaire', u'Au chômage',
               u'Étudiant(e)', u'Retraité(e)', u'Autre actif', u'Inactif']:
    dict_survey_statistics['socio_demographics']['employment_status'][status] = \
        float(len(data_pilot['full'][data_pilot['full']['employment_status']=='{}'.format(status)])) / len(data_pilot['full'])
del status

dict_survey_statistics['socio_demographics']['profession_type'] = {}
for profession in [u'Agriculteur/rice', u'Artisan, commerçant(e), chef(fe) d\'entreprise', u'Cadre ou profession intellectuelle supérieure',
                   u'Profession intermédiaire', u'Employé(e)', u'Ouvrier/ère', u'Retraité(e)', u'Autre Inactif/ve']:
    dict_survey_statistics['socio_demographics']['profession_type'][profession] = \
        float(len(data_pilot['full'][data_pilot['full']['profession_type']=='{}'.format(profession)])) / len(data_pilot['full'])
del profession

dict_survey_statistics['socio_demographics']['diploma'] = {}
for diploma in [u'Aucun diplôme', u'Brevet des collèges', u'CAP ou BEP', u'Baccalauréat',
                u'Bac +2 (BTS, DUT, DEUG, écoles de formation sanitaires et sociales...)', u'Bac +3 (licence...)',
                u'Bac +5 ou plus (master, école d\'ingénieur ou de commerce, doctorat, médecine, maîtrise, DEA, DESS...)']:
    dict_survey_statistics['socio_demographics']['diploma'][diploma] = \
        float(len(data_pilot['full'][data_pilot['full']['diploma']=='{}'.format(diploma)])) / len(data_pilot['full'])
del diploma

for var in ['household_size', 'nb_above_14', 'income_respondent', 'income_household']:
    dict_survey_statistics['socio_demographics'][var] = {}
    dict_survey_statistics['socio_demographics'][var]['mean'] = data_pilot['full'][var].mean()
    for percentile in [10, 25, 50, 75, 90]:
        dict_survey_statistics['socio_demographics'][var]['percentile_'+str(percentile)] = \
             data_pilot['full'][var].quantile(percentile/100)
del percentile

##### Meat
items_respondents_meat = [u'Jamais', u'Très occasionnellement', u'1 à 2 repas par semaine',
             u'3 à 5 repas par semaine', u'Environ un repas par jour', u'Presque à chaque repas']
items_desirable_meat = [u'jamais', u'très occasionnellement', u'1 à 2 repas par semaine',
             u'3 à 5 repas par semaine', u'environ un repas par jour',
             u'presque à chaque repas', u'NSP (Ne sait pas, ne se prononce pas).']

dict_meat = {}
dict_meat['frequency_respondents'] = pd.DataFrame(index=items_respondents_meat, columns=['result'])
for item in items_respondents_meat:
    dict_meat['frequency_respondents']['result'][item] = float(len(data_pilot['meat'][data_pilot['meat'].meat_frequency_respondent == item])) / len(data_pilot['meat'])
    

dict_meat['frequency_desirable'] = pd.DataFrame(index=items_desirable_meat, columns=['result'])
for item in items_desirable_meat:
    dict_meat['frequency_desirable']['result'][item] = float(len(data_pilot['meat'][data_pilot['meat'].meat_frequency_desirable == item])) / len(data_pilot['meat'])

dict_meat['joint_respondent_desirable'] = pd.DataFrame(index=items_desirable_meat, columns=items_respondents_meat, dtype=float)
for respondent in items_respondents_meat:
    for desirable in items_desirable_meat:
        dict_meat['joint_respondent_desirable'][respondent][desirable] = \
            float(len(data_pilot['meat'][data_pilot['meat'].meat_frequency_respondent == respondent][data_pilot['meat'].meat_frequency_desirable == desirable])) / len(data_pilot['meat'][data_pilot['meat'].meat_frequency_respondent == respondent])

del items_respondents_meat, items_desirable_meat, item, respondent, desirable
#print(dict_meat['joint_respondent_desirable'].to_latex(caption='Matrix of opinions on meat consumption'))


##### Air travel
items_respondents_airtravel = [u'Non, je ne le prend pas ou plus', u'Oui, moins d\'une fois par an',
                     u'Oui, environ une fois (aller-retour) par an', u'Oui, environ deux fois (aller-retour) par an',
                     u'Oui, plus de deux fois (aller-retour) par an']
items_desirable_airtravel = [u'jamais', u'au moins une fois dans leur vie',
                   u'environ une fois par an', u'plusieurs fois par an',
                   'le plus souvent possible', u'NSP (Ne sait pas, ne se prononce pas).']

dict_airtravel = {}
dict_airtravel['frequency_respondents'] = pd.DataFrame(index=items_respondents_airtravel, columns=['result'])
for item in items_respondents_airtravel:
    dict_airtravel['frequency_respondents']['result'][item] = float(len(data_pilot['airtravel'][data_pilot['airtravel'].airtravel_frequency_respondent == item])) / len(data_pilot['airtravel'])

dict_airtravel['frequency_desirable'] = pd.DataFrame(index=items_desirable_airtravel, columns=['result'])
for item in items_desirable_airtravel:
    dict_airtravel['frequency_desirable']['result'][item] = float(len(data_pilot['airtravel'][data_pilot['airtravel'].airtravel_frequency_desirable == item])) / len(data_pilot['airtravel'])

dict_airtravel['joint_respondent_desirable'] = pd.DataFrame(index=items_desirable_airtravel, columns=items_respondents_airtravel, dtype=float)
for respondent in items_respondents_airtravel:
    for desirable in items_desirable_airtravel:
        dict_airtravel['joint_respondent_desirable'][respondent][desirable] = \
            float(len(data_pilot['airtravel'][data_pilot['airtravel'].airtravel_frequency_respondent == respondent][data_pilot['airtravel'].airtravel_frequency_desirable == desirable])) / len(data_pilot['airtravel'][data_pilot['airtravel'].airtravel_frequency_respondent == respondent])

del items_respondents_airtravel, items_desirable_airtravel, item, respondent, desirable
#print(df_transition_matrix_airtravel_frequency.to_latex(caption='Matrix of opinions on air travel consumption'))


##### Vehicles
dict_vehicle = {}

items_number_vehicles = [u'Aucun', u'Un', u'Deux ou plus']
items_desirable_vehicle = [u'de cesser de les utiliser très rapidement (d\'ici 2030 ou avant)', u'de cesser de les utiliser progressivement (d\'ici 2040 ou 2050)',
                           u'de cesser d\'utiliser les véhicules diesel mais pas les véhicule essence', u'de continuer à les utiliser tant que des progrès majeurs ne sont pas fait vis-à-vis des véhicules électriques',
                           u'de continuer à les utiliser aussi longtemps que le pétrole est disponible', u'NSP (Ne sait pas, ne se prononce pas).']

dict_vehicle['desirable_future'] = pd.DataFrame(index=items_desirable_vehicle, columns=['result'], dtype=float)
for item in items_desirable_vehicle:
    dict_vehicle['desirable_future']['result'][item] = float(len(data_pilot['vehicle'][data_pilot['vehicle'].vehicle_desirable_future == item])) / len(data_pilot['vehicle'])

dict_vehicle['joint_carbon_quintile_desirable'] = pd.DataFrame(index=items_desirable_vehicle, columns=range(1,6), dtype=float)
for respondent in range(1,6):
    for desirable in items_desirable_vehicle:
        dict_vehicle['joint_carbon_quintile_desirable'][respondent][desirable] = \
            float(len(data_pilot['vehicle'][data_pilot['vehicle'].co2_quintile == respondent][data_pilot['vehicle'].vehicle_desirable_future == desirable])) / len(data_pilot['vehicle'][data_pilot['vehicle'].co2_quintile == respondent])

#print(df_transition_matrix_vehicle_carbon.to_latex(caption='Matrix of opinions on the future of thermal vehicles depending on carbon footprint quintile'))

dict_vehicle['joint_km_quintile_desirable'] = pd.DataFrame(index=items_desirable_vehicle, columns=range(1,6), dtype=float)
for respondent in range(1,6):
    for desirable in items_desirable_vehicle:
        dict_vehicle['joint_km_quintile_desirable'][respondent][desirable] = \
            float(len(data_pilot['vehicle'][data_pilot['vehicle'].km_quintile == respondent][data_pilot['vehicle'].vehicle_desirable_future == desirable])) / len(data_pilot['vehicle'][data_pilot['vehicle'].km_quintile == respondent])

#print(df_transition_matrix_vehicle_km.to_latex(caption='Matrix of opinions on the future of thermal vehicles depending on number of km travelled quintile'))

dict_vehicle['joint_nb_vehicles_desirable'] = pd.DataFrame(index=items_desirable_vehicle, columns=items_number_vehicles, dtype=float)
for respondent in items_number_vehicles:
    for desirable in items_desirable_vehicle:
        dict_vehicle['joint_nb_vehicles_desirable'][respondent][desirable] = \
            float(len(data_pilot['vehicle'][data_pilot['vehicle'].nb_vehicles == respondent][data_pilot['vehicle'].vehicle_desirable_future == desirable])) / len(data_pilot['vehicle'][data_pilot['vehicle'].nb_vehicles == respondent])

#print(df_transition_matrix_vehicle_number.to_latex(caption='Matrix of opinions on the future of thermal vehicles depending on vehicle ownership'))

dict_vehicle['joint_electric_hybrid_desirable'] = pd.DataFrame(index=items_desirable_vehicle, columns=[0,1], dtype=float)
for respondent in [0,1]:
    for desirable in items_desirable_vehicle:
        dict_vehicle['joint_electric_hybrid_desirable'][respondent][desirable] = \
            float(len(data_pilot['vehicle'][data_pilot['vehicle'].electric_or_hybrid_dummy == respondent][data_pilot['vehicle'].vehicle_desirable_future == desirable])) / len(data_pilot['vehicle'][data_pilot['vehicle'].electric_or_hybrid_dummy == respondent])

del items_number_vehicles, items_desirable_vehicle, item, respondent, desirable

##### Vaccine
items_respondents_vaccine = [u'Oui, j\'ai déjà reçu deux injections', u'Oui, j\'ai reçu la première injection',
                            u'Non, mais j\'ai déjà mon rendez-vous pour la première injection',
                            u'Non, mais je compte le faire à un moment donné', u'Non, le vaccin m\'est déconseillé pour des raisons personnelles',
                            u'Non, je ne souhaite pas être vacciné', u'Je préfère ne pas répondre à cette question']
items_desirable_vaccine = [u'tous les Français se fassent vacciner à partir de 12 ans', u'tous les Français se fassent vacciner à partir de 18 ans',
                          u'seules les personnes à risque se fassent vacciner', u'les Français évitent de se faire vacciner',
                          u'chacun décide de se faire vacciner en fonction de ses propres opinions et facteurs de risque',
                          u'NSP (Ne sait pas, ne se prononce pas).']

dict_vaccine = {}
dict_vaccine['respondents_status'] = pd.DataFrame(index=items_respondents_vaccine, columns=['result'])
for item in items_respondents_vaccine:
    dict_vaccine['respondents_status']['result'][item] = float(len(data_pilot['vaccine'][data_pilot['vaccine'].vaccine_respondent == item])) / len(data_pilot['vaccine'])

dict_vaccine['desirable_policy'] = pd.DataFrame(index=items_desirable_vaccine, columns=['result'])
for item in items_desirable_vaccine:
    dict_vaccine['desirable_policy']['result'][item] = float(len(data_pilot['vaccine'][data_pilot['vaccine'].vaccine_desirable == item])) / len(data_pilot['vaccine'])

dict_vaccine['joint_respondent_desirable'] = pd.DataFrame(index=items_desirable_vaccine, columns=items_respondents_vaccine, dtype=float)
for respondent in items_respondents_vaccine:
    for desirable in items_desirable_vaccine:
        dict_vaccine['joint_respondent_desirable'][respondent][desirable] = \
            float(len(data_pilot['vaccine'][data_pilot['vaccine'].vaccine_respondent == respondent][data_pilot['vaccine'].vaccine_desirable == desirable])) / len(data_pilot['vaccine'][data_pilot['vaccine'].vaccine_respondent == respondent])

del items_respondents_vaccine, items_desirable_vaccine, item, respondent, desirable
#print(df_transition_matrix_vaccine.to_latex(caption='Matrix of opinions on covid vaccine'))

#TODO: updater codes latex / remettre les df en pourcentages


##### Matrix arguments
variables_survey = list(data_pilot['full'].columns)
items_matrix_respondent = [u'Pas du tout pertinent', u'Peu pertinent', u'NSP (Ne sait pas, ne se prononce pas)',
                           u'Assez pertinent', u'Très pertinent']
items_matrix_french = [u'Une très petite minorité', u'Une minorité', u'NSP (Ne sait pas, ne se prononce pas)',
                       u'La moitié', u'La majorité', u'La très grande majorité']

dict_matrices_arguments = {}
dict_matrices_arguments['respondents'] = {}
for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
    variables_topic = list()
    for var in variables_survey:
        if 'matrix_respondent_{}'.format(topic) in var and '_num' not in var:
            variables_topic.append(var)
    dict_matrices_arguments['respondents'][topic] = pd.DataFrame(index=variables_topic, columns=items_matrix_respondent, dtype=float)
    for var in variables_topic:
        for answer in items_matrix_respondent:
            dict_matrices_arguments['respondents'][topic][answer][var] = float(len(data_pilot['matrix_respondent'][data_pilot['matrix_respondent'][var] == answer])) / len(data_pilot['matrix_respondent'])

dict_matrices_arguments['french'] = {}
for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
    variables_topic = list()
    for var in variables_survey:
        if 'matrix_french_{}'.format(topic) in var and '_num' not in var:
            variables_topic.append(var)
    dict_matrices_arguments['french'][topic] = pd.DataFrame(index=variables_topic, columns=items_matrix_french, dtype=float)
    for var in variables_topic:
        for answer in items_matrix_french:
            dict_matrices_arguments['french'][topic][answer][var] = float(len(data_pilot['matrix_french'][data_pilot['matrix_french'][var] == answer])) / len(data_pilot['matrix_french'])

dict_matrices_arguments['çomparison_average_score'] = {}
for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
    variables_topic_respondent = list()
    variables_topic_french = list()
    for var in variables_survey:
        if 'matrix_respondent_{}'.format(topic) in var and '_num' in var:
            variables_topic_respondent.append(var)
        elif 'matrix_french_{}'.format(topic) in var and '_num' in var:
            variables_topic_french.append(var)
    variables_topic_joint = [var.replace('matrix_french_', '') for var in variables_topic_french]
    dict_matrices_arguments['çomparison_average_score'][topic] = \
        pd.DataFrame(index=variables_topic_joint,
            columns=['score_respondents', 'score_french', 'difference', 'opposite_sign'],
            dtype=float)
    for var in variables_topic_joint:
        dict_matrices_arguments['çomparison_average_score'][topic]['score_respondents'][var] = data_pilot['matrix_respondent']['matrix_respondent_'+var].mean()
        dict_matrices_arguments['çomparison_average_score'][topic]['score_french'][var] = data_pilot['matrix_french']['matrix_french_'+var].mean()
        dict_matrices_arguments['çomparison_average_score'][topic]['difference'][var] = (
            dict_matrices_arguments['çomparison_average_score'][topic]['score_respondents'][var]
            - dict_matrices_arguments['çomparison_average_score'][topic]['score_french'][var]
            )
        dict_matrices_arguments['çomparison_average_score'][topic]['opposite_sign'][var] = (
            dict_matrices_arguments['çomparison_average_score'][topic]['score_respondents'][var]
            * dict_matrices_arguments['çomparison_average_score'][topic]['score_french'][var]
            ) < 0

del(items_matrix_respondent, items_matrix_french, variables_survey, variables_topic,
     variables_topic_joint, variables_topic_respondent, variables_topic_french, topic, var, answer)

arguments_pros = ['meat_animal_welfare_num', 'meat_global_warming_num', 'meat_cancer_num',
    'airtravel_global_warming_num', 'vehicle_air_pollution_num', 'vehicle_nuisance_city_num',
    'vaccine_protecting_others_num', 'vaccine_economic_activity_num']
arguments_cons = ['meat_farmers_precarity_num', 'meat_natural_num', 'meat_nutrients_num',
    'airtravel_freerider_num', 'airtravel_open_mindedness_num', 'airtravel_against_progress_num',
    'vehicle_small_share_cc_num', 'vehicle_batteries_num', 'vehicle_nuclear_num',
    'vaccine_imperfect_protecting_others_num', 'vaccine_taxes_industry_num', 'vaccine_poor_countries_num']

dict_matrices_arguments['pros_cons'] = pd.DataFrame(index=['meat', 'airtravel', 'vehicle', 'vaccine', 'all'],
    columns=['pros_respondents', 'cons_respondents', 'pros_french', 'cons_french'], dtype=float)
for item in ['pros', 'cons']:
    for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
        dict_matrices_arguments['pros_cons']['{}_respondents'.format(item)][topic] = 0
        dict_matrices_arguments['pros_cons']['{}_french'.format(item)][topic] = 0
        nb_topic = 0
        if item == 'pros':
            arguments = arguments_pros
        else:
            arguments = arguments_cons
        
        for var in arguments:
            if '{}'.format(topic) in var:
                nb_topic = nb_topic + 1
                dict_matrices_arguments['pros_cons']['{}_respondents'.format(item)][topic] = (
                    dict_matrices_arguments['pros_cons']['{}_respondents'.format(item)][topic]
                    + data_pilot['matrix_respondent']['matrix_respondent_'+var].mean()
                    )
                dict_matrices_arguments['pros_cons']['{}_french'.format(item)][topic] = (
                    dict_matrices_arguments['pros_cons']['{}_french'.format(item)][topic]
                    + data_pilot['matrix_french']['matrix_french_'+var].mean()
                    )
        dict_matrices_arguments['pros_cons']['{}_respondents'.format(item)][topic] = \
            dict_matrices_arguments['pros_cons']['{}_respondents'.format(item)][topic] / nb_topic
        dict_matrices_arguments['pros_cons']['{}_french'.format(item)][topic] = \
            dict_matrices_arguments['pros_cons']['{}_french'.format(item)][topic] / nb_topic
    
    dict_matrices_arguments['pros_cons']['{}_respondents'.format(item)]['all'] = 0
    dict_matrices_arguments['pros_cons']['{}_french'.format(item)]['all'] = 0
    if item == 'pros':
        arguments = arguments_pros
    else:
        arguments = arguments_cons
    
    for var in arguments:
        dict_matrices_arguments['pros_cons']['{}_respondents'.format(item)]['all'] = (
                    dict_matrices_arguments['pros_cons']['{}_respondents'.format(item)]['all']
                    + data_pilot['matrix_respondent']['matrix_respondent_'+var].mean()
                    ) / len(arguments)
        dict_matrices_arguments['pros_cons']['{}_french'.format(item)]['all'] = (
                    dict_matrices_arguments['pros_cons']['{}_french'.format(item)]['all']
                    + data_pilot['matrix_french']['matrix_french_'+var].mean()
                    ) / len(arguments)
    

# TODO: study arguments depending on people's position

### Meat


### Air travel


### Vehicle


### Vaccine
