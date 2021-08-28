  # -*- coding: utf-8 -*-


"""
This script ...
"""

from __future__ import division


import pandas as pd

##### Read data from Qualtrics
data_pilot = {}

data_pilot['full'] = \
    pd.read_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_pilot_narratives_prepared.csv', sep=',', index_col=0)

data_pilot['meat'] = data_pilot['full'].query('topic_meat == 1').copy()
data_pilot['airtravel'] = data_pilot['full'].query('topic_airtravel == 1').copy()
data_pilot['vehicle'] = data_pilot['full'].query('topic_vehicle == 1').copy()
data_pilot['vaccine'] = data_pilot['full'].query('topic_vaccine == 1').copy()

##### End of survey box
answers_open_end_box = data_pilot['full']['open_box_end'].dropna()
answers_open_end_box.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\open_end_box.csv',
                            sep=';', encoding='utf-8-sig', index=True)

### Meat
answers_meat_why_against_open = data_pilot['meat']['meat_why_against_open'].dropna()
answers_meat_why_against_open.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Meat\meat_why_against.csv',
                            sep=';', encoding='utf-8-sig', index=True)

answers_meat_why_favorable_open = data_pilot['meat']['meat_why_favorable_open'].dropna()
answers_meat_why_favorable_open.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Meat\meat_why_favorable.csv',
                            sep=';', encoding='utf-8-sig', index=True)

answers_meat_why_neutral_open = data_pilot['meat']['meat_why_neutral_open'].dropna()
answers_meat_why_neutral_open.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Meat\meat_why_neutral.csv',
                            sep=';', encoding='utf-8-sig', index=True)

answers_meat_landscape_argument_open = data_pilot['meat']['meat_landscape_argument_open'].dropna()
answers_meat_landscape_argument_open.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Meat\meat_landscape_argument.csv',
                            sep=';', encoding='utf-8-sig', index=True)

answers_meat_carbon_argument_open = data_pilot['meat']['meat_carbon_argument_open'].dropna()
answers_meat_carbon_argument_open.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Meat\meat_carbon_argument.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_tags_meat = {}
dict_tags_meat['why_against'] = {
    'Health': [8,17,34,50,62,88,95,128,196,207,211,305,344,357,380,398,449,537,550,606,703,
               719,821,838,992,2833,3236,3237],
    'Cancer': [128, 380, 992],
    'Cardiovascular_diseases': [606],
    'Unnecessary_health': [34,95,207,313,380,397,719],
    'Varied_diet': [17,80,334],
    'Animal_welfare': [62,246,294,344,357,537,1273,2833],
    'Environment': [211,246,357,493,512,537,902,929,3236],
    'Quality': [170],
    'Opposite_argument': [],
    'Dont_know': [269],
    'Unclear_undetermined': [57,100,228,453],
    }

dict_tags_meat['why_favorable'] = {
    'Health': [19,28,42,43,52,64,78,97,110,112,118,123,133, 146,152,154,166,188,197,205,212,216,242,248,
               250,255,271,278,302,330,347,351,375,400,409,410,418,424,428,475,485,520,548,651,655,725,
               765,781,892,1177,1214,1355,2463,3221,3242,3346],
    'Varied_diet': [14,78,152,262,271,280,286,311,359,400,
                    651,667],
    'Proteins': [19,42,43,64,72,112,152,197,205,212,216,242,255,271,302,330,347,409,424,428,520,725,
                 1355,2463,3221],
    'Nutrients': [28,52,154],
    'Irons': [146,166,242,485,1177],
    'Vitamines': [97,146,166,278,465,3346],
    'Natural': [217],
    'Taste': [43,218,261,271,311,1355,3297],
    'Farmers': [90,271,274,339,345,351,424],
    'Landscape': [339],
    'Animal_future': [651],
    'Tradition_habit': [166,315,495,667,1355],
    'Economy': [118,271,274],
    'Environment': [29,117,188,339,877],
    'Price': [968],
    'Opposite_argument': [29,117,188,360,368,465,877],
    'Dont_know': [103,317,406,412,906,1161],
    'Unclear_undetermined': [139,140,204,226,239,368,532,579,620,877,968,976,3301],
    }

