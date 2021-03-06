  # -*- coding: utf-8 -*-


"""
This script produces descriptive statistics about the data collected from the
Qualtrics pilot survey on narratives and externalities.
The main outpout is a latex file that gathers many tables with descriptive statistics about the sample
"""

from __future__ import division


import pandas as pd
import re


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

data_pilot['labels'] = \
    pd.read_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_pilot_narratives_labels.csv', sep=',', index_col=0)


##### Survey key statictics
### Generalities
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

### Socio-demographics
dict_survey_statistics['socio_demographics'] = {}

dict_survey_statistics['socio_demographics']['sexe'] = {}
dict_survey_statistics['socio_demographics']['sexe']['F??minin'] = float(len(data_pilot['full'][data_pilot['full']['sexe']=='F??minin'])) / len(data_pilot['full'])
dict_survey_statistics['socio_demographics']['sexe']['Masculin'] = float(len(data_pilot['full'][data_pilot['full']['sexe']=='Masculin'])) / len(data_pilot['full'])

dict_survey_statistics['socio_demographics']['age_group'] = {}
for age in [u'18 ?? 24 ans', u'25 ?? 34 ans', u'35 ?? 49 ans', u'50 ?? 64 ans', u'65 ans ou plus']:
    dict_survey_statistics['socio_demographics']['age_group'][age] = \
        float(len(data_pilot['full'][data_pilot['full']['age_group']=='{}'.format(age)])) / len(data_pilot['full'])
del age

dict_survey_statistics['socio_demographics']['employment_status'] = {}
for status in [u'Fonctionnaire', u'CDI', u'CDD', u'Int??rimaire ou contrat pr??caire', u'Au ch??mage',
               u'??tudiant(e)', u'Retrait??(e)', u'Autre actif', u'Inactif']:
    dict_survey_statistics['socio_demographics']['employment_status'][status] = \
        float(len(data_pilot['full'][data_pilot['full']['employment_status']=='{}'.format(status)])) / len(data_pilot['full'])
del status

dict_survey_statistics['socio_demographics']['profession_type'] = {}
for profession in [u'Agriculteur/rice', u'Artisan, commer??ant(e), chef(fe) d\'entreprise', u'Cadre ou profession intellectuelle sup??rieure',
                   u'Profession interm??diaire', u'Employ??(e)', u'Ouvrier/??re', u'Retrait??(e)', u'Autre Inactif/ve']:
    dict_survey_statistics['socio_demographics']['profession_type'][profession] = \
        float(len(data_pilot['full'][data_pilot['full']['profession_type']=='{}'.format(profession)])) / len(data_pilot['full'])
del profession

dict_survey_statistics['socio_demographics']['diploma'] = {}
for diploma in [u'Aucun dipl??me', u'Brevet des coll??ges', u'CAP ou BEP', u'Baccalaur??at',
                u'Bac +2 (BTS, DUT, DEUG, ??coles de formation sanitaires et sociales...)', u'Bac +3 (licence...)',
                u'Bac +5 ou plus (master, ??cole d\'ing??nieur ou de commerce, doctorat, m??decine, ma??trise, DEA, DESS...)']:
    dict_survey_statistics['socio_demographics']['diploma'][diploma] = \
        float(len(data_pilot['full'][data_pilot['full']['diploma']=='{}'.format(diploma)])) / len(data_pilot['full'])
del diploma

for var in ['household_size', 'nb_above_14', 'income_respondent', 'income_household']:
    dict_survey_statistics['socio_demographics'][var] = {}
    dict_survey_statistics['socio_demographics'][var]['mean'] = data_pilot['full'][var].mean()
    for percentile in [10, 25, 50, 75, 90]:
        dict_survey_statistics['socio_demographics'][var]['percentile_'+str(percentile)] = \
             data_pilot['full'][var].quantile(percentile/100)
del percentile, var

### Ideology
dict_survey_statistics['ideology'] = {}

dict_survey_statistics['ideology']['trust_others'] = {}
dict_survey_statistics['ideology']['trust_others'][u'on peut faire confiance ?? la plupart des gens'] = \
    float(len(data_pilot['full'][data_pilot['full']['trust_others']==u'on peut faire confiance ?? la plupart des gens'])) / len(data_pilot['full'])
dict_survey_statistics['ideology']['trust_others'][u'on n???est jamais assez prudent quand on a affaire aux autres.'] = \
    float(len(data_pilot['full'][data_pilot['full']['trust_others']==u'on n???est jamais assez prudent quand on a affaire aux autres.'])) / len(data_pilot['full'])