dict_tags_meat['why_neutral'] = {
    'Free_choice': [180,303],
    'Health': [490],
    'Animal_welfare': [708],
    'Environment': [186],
    'Nutrients': [490],
    'Taste': [180],
    'Farmers': [708],
    'Economy': [708],
    'Price': [490],
    'Dont_know': [181,1097],
    'Unclear_undetermined': [23,436],
    }

dict_tags_meat['landscape_argument'] = {
    'Agree': [8,17,50,57,88,181,186,303,344,357,398,490,537,606,902,929,1097,3236,3237],
    'Not_fully_agree': [34,95,100,449,493,719],
    'Possible_reconversion_farmers': [344],
    'Not_true': [80,128,170,305,334,512,1273,2833],
    'Unlikely_impossible_scenario': [170,180,207,211,380,397,708,838],
    'Would_reduce_intensive_farming': [207,294],
    'Stupid_argument': [80,246,334,703],
    'Dont_know': [62,100,269,436,821],
    'Unclear_undetermined': [8,17,23,180,196,228,313,398,453,550,719,992],
    }

dict_tags_meat['carbon_footprint_argument'] = {
    'Agree': [19,28,29,42,97,123,140,154,188,212,217,218,278,302,315,317,339,428,465,475,485,725,765,877,2463,3297,3301],
    'It_depends': [28,78,112,139,262,330,400,1355,3346],
    'Uncertain': [97,123,146,152,204,242,271,347,351,360,475,725],
    'Other_things_pollute_more': [14,118,1161],
    'Vegetables_also_pollute': [28,90,112,118,139,140,146,330,400,424,3301],
    'Local_production_vs_imports': [28,140,146,262,410,1355],
    'Not_all_meat_pollutes': [28,64,78,217,262],
    'Intensive_production_responsible': [64,78,262,651],
    'Not_true': [64,90,117,118,133,239,248,250,261,274,368,406,409,418,424,495,532,548,976,1355,3221,3242,3346],
    'Unrelated_opposite_argument': [118,216,347,375,410,620,1214],
    'Agressive_answer': [118,197,205,250,261,351,360,548,655,3221],
    'Dont_care': [205,278,315,345,475,655],
    'Dont_know': [43,97,103,110,133,166,255,274,311,359,412,520,667,781,892,906],
    'Unclear_undetermined': [72,226,280,375,579,620,968],
    }

data_pilot['meat']['asked_why_against'] = (
    1*(data_pilot['meat']['meat_frequency_desirable'] == 'jamais')
    + 1*(data_pilot['meat']['meat_frequency_desirable'] == u'très occasionnellement')
    + 1*(data_pilot['meat']['meat_frequency_desirable'] == '1 à 2 repas par semaine')
    )
data_pilot['meat']['asked_why_neutral'] = (
    1*(data_pilot['meat']['meat_frequency_desirable'] == u'NSP (Ne sait pas, ne se prononce pas).')
    )
data_pilot['meat']['asked_why_favorable'] = (
    1 - data_pilot['meat']['asked_why_against'] - data_pilot['meat']['asked_why_neutral']
    )
data_pilot['meat']['asked_landscape_argument'] = (
    data_pilot['meat']['asked_why_against'] + data_pilot['meat']['asked_why_neutral']
    )
data_pilot['meat']['asked_carbon_footrpint_argument'] = data_pilot['meat']['asked_why_favorable']


data_pilot['meat']['tags_answer_why_against'] = ''
for element in dict_tags_meat['why_against'].keys():
    data_pilot['meat'].loc[dict_tags_meat['why_against'][element],'tags_answer_why_against'] = \
        element + ';' + data_pilot['meat'].loc[dict_tags_meat['why_against'][element],'tags_answer_why_against']

data_pilot['meat']['tags_answer_why_neutral'] = ''
for element in dict_tags_meat['why_neutral'].keys():
    data_pilot['meat'].loc[dict_tags_meat['why_neutral'][element],'tags_answer_why_neutral'] = \
        element + ';' + data_pilot['meat'].loc[dict_tags_meat['why_neutral'][element],'tags_answer_why_neutral']

data_pilot['meat']['tags_answer_why_favorable'] = ''
for element in dict_tags_meat['why_favorable'].keys():
    data_pilot['meat'].loc[dict_tags_meat['why_favorable'][element],'tags_answer_why_favorable'] = \
        element + ';' + data_pilot['meat'].loc[dict_tags_meat['why_favorable'][element],'tags_answer_why_favorable']

data_pilot['meat']['tags_answer_landscape_argument'] = ''
for element in dict_tags_meat['landscape_argument'].keys():
    data_pilot['meat'].loc[dict_tags_meat['landscape_argument'][element],'tags_answer_landscape_argument'] = \
        element + ';' + data_pilot['meat'].loc[dict_tags_meat['landscape_argument'][element],'tags_answer_landscape_argument']

data_pilot['meat']['tags_answer_carbon_footprint_argument'] = ''
for element in dict_tags_meat['carbon_footprint_argument'].keys():
    data_pilot['meat'].loc[dict_tags_meat['carbon_footprint_argument'][element],'tags_answer_carbon_footprint_argument'] = \
        element + ';' + data_pilot['meat'].loc[dict_tags_meat['carbon_footprint_argument'][element],'tags_answer_carbon_footprint_argument']


##### Air travel
answers_airtravel_why_against_open = data_pilot['airtravel']['airtravel_why_against_open'].dropna()
answers_airtravel_why_against_open.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Airtravel\airtravel_why_against.csv',
                            sep=';', encoding='utf-8-sig', index=True)

answers_airtravel_why_favorable_open = data_pilot['airtravel']['airtravel_why_favorable_open'].dropna()
answers_airtravel_why_favorable_open.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Airtravel\airtravel_why_favorable.csv',
                            sep=';', encoding='utf-8-sig', index=True)

answers_airtravel_why_neutral_open = data_pilot['airtravel']['airtravel_why_neutral_open'].dropna()
answers_airtravel_why_neutral_open.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Airtravel\airtravel_why_neutral.csv',
                            sep=';', encoding='utf-8-sig', index=True)

answers_airtravel_open_mindedness_argument_open = data_pilot['airtravel']['airtravel_open_mindedness_argument_open'].dropna()
answers_airtravel_open_mindedness_argument_open.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Airtravel\airtravel_open_mindedness_argument.csv',
                            sep=';', encoding='utf-8-sig', index=True)

answers_airtravel_carbon_argument_open = data_pilot['airtravel']['airtravel_carbon_argument_open'].dropna()
answers_airtravel_carbon_argument_open.to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Airtravel\airtravel_carbon_argument.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_tags_airtravel = {}
dict_tags_airtravel['why_against'] = {
    'Pollution': [12,16,25,26,41,86,124,142,147,165,171,178,184,214,215,
                  270,291,312,318,361,367,378,390,392,425,431,484,503,508,
                  527,544,653,715,903,1227,3285,3762],
    'Virus_spreading': [12,297,322],
    'Noise': [378],
    'Price_expensive': [104,343,419,433,461,653,824],
    'Better_alternatives_exist': [104,178,247,392,425,670,715,3285],
    'Not_always_convenient': [247,419,460],
    'Risky': [],
    'Opposite_argument': [288,318,408,546,698,965],
    'Dont_know': [3775],
    'Unclear_undetermined': [126,252,322,386,442,3224,3775],
    }

dict_tags_airtravel['why_favorable'] = {
    'Discover_the_world': [44,66,108,153,200,225,229,374,389,420,971,1278],
    'To_go_everywhere': [51,63,66,225,229,335,374,389,420,971,1278],
    'Quicker': [51,63,79,107,114,119,136,175,233,235,254,279,783,971,1101],
    'Convenient': [79,107,114,138,971,1101,1278],
    'Economy': [98,420,481],
    'Evasion': [108,430,438,577,3239],
    'Safer': [114,783],
    'Price_cheap': [119,138],
    'Pollutes_less': [198,235,326,358],
    'Less_road_traffic': [],
    'Politicians_wealthy_do_it': [349],
    'Opposite_argument': [229,301,335,971],
    'Dont_know': [260],
    'Unclear_undetermined': [160,198,258,358,737,1200],
    }