dict_survey_statistics['ideology']['trust_government'] = {}
for answer in [u'Toujours', u'La plupart du temps', u'La moiti?? du temps', u'Parfois', u'Jamais', u'NSP (Ne sait pas, ne se prononce pas)']:
    dict_survey_statistics['ideology']['trust_government'][answer] = \
        float(len(data_pilot['full'][data_pilot['full']['trust_government']=='{}'.format(answer)])) / len(data_pilot['full'])
del answer

dict_survey_statistics['ideology']['life_satisfaction_scale'] = {}
dict_survey_statistics['ideology']['life_satisfaction_scale']['mean'] = data_pilot['full']['life_satisfaction_scale'].mean()
for percentile in [10, 25, 50, 75, 90]:
    dict_survey_statistics['ideology']['life_satisfaction_scale']['percentile_'+str(percentile)] = \
         data_pilot['full']['life_satisfaction_scale'].quantile(percentile/100)
del percentile

dict_survey_statistics['ideology']['political_leaning'] = {}
for answer in [u'D\'extr??me gauche', u'De gauche', u'Du centre', u'De droite', u'D\'extr??me droite',
               u'Conservateur', u'Lib??ral', u'Humaniste', u'Patriote', u'Apolitique', u'??cologiste',
               u'Je ne souhaite pas r??pondre / ne se prononce pas']:
    dict_survey_statistics['ideology']['political_leaning'][answer] = \
        float(len(data_pilot['full'][data_pilot['full']['political_leaning'].str.contains('{}'.format(answer))])) / len(data_pilot['full'])
del answer

dict_survey_statistics['ideology']['media_for_news'] = {}
for answer in [u'T??l??vision', u'Presse (??crite ou en ligne)', u'R??seaux sociaux', u'Radio', u'Autre']:
    dict_survey_statistics['ideology']['media_for_news'][answer] = \
        float(len(data_pilot['full'][data_pilot['full']['media_for_news']=='{}'.format(answer)])) / len(data_pilot['full'])
del answer

dict_survey_statistics['ideology']['social_networks_frequency'] = {}
for answer in [u'Tous les jours, pendant au moins une heure', u'Tous les jours, pendant moins d\'une heure',
               u'Presque tous les jours', u'De temps en temps', u'Jamais', u'NSP (Ne sait pas, ne se prononce pas)']:
    dict_survey_statistics['ideology']['social_networks_frequency'][answer] = \
        float(len(data_pilot['full'][data_pilot['full']['social_networks_frequency']=='{}'.format(answer)])) / len(data_pilot['full'])
del answer

### Science and climate change
dict_survey_statistics['cc_science'] = {}

dict_survey_statistics['cc_science']['cc_cause'] = {}
for answer in [u'n\'est pas une r??alit??', u'est principalement d?? ?? la variabilit?? naturelle du climat',
               u'est principalement d?? ?? l\'activit?? humaine', u'NSP (Ne sait pas, ne se prononce pas).']:
    dict_survey_statistics['cc_science']['cc_cause'][answer] = \
        float(len(data_pilot['full'][data_pilot['full']['cc_cause']=='{}'.format(answer)])) / len(data_pilot['full'])
del answer

dict_survey_statistics['cc_science']['cc_consequences'] = {}
for answer in [u'Insignifiants, voire b??n??fiques', u'Faibles, car les humains sauraient vivre avec',
               u'Graves, car il y aurait plus de catastrophes naturelles', u'D??sastreux, les modes de vie seraient largement alt??r??s',
               u'Cataclysmiques, l\'humanit?? dispara??trait', u'NSP (Ne sait pas, ne se prononce pas)']:
    dict_survey_statistics['cc_science']['cc_consequences'][answer] = \
        float(len(data_pilot['full'][data_pilot['full']['cc_consequences']=='{}'.format(answer)])) / len(data_pilot['full'])
del answer

dict_survey_statistics['cc_science']['cc_responsible'] = {}
for answer in [u'Chacun d\'entre nous', u'Les plus riches', u'Les gouvernements', u'Certains pays ??trangers',
               u'Les g??n??rations pass??es', u'Des causes naturelles']:
    dict_survey_statistics['cc_science']['cc_responsible'][answer] = \
        float(len(data_pilot['full'][data_pilot['full']['cc_responsible'].str.contains('{}'.format(answer))])) / len(data_pilot['full'])
del answer