dict_tags_airtravel['why_neutral'] = {
    'Pollution': [22,83,89,287,310,385,509,636,675,732,856,896,939,2706,3231,3235],
    'Virus_spreading': [201],
    'Noise': [],
    'Price_expensive': [104,343,419,433,461,653,824]+[983,1175],
    'Better_alternatives_exist': [],
    'Not_always_convenient': [287,332,432],
    'Risky': [74],
    'Discover_the_world': [69,597],
    'To_go_everywhere': [53,69,287,636,732,896],
    'Quicker': [74,287,385,432,636,697,896,983,3231],
    'Convenient': [332,597,732],
    'Economy': [636,843],
    'Evasion': [597],
    'Safer': [],
    'Pollutes_less': [22],
    'Less_road_traffic': [675,939,1175],
    'Politicians_wealthy_do_it': [407],
    'Dont_know': [192,224,231,346,364,3282],
    'Unclear_undetermined': [3238],
    }

dict_tags_airtravel['open_mindedness_argument'] = {
    'Agree': [16,22,25,26,41,69,86,89,94,104,124,142,147,165,171,184,185,201,
              214,215,224,231,247,252,270,288,291,310,318,332,343,361,364,367,
              385,386,390,392,407,408,419,425,432,433,452,460,461,471,484,503,
              508,509,527,546,636,653,670,675,697,698,715,732,824,843,856,896,
              903,939,965,983,1175,1227,3224,3231,3235,3282,3285,3775],
    'Not_true': [53,74,83,178,192,312,322,346,378],
    'It_depends': [12,41,392,460,670,843,2706,3231,3235],
    'Uncertain': [322,346,732],
    'Other_modes_also_do_it': [12,53,178,231,378,431,843,3762],
    'Can_travel_differently': [83,270,312,670],
    'Unrelated_opposite_argument': [86,104,201,322,432,544,597],
    'Dont_know': [],
    'Unclear_undetermined': [94,126,442,3238],
    }

dict_tags_airtravel['carbon_footprint_argument'] = {
    'Agree': [63,66,98,107,108,119,136,153,160,254,279,301,335,389,420,577,783,971],
    'Not_true': [51,138,175,198,200,233,235,358,374,3239],
    'It_depends': [51,79,136,160,326,737,783],
    'Uncertain': [114,233,430,438],
    'Other_things_pollute_more': [44,258,349],
    'Unrelated_opposite_argument': [349,420,1278],
    'Dont_know': [225,229,260,1101],
    'Unclear_undetermined': [79,258,1200],
    }


data_pilot['airtravel']['tags_answer_why_against'] = ''
for element in dict_tags_airtravel['why_against'].keys():
    data_pilot['airtravel'].loc[dict_tags_airtravel['why_against'][element],'tags_answer_why_against'] = \
        element + ';' + data_pilot['airtravel'].loc[dict_tags_airtravel['why_against'][element],'tags_answer_why_against']

data_pilot['airtravel']['tags_answer_why_neutral'] = ''
for element in dict_tags_airtravel['why_neutral'].keys():
    data_pilot['airtravel'].loc[dict_tags_airtravel['why_neutral'][element],'tags_answer_why_neutral'] = \
        element + ';' + data_pilot['airtravel'].loc[dict_tags_airtravel['why_neutral'][element],'tags_answer_why_neutral']

data_pilot['airtravel']['tags_answer_why_favorable'] = ''
for element in dict_tags_airtravel['why_favorable'].keys():
    data_pilot['airtravel'].loc[dict_tags_airtravel['why_favorable'][element],'tags_answer_why_favorable'] = \
        element + ';' + data_pilot['airtravel'].loc[dict_tags_airtravel['why_favorable'][element],'tags_answer_why_favorable']

data_pilot['airtravel']['tags_answer_open_mindedness_argument'] = ''
for element in dict_tags_airtravel['open_mindedness_argument'].keys():
    data_pilot['airtravel'].loc[dict_tags_airtravel['open_mindedness_argument'][element],'tags_answer_open_mindedness_argument'] = \
        element + ';' + data_pilot['airtravel'].loc[dict_tags_airtravel['open_mindedness_argument'][element],'tags_answer_open_mindedness_argument']

data_pilot['airtravel']['tags_answer_carbon_footprint_argument'] = ''
for element in dict_tags_airtravel['carbon_footprint_argument'].keys():
    data_pilot['airtravel'].loc[dict_tags_airtravel['carbon_footprint_argument'][element],'tags_answer_carbon_footprint_argument'] = \
        element + ';' + data_pilot['airtravel'].loc[dict_tags_airtravel['carbon_footprint_argument'][element],'tags_answer_carbon_footprint_argument']





# TODO: count the share of answered
# Do some stats over tags
# Display most common words