dict_survey_statistics['cc_science']['trust_scientists'] = {}
for answer in [u'Oui, tout ?? fait', u'Oui, plut??t', u'Non, plut??t pas',
               u'Non, pas du tout', u'NSP (Ne sait pas, ne se prononce pas)']:
    dict_survey_statistics['cc_science']['trust_scientists'][answer] = \
        float(len(data_pilot['full'][data_pilot['full']['trust_scientists']=='{}'.format(answer)])) / len(data_pilot['full'])
del answer


##### Matrix arguments
variables_survey = list(data_pilot['full'].columns)
items_matrix_respondent = [u'Pas du tout pertinent', u'Peu pertinent', u'NSP (Ne sait pas, ne se prononce pas)',
                           u'Assez pertinent', u'Tr??s pertinent']
items_matrix_french = [u'Une tr??s petite minorit??', u'Une minorit??', u'NSP (Ne sait pas, ne se prononce pas)',
                       u'La moiti??', u'La majorit??', u'La tr??s grande majorit??']

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

dict_matrices_arguments['??omparison_average_score'] = {}
for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
    variables_topic_respondent = list()
    variables_topic_french = list()
    for var in variables_survey:
        if 'matrix_respondent_{}'.format(topic) in var and '_num' in var:
            variables_topic_respondent.append(var)
        elif 'matrix_french_{}'.format(topic) in var and '_num' in var:
            variables_topic_french.append(var)
    variables_topic_joint = [var.replace('matrix_french_', '') for var in variables_topic_french]
    dict_matrices_arguments['??omparison_average_score'][topic] = \
        pd.DataFrame(index=variables_topic_joint,
            columns=['score_respondents', 'score_french', 'difference', 'opposite_sign'],
            dtype=float)
    for var in variables_topic_joint:
        dict_matrices_arguments['??omparison_average_score'][topic]['score_respondents'][var] = data_pilot['matrix_respondent']['matrix_respondent_'+var].mean()
        dict_matrices_arguments['??omparison_average_score'][topic]['score_french'][var] = data_pilot['matrix_french']['matrix_french_'+var].mean()
        dict_matrices_arguments['??omparison_average_score'][topic]['difference'][var] = (
            dict_matrices_arguments['??omparison_average_score'][topic]['score_respondents'][var]
            - dict_matrices_arguments['??omparison_average_score'][topic]['score_french'][var]
            )
        dict_matrices_arguments['??omparison_average_score'][topic]['opposite_sign'][var] = (
            dict_matrices_arguments['??omparison_average_score'][topic]['score_respondents'][var]
            * dict_matrices_arguments['??omparison_average_score'][topic]['score_french'][var]
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

del item, nb_topic, topic, var


dict_topics = {}
##### Meat
items_respondents_meat = [u'Jamais', u'Tr??s occasionnellement', u'1 ?? 2 repas par semaine',
             u'3 ?? 5 repas par semaine', u'Environ un repas par jour', u'Presque ?? chaque repas']
items_desirable_meat = [u'jamais', u'tr??s occasionnellement', u'1 ?? 2 repas par semaine',
             u'3 ?? 5 repas par semaine', u'environ un repas par jour',
             u'presque ?? chaque repas', u'NSP (Ne sait pas, ne se prononce pas).']

dict_topics['meat'] = {}

### Opinions on meat
dict_topics['meat']['meat_frequency_respondent'] = pd.DataFrame(index=items_respondents_meat, columns=['result'])
for item in items_respondents_meat:
    dict_topics['meat']['meat_frequency_respondent']['result'][item] = float(len(data_pilot['meat'][data_pilot['meat'].meat_frequency_respondent == item])) / len(data_pilot['meat'])
    

dict_topics['meat']['meat_frequency_desirable'] = pd.DataFrame(index=items_desirable_meat, columns=['result'])
for item in items_desirable_meat:
    dict_topics['meat']['meat_frequency_desirable']['result'][item] = float(len(data_pilot['meat'][data_pilot['meat'].meat_frequency_desirable == item])) / len(data_pilot['meat'])

dict_topics['meat']['joint_own_desirable'] = pd.DataFrame(index=items_desirable_meat, columns=items_respondents_meat, dtype=float)
for respondent in items_respondents_meat:
    for desirable in items_desirable_meat:
        dict_topics['meat']['joint_own_desirable'][respondent][desirable] = \
            float(len(data_pilot['meat'][data_pilot['meat'].meat_frequency_respondent == respondent][data_pilot['meat'].meat_frequency_desirable == desirable])) / len(data_pilot['meat'][data_pilot['meat'].meat_frequency_respondent == respondent])

del desirable, item, respondent

### Opinions on arguments in matrices
for element in ['respondent', 'desirable']:
    if element == 'respondent':
        items_responses = items_respondents_meat
    else:
        items_responses = items_desirable_meat
    dict_topics['meat']['score_arguments_{}_frequency'.format(element)] = {}
    arguments = arguments_pros+arguments_cons
    for matrix in ['respondent', 'french']:
        dict_topics['meat']['score_arguments_{}_frequency'.format(element)]['{}_all'.format(matrix)] = pd.DataFrame(index = arguments,
                                                               columns = items_responses, dtype=float)
        for argument in arguments:
            for item in items_responses:
                dict_topics['meat']['score_arguments_{}_frequency'.format(element)]['{}_all'.format(matrix)][item][argument] = \
                    data_pilot['matrix_{}'.format(matrix)][data_pilot['matrix_{}'.format(matrix)]['meat_frequency_{}'.format(element)] == item]['matrix_{}_'.format(matrix)+argument].mean()
    
    for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
        arguments_topic = list()
        for argument in arguments:
            if '{}'.format(topic) in argument:
                arguments_topic.append(argument)            
        dict_topics['meat']['score_arguments_{}_frequency'.format(element)]['respondent_{}'.format(topic)] = dict_topics['meat']['score_arguments_{}_frequency'.format(element)]['respondent_all'].loc[arguments_topic]

del argument, arguments_topic, element, item, items_desirable_meat, items_respondents_meat, items_responses, matrix, topic


##### Air travel
items_respondents_airtravel = [u'Non, je ne le prend pas ou plus', u'Oui, moins d\'une fois par an',
                     u'Oui, environ une fois (aller-retour) par an', u'Oui, environ deux fois (aller-retour) par an',
                     u'Oui, plus de deux fois (aller-retour) par an']
items_desirable_airtravel = [u'jamais', u'au moins une fois dans leur vie',
                   u'environ une fois par an', u'plusieurs fois par an',
                   'le plus souvent possible', u'NSP (Ne sait pas, ne se prononce pas).']

dict_topics['airtravel'] = {}

### Opinions on air travel
dict_topics['airtravel']['airtravel_frequency_respondent'] = pd.DataFrame(index=items_respondents_airtravel, columns=['result'])
for item in items_respondents_airtravel:
    dict_topics['airtravel']['airtravel_frequency_respondent']['result'][item] = float(len(data_pilot['airtravel'][data_pilot['airtravel'].airtravel_frequency_respondent == item])) / len(data_pilot['airtravel'])

dict_topics['airtravel']['airtravel_frequency_desirable'] = pd.DataFrame(index=items_desirable_airtravel, columns=['result'])
for item in items_desirable_airtravel:
    dict_topics['airtravel']['airtravel_frequency_desirable']['result'][item] = float(len(data_pilot['airtravel'][data_pilot['airtravel'].airtravel_frequency_desirable == item])) / len(data_pilot['airtravel'])

dict_topics['airtravel']['joint_own_desirable'] = pd.DataFrame(index=items_desirable_airtravel, columns=items_respondents_airtravel, dtype=float)
for respondent in items_respondents_airtravel:
    for desirable in items_desirable_airtravel:
        dict_topics['airtravel']['joint_own_desirable'][respondent][desirable] = \
            float(len(data_pilot['airtravel'][data_pilot['airtravel'].airtravel_frequency_respondent == respondent][data_pilot['airtravel'].airtravel_frequency_desirable == desirable])) / len(data_pilot['airtravel'][data_pilot['airtravel'].airtravel_frequency_respondent == respondent])

del desirable, item, respondent

### Opinions on arguments in matrices
for element in ['respondent', 'desirable']:
    if element == 'respondent':
        items_responses = items_respondents_airtravel
    else:
        items_responses = items_desirable_airtravel
    dict_topics['airtravel']['score_arguments_{}_frequency'.format(element)] = {}
    arguments = arguments_pros+arguments_cons
    for matrix in ['respondent', 'french']:
        dict_topics['airtravel']['score_arguments_{}_frequency'.format(element)]['{}_all'.format(matrix)] = pd.DataFrame(index = arguments,
                                                               columns = items_responses, dtype=float)
        for argument in arguments:
            for item in items_responses:
                dict_topics['airtravel']['score_arguments_{}_frequency'.format(element)]['{}_all'.format(matrix)][item][argument] = \
                    data_pilot['matrix_{}'.format(matrix)][data_pilot['matrix_{}'.format(matrix)]['airtravel_frequency_{}'.format(element)] == item]['matrix_{}_'.format(matrix)+argument].mean()
    
    for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
        arguments_topic = list()
        for argument in arguments:
            if '{}'.format(topic) in argument:
                arguments_topic.append(argument)            
        dict_topics['airtravel']['score_arguments_{}_frequency'.format(element)]['respondent_{}'.format(topic)] = dict_topics['airtravel']['score_arguments_{}_frequency'.format(element)]['respondent_all'].loc[arguments_topic]

del argument, arguments_topic, element, item, items_desirable_airtravel, items_respondents_airtravel, items_responses, matrix, topic


##### Vehicles
dict_topics['vehicle'] = {}

items_number_vehicles = [u'Aucun', u'Un', u'Deux ou plus']
items_desirable_vehicle = [u'de cesser de les utiliser tr??s rapidement (d\'ici 2030 ou avant)', u'de cesser de les utiliser progressivement (d\'ici 2040 ou 2050)',
                           u'de cesser d\'utiliser les v??hicules diesel mais pas les v??hicule essence', u'de continuer ?? les utiliser tant que des progr??s majeurs ne sont pas fait vis-??-vis des v??hicules ??lectriques',
                           u'de continuer ?? les utiliser aussi longtemps que le p??trole est disponible', u'NSP (Ne sait pas, ne se prononce pas).']

### Opinions on vehicles
dict_topics['vehicle']['vehicle_desirable_future'] = pd.DataFrame(index=items_desirable_vehicle, columns=['result'], dtype=float)
for item in items_desirable_vehicle:
    dict_topics['vehicle']['vehicle_desirable_future']['result'][item] = float(len(data_pilot['vehicle'][data_pilot['vehicle'].vehicle_desirable_future == item])) / len(data_pilot['vehicle'])

dict_topics['vehicle']['joint_carbon_quintile_desirable'] = pd.DataFrame(index=items_desirable_vehicle, columns=range(1,6), dtype=float)
for respondent in range(1,6):
    for desirable in items_desirable_vehicle:
        dict_topics['vehicle']['joint_carbon_quintile_desirable'][respondent][desirable] = \
            float(len(data_pilot['vehicle'][data_pilot['vehicle'].co2_quintile == respondent][data_pilot['vehicle'].vehicle_desirable_future == desirable])) / len(data_pilot['vehicle'][data_pilot['vehicle'].co2_quintile == respondent])

dict_topics['vehicle']['joint_km_quintile_desirable'] = pd.DataFrame(index=items_desirable_vehicle, columns=range(1,6), dtype=float)
for respondent in range(1,6):
    for desirable in items_desirable_vehicle:
        dict_topics['vehicle']['joint_km_quintile_desirable'][respondent][desirable] = \
            float(len(data_pilot['vehicle'][data_pilot['vehicle'].km_quintile == respondent][data_pilot['vehicle'].vehicle_desirable_future == desirable])) / len(data_pilot['vehicle'][data_pilot['vehicle'].km_quintile == respondent])

dict_topics['vehicle']['joint_nb_vehicles_desirable'] = pd.DataFrame(index=items_desirable_vehicle, columns=items_number_vehicles, dtype=float)
for respondent in items_number_vehicles:
    for desirable in items_desirable_vehicle:
        dict_topics['vehicle']['joint_nb_vehicles_desirable'][respondent][desirable] = \
            float(len(data_pilot['vehicle'][data_pilot['vehicle'].nb_vehicles == respondent][data_pilot['vehicle'].vehicle_desirable_future == desirable])) / len(data_pilot['vehicle'][data_pilot['vehicle'].nb_vehicles == respondent])

dict_topics['vehicle']['joint_electric_hybrid_desirable'] = pd.DataFrame(index=items_desirable_vehicle, columns=[0,1], dtype=float)
for respondent in [0,1]:
    for desirable in items_desirable_vehicle:
        dict_topics['vehicle']['joint_electric_hybrid_desirable'][respondent][desirable] = \
            float(len(data_pilot['vehicle'][data_pilot['vehicle'].electric_or_hybrid_dummy == respondent][data_pilot['vehicle'].vehicle_desirable_future == desirable])) / len(data_pilot['vehicle'][data_pilot['vehicle'].electric_or_hybrid_dummy == respondent])

del desirable, item, respondent

### Opinions on arguments in matrices

for element in ['co2_quintile', 'nb_vehicles', 'vehicle_desirable_future']:
    if element == 'co2_quintile':
        items_responses = range(1,6)
    elif element == 'nb_vehicles':
        items_responses = items_number_vehicles
    else:
        items_responses = items_desirable_vehicle
    dict_topics['vehicle']['score_arguments_{}'.format(element)] = {}
    arguments = arguments_pros+arguments_cons
    for matrix in ['respondent', 'french']:
        dict_topics['vehicle']['score_arguments_{}'.format(element)]['{}_all'.format(matrix)] = pd.DataFrame(index = arguments,
                                                               columns = items_responses, dtype=float)
        for argument in arguments:
            for item in items_responses:
                dict_topics['vehicle']['score_arguments_{}'.format(element)]['{}_all'.format(matrix)][item][argument] = \
                    data_pilot['matrix_{}'.format(matrix)][data_pilot['matrix_{}'.format(matrix)]['{}'.format(element)] == item]['matrix_{}_'.format(matrix)+argument].mean()
    
    for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
        arguments_topic = list()
        for argument in arguments:
            if '{}'.format(topic) in argument:
                arguments_topic.append(argument)            
        dict_topics['vehicle']['score_arguments_{}'.format(element)]['respondent_{}'.format(topic)] = dict_topics['vehicle']['score_arguments_{}'.format(element)]['respondent_all'].loc[arguments_topic]

del argument, arguments_topic, element, item, items_desirable_vehicle, items_number_vehicles, items_responses, matrix, topic


##### Vaccine
items_respondents_vaccine = [u'Oui, j\'ai d??j?? re??u deux injections', u'Oui, j\'ai re??u la premi??re injection',
                            u'Non, mais j\'ai d??j?? mon rendez-vous pour la premi??re injection',
                            u'Non, mais je compte le faire ?? un moment donn??', u'Non, le vaccin m\'est d??conseill?? pour des raisons personnelles',
                            u'Non, je ne souhaite pas ??tre vaccin??', u'Je pr??f??re ne pas r??pondre ?? cette question']
items_desirable_vaccine = [u'tous les Fran??ais se fassent vacciner ?? partir de 12 ans', u'tous les Fran??ais se fassent vacciner ?? partir de 18 ans',
                          u'seules les personnes ?? risque se fassent vacciner', u'les Fran??ais ??vitent de se faire vacciner',
                          u'chacun d??cide de se faire vacciner en fonction de ses propres opinions et facteurs de risque',
                          u'NSP (Ne sait pas, ne se prononce pas).']

dict_topics['vaccine'] = {}

### Opinions on vaccine
dict_topics['vaccine']['vaccine_respondent'] = pd.DataFrame(index=items_respondents_vaccine, columns=['result'])
for item in items_respondents_vaccine:
    dict_topics['vaccine']['vaccine_respondent']['result'][item] = float(len(data_pilot['vaccine'][data_pilot['vaccine'].vaccine_respondent == item])) / len(data_pilot['vaccine'])

dict_topics['vaccine']['vaccine_desirable'] = pd.DataFrame(index=items_desirable_vaccine, columns=['result'])
for item in items_desirable_vaccine:
    dict_topics['vaccine']['vaccine_desirable']['result'][item] = float(len(data_pilot['vaccine'][data_pilot['vaccine'].vaccine_desirable == item])) / len(data_pilot['vaccine'])

dict_topics['vaccine']['joint_own_desirable'] = pd.DataFrame(index=items_desirable_vaccine, columns=items_respondents_vaccine, dtype=float)
for respondent in items_respondents_vaccine:
    for desirable in items_desirable_vaccine:
        dict_topics['vaccine']['joint_own_desirable'][respondent][desirable] = \
            float(len(data_pilot['vaccine'][data_pilot['vaccine'].vaccine_respondent == respondent][data_pilot['vaccine'].vaccine_desirable == desirable])) / len(data_pilot['vaccine'][data_pilot['vaccine'].vaccine_respondent == respondent])

del desirable, item, respondent

### Opinions on arguments in matrices
for element in ['respondent', 'desirable']:
    if element == 'respondent':
        items_responses = items_respondents_vaccine
    else:
        items_responses = items_desirable_vaccine
    dict_topics['vaccine']['score_arguments_{}'.format(element)] = {}
    arguments = arguments_pros+arguments_cons
    for matrix in ['respondent', 'french']:
        dict_topics['vaccine']['score_arguments_{}'.format(element)]['{}_all'.format(matrix)] = pd.DataFrame(index = arguments,
                                                               columns = items_responses, dtype=float)
        for argument in arguments:
            for item in items_responses:
                dict_topics['vaccine']['score_arguments_{}'.format(element)]['{}_all'.format(matrix)][item][argument] = \
                    data_pilot['matrix_{}'.format(matrix)][data_pilot['matrix_{}'.format(matrix)]['vaccine_{}'.format(element)] == item]['matrix_{}_'.format(matrix)+argument].mean()
    
    for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
        arguments_topic = list()
        for argument in arguments:
            if '{}'.format(topic) in argument:
                arguments_topic.append(argument)            
        dict_topics['vaccine']['score_arguments_{}'.format(element)]['respondent_{}'.format(topic)] = dict_topics['vaccine']['score_arguments_{}'.format(element)]['respondent_all'].loc[arguments_topic]

del argument, arguments_topic, element, item, items_desirable_vaccine, items_respondents_vaccine, items_responses, matrix, topic


##### Generate Latex file with relevant tables for descriptive statistics
dict_latex_tables = {}

dict_variables = data_pilot['labels'].to_dict()

latex_file = open(r"C:\Users\TDOUENN\Documents\Projects\Narratives\Data\latex_template.txt").read()

### Sample characteristics
latex_file = latex_file.replace('\end{document}',
    '\\section{Respondents characteristics}' + '\n' + '\end{document}')


for theme in ['socio_demographics', 'ideology', 'cc_science']:
    dict_latex_tables[theme] = {}
    for question in dict_survey_statistics[theme]:
        title = dict_variables['Question_survey'][question]
        
        if sum(dict_survey_statistics[theme][question].values()) < 1+1e-03:
            float_format="{:.0%}".format
        elif sum(dict_survey_statistics[theme][question].values()) > 1+1e-03 and sum(dict_survey_statistics[theme][question].values()) < 100:
            float_format="{:.1f}".format
        else:
            float_format="{:.0f}".format
        
        dict_latex_tables[theme][question] = \
        pd.DataFrame.from_dict(dict_survey_statistics[theme][question], orient='index',
                           columns=['Percentage']).to_latex(
            caption='\"{}\"'.format(title),
            float_format=float_format,
            )

dict_latex_tables['full_tables'] = {}
for theme in ['socio_demographics', 'ideology', 'cc_science']:
    if theme == 'socio_demographics':
        section_title = '\subsection{Socio-demographic}'
    elif theme == 'ideology':
        section_title = '\subsection{Ideology}'
    elif theme == 'cc_science':
        section_title = '\subsection{Science and Climate Change}'

    dict_latex_tables['full_tables'][theme] = ''
    for question in dict_survey_statistics[theme]:
        dict_latex_tables['full_tables'][theme] = (
            dict_latex_tables['full_tables'][theme] + '\n' + dict_latex_tables[theme][question]
            )
    latex_file = latex_file.replace("\end{document}",
        '\\clearpage' + '\n' + '{}'.format(section_title) + '\n' + dict_latex_tables['full_tables'][theme] + '\n' + "\end{document}" )

del theme, question, section_title, title


### Respondents attitude and views on topics
latex_file = latex_file.replace('\end{document}',
    '\n' + '\\section{Attitudes and views on four topics}' + '\n' + '\end{document}')

for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
    dict_latex_tables[topic] = {}
dict_latex_tables['meat']['joint_own_desirable'] = dict_topics['meat']['joint_own_desirable'].to_latex(
    caption='Opinions about desirable meat consumption (raws) by own meat consumption (columns)',
    float_format="{:.0%}".format,
    column_format='p{3.0cm}|p{1.8cm}p{1.8cm}p{1.8cm}p{1.8cm}p{1.8cm}p{1.8cm}p{1.8cm}',
    )

dict_latex_tables['airtravel']['joint_own_desirable'] = dict_topics['airtravel']['joint_own_desirable'].to_latex(
    caption='Opinions about desirable air travel frequency (raws) by own air travel frequency (columns)',
    float_format="{:.0%}".format,
    column_format='p{5.0cm}|p{2.0cm}p{2.0cm}p{2.0cm}p{2.0cm}p{2.0cm}',
    )

dict_latex_tables['vehicle']['joint_carbon_quintile_desirable'] = dict_topics['vehicle']['joint_carbon_quintile_desirable'].to_latex(
    caption='Opinions about the future of thermal vehicles (raws) by CO2 quintile (columns)',
    float_format="{:.0%}".format,
    column_format='p{5.0cm}|p{2.0cm}p{2.0cm}p{2.0cm}p{2.0cm}p{2.0cm}',
    )
dict_latex_tables['vehicle']['joint_nb_vehicles_desirable'] = dict_topics['vehicle']['joint_nb_vehicles_desirable'].to_latex(
    caption='Opinions about the future of thermal vehicles (raws) by vehicle ownership (columns)',
    float_format="{:.0%}".format,
    column_format='p{9.0cm}|p{2.0cm}p{2.0cm}p{2.0cm}',
    )
dict_latex_tables['vehicle']['joint_own_desirable'] = (
    dict_latex_tables['vehicle']['joint_carbon_quintile_desirable'] + '\n'
    + dict_latex_tables['vehicle']['joint_nb_vehicles_desirable']
    )

dict_latex_tables['vaccine']['joint_own_desirable'] = dict_topics['vaccine']['joint_own_desirable'].to_latex(
    caption='Opinions about mandatory covid vaccination (raws) by own vaccination status (columns)',
    float_format="{:.0%}".format,
    column_format='p{3.0cm}|p{1.8cm}p{1.8cm}p{1.8cm}p{1.8cm}p{1.8cm}p{1.8cm}p{1.8cm}',
    )

del topic
    
for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
    dict_latex_tables['full_tables'][topic] = ''
    if topic == 'meat':
        questions = ['meat_frequency_respondent', 'meat_frequency_desirable']
        section_title = '\subsection{Meat}'
    elif topic == 'airtravel':
        questions = ['airtravel_frequency_respondent', 'airtravel_frequency_desirable']
        section_title = '\subsection{Air travel}'
    elif topic == 'vehicle':
        questions = ['vehicle_desirable_future']
        section_title = '\subsection{Vehicle}'
    elif topic == 'vaccine':
        questions = ['vaccine_respondent', 'vaccine_desirable']
        section_title = '\subsection{Vaccine}'

    for question in questions:        
        title = dict_variables['Question_survey'][question]
        dict_latex_tables[topic][question] = dict_topics[topic][question].to_latex(
            caption='\"{}\"'.format(title),
            float_format="{:.0%}".format,
            )
        dict_latex_tables['full_tables'][topic] = (
            dict_latex_tables['full_tables'][topic] + '\n' + dict_latex_tables[topic][question]
            )
    
    dict_latex_tables['full_tables'][topic] = (
        dict_latex_tables['full_tables'][topic] + '\n' + dict_latex_tables[topic]['joint_own_desirable']
        )
        
    latex_file = latex_file.replace("\end{document}",
        '\\clearpage' + '\n' + '{}'.format(section_title) + '\n' + dict_latex_tables['full_tables'][topic] + '\n' + "\end{document}" )
    
del topic, questions, question, section_title, title


##### Argument matrices
latex_file = latex_file.replace('\end{document}',
    '\n' + '\\section{Answers to arguments matrices}' + '\n' + '\end{document}')

for element in ['respondents', 'french']:
    if element == 'respondents':
        section_title = '\subsection{Respondents own views}'
        column_format='p{5.0cm}|p{2.1cm}p{2.1cm}p{2.1cm}p{2.1cm}p{2.1cm}'
        title = 'Parmi les arguments suivants, lesquels vous semblent pertinents ?'
    elif element == 'french':
        section_title = '\subsection{Beliefs about French people view}'
        column_format='p{5.0cm}|p{1.8cm}p{1.8cm}p{1.8cm}p{1.8cm}p{1.8cm}p{1.8cm}'
        title = 'D\'apr??s vous, quelle part des Fran??ais jugent pertinent chacun des arguments suivants ?'
    dict_latex_tables['matrices_' + element] = {}
    dict_latex_tables['full_tables']['matrices_' + element] = ''
    for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
        
        final_indexes = []
        current_indexes = dict_matrices_arguments[element][topic].index.tolist()
        new_indexes = [dict_variables['Question_survey'][item] for item in current_indexes]

        drop_before = " ? - "

        for i in new_indexes:
            final_i = re.sub(r'^.*?{}'.format(drop_before), '', i)
            final_indexes.append(final_i)
           
        dict_matrices_arguments[element][topic].index = final_indexes
        
        dict_latex_tables['matrices_' + element][topic] = dict_matrices_arguments[element][topic].to_latex(
            caption='\"{}\"'.format(title),
            column_format=column_format,
            float_format="{:.0%}".format,
            )

        dict_latex_tables['full_tables']['matrices_' + element] = (
            dict_latex_tables['full_tables']['matrices_' + element] + '\n' + dict_latex_tables['matrices_' + element][topic]
            )
        
    latex_file = latex_file.replace("\end{document}",
        '\\clearpage' + '\n' + '{}'.format(section_title) + '\n' + dict_latex_tables['full_tables']['matrices_' + element] + '\n' + "\end{document}" )
        
latex_file = latex_file.replace("begin{table}", "begin{table}[h!]")

del topic, element, title, section_title, i, drop_before, final_indexes, new_indexes, current_indexes, final_i

# TODO: check if there is a way to create sections in the script
