  # -*- coding: utf-8 -*-


"""
This script analyzes the answers to open-ended questions from the
Qualtrics pilot survey on narratives and externalities
"""


from __future__ import division


import pandas as pd

##### Read data
data_pilot = {}

data_pilot['full'] = \
    pd.read_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_pilot_narratives_prepared.csv', sep=',', index_col=0)

data_pilot['meat'] = data_pilot['full'].query('topic_meat == 1').copy()
data_pilot['airtravel'] = data_pilot['full'].query('topic_airtravel == 1').copy()
data_pilot['vehicle'] = data_pilot['full'].query('topic_vehicle == 1').copy()
data_pilot['vaccine'] = data_pilot['full'].query('topic_vaccine == 1').copy()

##### End of survey box
dict_full_answers = {}
dict_full_answers['open_end_box'] = data_pilot['full']['end_of_survey_box'].dropna()
dict_full_answers['open_end_box'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\open_end_box.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_tags = {}
### Meat
dict_full_answers['meat'] = {}
dict_full_answers['meat']['why_against_open'] = data_pilot['meat']['meat_why_against_open'].dropna()
dict_full_answers['meat']['why_against_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Meat\meat_why_against.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['meat']['why_favorable_open'] = data_pilot['meat']['meat_why_favorable_open'].dropna()
dict_full_answers['meat']['why_favorable_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Meat\meat_why_favorable.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['meat']['why_neutral_open'] = data_pilot['meat']['meat_why_neutral_open'].dropna()
dict_full_answers['meat']['why_neutral_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Meat\meat_why_neutral.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['meat']['landscape_argument_open'] = data_pilot['meat']['meat_landscape_argument_open'].dropna()
dict_full_answers['meat']['landscape_argument_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Meat\meat_landscape_argument.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['meat']['carbon_footprint_argument_open'] = data_pilot['meat']['meat_carbon_footprint_argument_open'].dropna()
dict_full_answers['meat']['carbon_footprint_argument_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Meat\meat_carbon_footprint_argument.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_tags['meat'] = {}
dict_tags['meat']['why_against'] = {
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

dict_tags['meat']['why_favorable'] = {
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

dict_tags['meat']['why_neutral'] = {
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

dict_tags['meat']['landscape_argument'] = {
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

dict_tags['meat']['carbon_footprint_argument'] = {
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

data_pilot['meat']['tags_answer_why_against'] = ''
for element in dict_tags['meat']['why_against'].keys():
    data_pilot['meat'].loc[dict_tags['meat']['why_against'][element],'tags_answer_why_against'] = \
        element + ';' + data_pilot['meat'].loc[dict_tags['meat']['why_against'][element],'tags_answer_why_against']

data_pilot['meat']['tags_answer_why_neutral'] = ''
for element in dict_tags['meat']['why_neutral'].keys():
    data_pilot['meat'].loc[dict_tags['meat']['why_neutral'][element],'tags_answer_why_neutral'] = \
        element + ';' + data_pilot['meat'].loc[dict_tags['meat']['why_neutral'][element],'tags_answer_why_neutral']

data_pilot['meat']['tags_answer_why_favorable'] = ''
for element in dict_tags['meat']['why_favorable'].keys():
    data_pilot['meat'].loc[dict_tags['meat']['why_favorable'][element],'tags_answer_why_favorable'] = \
        element + ';' + data_pilot['meat'].loc[dict_tags['meat']['why_favorable'][element],'tags_answer_why_favorable']

data_pilot['meat']['tags_answer_landscape_argument'] = ''
for element in dict_tags['meat']['landscape_argument'].keys():
    data_pilot['meat'].loc[dict_tags['meat']['landscape_argument'][element],'tags_answer_landscape_argument'] = \
        element + ';' + data_pilot['meat'].loc[dict_tags['meat']['landscape_argument'][element],'tags_answer_landscape_argument']

data_pilot['meat']['tags_answer_carbon_footprint_argument'] = ''
for element in dict_tags['meat']['carbon_footprint_argument'].keys():
    data_pilot['meat'].loc[dict_tags['meat']['carbon_footprint_argument'][element],'tags_answer_carbon_footprint_argument'] = \
        element + ';' + data_pilot['meat'].loc[dict_tags['meat']['carbon_footprint_argument'][element],'tags_answer_carbon_footprint_argument']

del element


##### Air travel
dict_full_answers['airtravel'] = {}
dict_full_answers['airtravel']['why_against_open'] = data_pilot['airtravel']['airtravel_why_against_open'].dropna()
dict_full_answers['airtravel']['why_against_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Airtravel\airtravel_why_against.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['airtravel']['why_favorable_open'] = data_pilot['airtravel']['airtravel_why_favorable_open'].dropna()
dict_full_answers['airtravel']['why_favorable_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Airtravel\airtravel_why_favorable.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['airtravel']['why_neutral_open'] = data_pilot['airtravel']['airtravel_why_neutral_open'].dropna()
dict_full_answers['airtravel']['why_neutral_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Airtravel\airtravel_why_neutral.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['airtravel']['open_mindedness_argument_open'] = data_pilot['airtravel']['airtravel_open_mindedness_argument_open'].dropna()
dict_full_answers['airtravel']['open_mindedness_argument_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Airtravel\airtravel_open_mindedness_argument.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['airtravel']['carbon_footprint_argument_open'] = data_pilot['airtravel']['airtravel_carbon_footprint_argument_open'].dropna()
dict_full_answers['airtravel']['carbon_footprint_argument_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Airtravel\airtravel_carbon_argument.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_tags['airtravel'] = {}
dict_tags['airtravel']['why_against'] = {
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

dict_tags['airtravel']['why_favorable'] = {
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

dict_tags['airtravel']['why_neutral'] = {
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

dict_tags['airtravel']['open_mindedness_argument'] = {
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

dict_tags['airtravel']['carbon_footprint_argument'] = {
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
for element in dict_tags['airtravel']['why_against'].keys():
    data_pilot['airtravel'].loc[dict_tags['airtravel']['why_against'][element],'tags_answer_why_against'] = \
        element + ';' + data_pilot['airtravel'].loc[dict_tags['airtravel']['why_against'][element],'tags_answer_why_against']

data_pilot['airtravel']['tags_answer_why_neutral'] = ''
for element in dict_tags['airtravel']['why_neutral'].keys():
    data_pilot['airtravel'].loc[dict_tags['airtravel']['why_neutral'][element],'tags_answer_why_neutral'] = \
        element + ';' + data_pilot['airtravel'].loc[dict_tags['airtravel']['why_neutral'][element],'tags_answer_why_neutral']

data_pilot['airtravel']['tags_answer_why_favorable'] = ''
for element in dict_tags['airtravel']['why_favorable'].keys():
    data_pilot['airtravel'].loc[dict_tags['airtravel']['why_favorable'][element],'tags_answer_why_favorable'] = \
        element + ';' + data_pilot['airtravel'].loc[dict_tags['airtravel']['why_favorable'][element],'tags_answer_why_favorable']

data_pilot['airtravel']['tags_answer_open_mindedness_argument'] = ''
for element in dict_tags['airtravel']['open_mindedness_argument'].keys():
    data_pilot['airtravel'].loc[dict_tags['airtravel']['open_mindedness_argument'][element],'tags_answer_open_mindedness_argument'] = \
        element + ';' + data_pilot['airtravel'].loc[dict_tags['airtravel']['open_mindedness_argument'][element],'tags_answer_open_mindedness_argument']

data_pilot['airtravel']['tags_answer_carbon_footprint_argument'] = ''
for element in dict_tags['airtravel']['carbon_footprint_argument'].keys():
    data_pilot['airtravel'].loc[dict_tags['airtravel']['carbon_footprint_argument'][element],'tags_answer_carbon_footprint_argument'] = \
        element + ';' + data_pilot['airtravel'].loc[dict_tags['airtravel']['carbon_footprint_argument'][element],'tags_answer_carbon_footprint_argument']

del element


##### Vehicle
dict_full_answers['vehicle'] = {}
dict_full_answers['vehicle']['why_against_open'] = data_pilot['vehicle']['vehicle_why_against_open'].dropna()
dict_full_answers['vehicle']['why_against_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Vehicle\vehicle_why_against.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['vehicle']['why_favorable_open'] = data_pilot['vehicle']['vehicle_why_favorable_open'].dropna()
dict_full_answers['vehicle']['why_favorable_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Vehicle\vehicle_why_favorable.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['vehicle']['why_diesel_open'] = data_pilot['vehicle']['vehicle_why_diesel_open'].dropna()
dict_full_answers['vehicle']['why_diesel_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Vehicle\vehicle_why_diesel.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['vehicle']['why_neutral_open'] = data_pilot['vehicle']['vehicle_why_neutral_open'].dropna()
dict_full_answers['vehicle']['why_neutral_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Vehicle\vehicle_why_neutral.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['vehicle']['electric_pollutes_more_argument_open'] = data_pilot['vehicle']['vehicle_electric_pollutes_more_argument_open'].dropna()
dict_full_answers['vehicle']['electric_pollutes_more_argument_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Vehicle\vehicle_electric_pollutes_more_argument.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['vehicle']['thermal_pollutes_more_argument_open'] = data_pilot['vehicle']['vehicle_thermal_pollutes_more_argument_open'].dropna()
dict_full_answers['vehicle']['thermal_pollutes_more_argument_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Vehicle\vehicle_thermal_pollutes_more_argument.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_tags['vehicle'] = {}
dict_tags['vehicle']['why_against'] = {
    'Environment': [10,11,27,33,87,102,105,111,116,134,137,195,199,206,222,223,243,251,
                    256,289,295,309,316,331,383,404,439,443,454,480,717,723,804,822,938,
                    1186,3233,3234,3377],
    'Climate_change': [87,111,199,206,223,243,251,383,439,480,723,822,3234],
    'Air_pollution': [105,331,938,3377],
    'Good_alternatives_exist': [195,256,804,938,986],
    'Save_money': [256,309,454],
    'Reduce_energy_dependency': [331,454],
    'Dont_know': [68,341],
    'Unclear_undetermined': [27,134,598],
    }

dict_tags['vehicle']['why_favorable'] = {
    'EV_pollute_as_much_or_more': [39,47,127,156,244,257,275,319,329,342,354,379,
                                   395,401,444,654,673,905],
    'EV_construction_pollutes': [39,49,329,354,401,654,740],
    'Electricity_generation_pollutes': [39,257,329,354,394,415,654],
    'Batteries_pollute': [60,156,236,257,342,354,369,401,415,654,887],
    'Lower_cost': [35,59,99,168,202,244,266,299,304,337,371,379,395,435,458,
                   469,672,740,777,942,991,1011,1229,1277],
    'EV_not_convenient': [59,60,99,125,182,187,236,241,257,342,369,387,394,395,
                          415,435,447,458,528,551,561,3220,3294],
    'Lack_infrastructures': [99,325,369,387,394,458,654,1852],
    'Uncertainties': [127,1011],
    'Fiability': [99,127,148,293,325,337,584,761,1117,1229,1852,3774],
    'Requires_more_nuclear': [354,394,2197],
    'New_thermal_cleaner': [371,469,486],
    'Rural_areas': [325,447,486,777],
    'Poor_people_cannot': [59,299,304,371,379,395,777,991,1011,1205,1277],
    'Other_things_pollute_more': [319,371],
    'Impact_poor_countries': [415,740],
    'Protect_economy': [2197],
    'Favor_bio_energies': [740],
    'Favor_hydrogen': [39,60],
    'Opposite_argument': [1011,3294],
    'Dont_know': [],
    'Unclear_undetermined': [40,77,96,193,372,464,693],
    }

dict_tags['vehicle']['why_diesel'] = {
    'Environment': [13,70,76,85,141,159,227,273,324,403,414,796],
    'Air_pollution': [13,141],
    'Batteries_pollute': [85],
    'New_thermal_cleaner': [70],
    'Cost_EV': [414],
    'Poor_people_cannot_EV': [414],
    'Dont_know': [510],
    'Unclear_undetermined': [129,268],
    }

dict_tags['vehicle']['why_neutral'] = {
    'Environment': [58,422,473,540],
    'Batteries_pollute': [58],
    'Favor_bio_energies': [163],
    'Less_convenient': [422],
    'Cost': [473,540],
    'Fiability': [1104],
    'Dont_know': [24,296,426,1008],
    'Unclear_undetermined': [540],
    }

dict_tags['vehicle']['electric_pollutes_more_argument'] = {
    'Agree': [10,11,24,87,105,163,222,256,296,383,540,598,723,3234,3377],
    'Not_true': [58,116,134,137,195,199,206,289,295,404,439,443,454,473,480,
                 717,804,1186],
    'It_depends': [10,111,179,222,223,331,422,938,986,3233,3234,3377],
    'Uncertain': [27,105,295,439,454,473,480,723,822,1104],
    'Batteries_pollute': [11,24,27,33,87,105,111,163,179,206,222,223,251,256,
                          309,331,598,938,986],
    'Nuclear': [540,598,3377],
    'Less_local_pollution': [243,443],
    'Impact_poor_countries': [540],
    'Unrelated_opposite_argument': [],
    'Dont_know': [68,102,316,341,426,1008],
    'Unclear_undetermined': [],
    }

dict_tags['vehicle']['thermal_pollutes_more_argument'] = {
    'Agree': [60,71,99,125,127,141,156,227,236,268,293,299,324,325,337,342,354,
              371,387,394,395,435,469,551,672,673,777,898,942,991,1117,1229,
              1277],
    'Not_true': [39,40,47,59,76,85,129,241,244,257,266,275,319,329,372,415,444,
                 464,584,693,761,887,2197,3294],
    'It_depends': [13,60,148,354,369,379,394,401,469,3220],
    'Uncertain': [99,129,168,182,202,227,241,244,266,275,293,325,372,387,395,
                  403,458,528,584,654,777,796,887,1852],
    'Batteries_pollute': [39,59,60,85,156,159,182,241,342,387,395,401,528,551,
                          561,654,991,1205],
    'EV_construction_pollutes': [39,129,148,182,202,257,369,387,464,654,887,
                                 2197,3220,3294],
    'Electricity_generation_pollutes': [13,39,85,99,319,379,403,464,469,796,
                                        1205,2197],
    'Nuclear': [13,319,403,464,1205],
    'Less_local_pollution': [],
    'Impact_poor_countries': [],
    'Unrelated_opposite_argument': [268,337,342,354,387,528,561,672,991,1277,
                                    1852],
    'Dont_know': [35,47,70,96,159,193,273,304,414,447,486,510,561,621,740,
                  905,3774],
    'Unclear_undetermined': [77,187,1011],
    }


data_pilot['vehicle']['tags_answer_why_against'] = ''
for element in dict_tags['vehicle']['why_against'].keys():
    data_pilot['vehicle'].loc[dict_tags['vehicle']['why_against'][element],'tags_answer_why_against'] = \
        element + ';' + data_pilot['vehicle'].loc[dict_tags['vehicle']['why_against'][element],'tags_answer_why_against']

data_pilot['vehicle']['tags_answer_why_neutral'] = ''
for element in dict_tags['vehicle']['why_neutral'].keys():
    data_pilot['vehicle'].loc[dict_tags['vehicle']['why_neutral'][element],'tags_answer_why_neutral'] = \
        element + ';' + data_pilot['vehicle'].loc[dict_tags['vehicle']['why_neutral'][element],'tags_answer_why_neutral']

data_pilot['vehicle']['tags_answer_why_diesel'] = ''
for element in dict_tags['vehicle']['why_diesel'].keys():
    data_pilot['vehicle'].loc[dict_tags['vehicle']['why_diesel'][element],'tags_answer_why_diesel'] = \
        element + ';' + data_pilot['vehicle'].loc[dict_tags['vehicle']['why_diesel'][element],'tags_answer_why_diesel']

data_pilot['vehicle']['tags_answer_why_favorable'] = ''
for element in dict_tags['vehicle']['why_favorable'].keys():
    data_pilot['vehicle'].loc[dict_tags['vehicle']['why_favorable'][element],'tags_answer_why_favorable'] = \
        element + ';' + data_pilot['vehicle'].loc[dict_tags['vehicle']['why_favorable'][element],'tags_answer_why_favorable']

data_pilot['vehicle']['tags_answer_electric_pollutes_more_argument'] = ''
for element in dict_tags['vehicle']['electric_pollutes_more_argument'].keys():
    data_pilot['vehicle'].loc[dict_tags['vehicle']['electric_pollutes_more_argument'][element],'tags_answer_electric_pollutes_more_argument'] = \
        element + ';' + data_pilot['vehicle'].loc[dict_tags['vehicle']['electric_pollutes_more_argument'][element],'tags_answer_electric_pollutes_more_argument']

data_pilot['vehicle']['tags_answer_thermal_pollutes_more_argument'] = ''
for element in dict_tags['vehicle']['thermal_pollutes_more_argument'].keys():
    data_pilot['vehicle'].loc[dict_tags['vehicle']['thermal_pollutes_more_argument'][element],'tags_answer_thermal_pollutes_more_argument'] = \
        element + ';' + data_pilot['vehicle'].loc[dict_tags['vehicle']['thermal_pollutes_more_argument'][element],'tags_answer_thermal_pollutes_more_argument']

del element

##### Vaccine
dict_full_answers['vaccine'] = {}
dict_full_answers['vaccine']['why_against_open'] = data_pilot['vaccine']['vaccine_why_against_open'].dropna()
dict_full_answers['vaccine']['why_against_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Vaccine\vaccine_why_against.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['vaccine']['why_favorable_open'] = data_pilot['vaccine']['vaccine_why_favorable_open'].dropna()
dict_full_answers['vaccine']['why_favorable_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Vaccine\vaccine_why_favorable.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['vaccine']['why_neutral_open'] = data_pilot['vaccine']['vaccine_why_neutral_open'].dropna()
dict_full_answers['vaccine']['why_neutral_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Vaccine\vaccine_why_neutral.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['vaccine']['poor_country_argument_open'] = data_pilot['vaccine']['vaccine_poor_country_argument_open'].dropna()
dict_full_answers['vaccine']['poor_country_argument_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Vaccine\vaccine_poor_country_argument.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_full_answers['vaccine']['protecting_others_argument_open'] = data_pilot['vaccine']['vaccine_protecting_others_argument_open'].dropna()
dict_full_answers['vaccine']['protecting_others_argument_open'].to_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Text_open_questions\Vaccine\vaccine_protecting_others_argument.csv',
                            sep=';', encoding='utf-8-sig', index=True)

dict_tags['vaccine'] = {}
dict_tags['vaccine']['why_against'] = {
    'Health_risk_vaccin': [15,284,987],
    'Anti_vaccins': [172],
    'Lack_hindsight': [284,411,987],
    'Distrust': [172,306,534],
    'Small_benefits_vaccin': [904],
    'Finances_industry': [172,306],
    'Opposite_argument': [],
    'Dont_know': [122],
    'Unclear_undetermined': [18,382],
    }

dict_tags['vaccine']['why_favorable'] = {
    'End_this_situation': [21,30,61,131,145,203,221,276,281,362,365,416,455,
                           665,750,771,817,953,1271,1770,2223,3240],
    'Reach_collective_immunity': [37,61,73,82,115,131,155,162,164,176,189,221,
                                  290,321,328,399,413,416,455,482,665,750,771,
                                  793,882,1770,3240],
    'Avoid_lockdowns': [38,298,328,515],
    'Avoid_new_wave': [245,264,290,487,559],
    'Safer': [45,56,210,265,272,340,434,451,687,716,814,901,966,3222],
    'Avoid_variants': [48,203,253,290,559,611,690],
    'Avoid_transmissions': [55,164,173,190,194,209,230,245,253,264,265,267,276,
                            298,340,353,384,399,440,478,687,3222,3245],
    'Limit_serious_cases': [115,190,276,559],
    'Avoid_hospital_overload': [276,314],
    'Moral_responsibility': [276,336,413],
    'Economic_activity': [276],
    'Opposite_argument': [314],
    'Dont_know': [],
    'Unclear_undetermined': [314],
    }# Note: by contrast with 'Reach_collective_immunity', the item 'Avoid_transmissions' does not explicitely refer to reaching a state where the virus disappears
# When people refer to 'eradiquer la pandemie', it is understood that they refer to all its implications so 'End_this_situation' is also applied, while 'eradiquer le virus' is simply understood as 'Reach_collective_immunity'
# Safer often refers to more personal considerations

dict_tags['vaccine']['why_neutral'] = {
    'End_this_situation': [31,130,393,445,852,881,3227],
    'Reach_collective_immunity': [54,65,130,320,391,405,445,775,1002],
    'Avoid_lockdowns': [219],
    'Avoid_new_wave': [101,219],
    'Safer': [150,183,352,539,635,852,899],
    'Avoid_variants': [363],
    'Avoid_transmissions': [101,106,113,130,323,463,472,832],
    'Limit_serious_cases': [101,263,277,539,899],
    'Moral_responsibility': [183],
    'Economic_activity': [277],
    'Avoid_hospital_overload': [101,472],
    'Other_mandatory_vaccines_exist': [707],
    'Uncertainty_efficacy': [54,109,320],
    'Health_risk_vaccin': [92,93,101,151,183,208,213,220,323,445,446,726,852,881],
    'Anti_vaccins': [],
    'Lack_hindsight': [93,101,151,208,213,220,323,333,445,446,645,852],
    'Distrust': [208,3257],
    'Small_benefits_vaccin': [121,238,492],
    'Could_generate_complotism': [65],
    'Everyone_should_be_free': [113,130,238,263,393,472,547,3257,3347],
    'Finances_industry': [533],
    'Dont_know': [67,132,370,421,441,609,645],
    'Unclear_undetermined':[9,327,376],
    }

dict_tags['vaccine']['poor_country_argument'] = {
    'Agree': [30,45,48,56,281,314,451,966,1100,1271],
    'Not_true': [21,38,61,176,177,221,230,264,265,328,399,440,482,611,687,
                 690,716,771,793,814,817,953,1770,2223,3222,3245],
    'It_depends': [155,162,210,276,314,384,434,455,559,665,882],
    'Uncertain': [353],
    'French_first': [21,38,155,176,203,230,298,328,336,365,373,399,440,487,
                     690,771,953,1770,3222,3245],
    'Yes_to_limit_variants': [48],
    'Yes_to_protect_us': [30,48,276],
    'Do_both': [55,73,82,115,131,145,164,173,189,190,245,253,267,272,290,
                321,340,362,413,416,478,482,817,3240],
    'They_need_it_less': [61,162,687],
    'Their_dirigeants_responsibility': [336,455],
    'Close_borders': [245,314,373],
    'Unrelated_opposite_argument': [],
    'Dont_know': [37,515,901],
    'Unclear_undetermined': [194,209,665,750],
    }

dict_tags['vaccine']['protecting_others_argument'] = {
    'Agree': [31,54,65,93,101,113,130,150,167,183,208,219,220,240,277,306,
              333,376,382,391,445,472,635,645,707,775,832,899,987,1002,3227],
    'Not_true': [9,15,92,106,109,121,132,151,172,213,238,263,284,320,323,363,
                 370,393,405,411,441,492,539,609,852,904,3347],
    'It_depends': [67,106,411,881],
    'Uncertain': [15,93,109,151,213,284,320,533,547,1209],
    'Not_for_variants': [93,323,987],
    'Only_prevents_serious_cases': [405,539],
    'Distrust': [121,213,238,320,393,534],
    'Agressive_answer': [172],
    'Unrelated_opposite_argument': [130,132,213,320,333,446,852],
    'Dont_know': [122,726],
    'Unclear_undetermined': [18,327,333,421,446,3257],
    }

data_pilot['vaccine']['tags_answer_why_against'] = ''
for element in dict_tags['vaccine']['why_against'].keys():
    data_pilot['vaccine'].loc[dict_tags['vaccine']['why_against'][element],'tags_answer_why_against'] = \
        element + ';' + data_pilot['vaccine'].loc[dict_tags['vaccine']['why_against'][element],'tags_answer_why_against']

data_pilot['vaccine']['tags_answer_why_neutral'] = ''
for element in dict_tags['vaccine']['why_neutral'].keys():
    data_pilot['vaccine'].loc[dict_tags['vaccine']['why_neutral'][element],'tags_answer_why_neutral'] = \
        element + ';' + data_pilot['vaccine'].loc[dict_tags['vaccine']['why_neutral'][element],'tags_answer_why_neutral']

data_pilot['vaccine']['tags_answer_why_favorable'] = ''
for element in dict_tags['vaccine']['why_favorable'].keys():
    data_pilot['vaccine'].loc[dict_tags['vaccine']['why_favorable'][element],'tags_answer_why_favorable'] = \
        element + ';' + data_pilot['vaccine'].loc[dict_tags['vaccine']['why_favorable'][element],'tags_answer_why_favorable']

data_pilot['vaccine']['tags_answer_poor_country_argument'] = ''
for element in dict_tags['vaccine']['poor_country_argument'].keys():
    data_pilot['vaccine'].loc[dict_tags['vaccine']['poor_country_argument'][element],'tags_answer_poor_country_argument'] = \
        element + ';' + data_pilot['vaccine'].loc[dict_tags['vaccine']['poor_country_argument'][element],'tags_answer_poor_country_argument']

data_pilot['vaccine']['tags_answer_protecting_others_argument'] = ''
for element in dict_tags['vaccine']['protecting_others_argument'].keys():
    data_pilot['vaccine'].loc[dict_tags['vaccine']['protecting_others_argument'][element],'tags_answer_protecting_others_argument'] = \
        element + ';' + data_pilot['vaccine'].loc[dict_tags['vaccine']['protecting_others_argument'][element],'tags_answer_protecting_others_argument']

del element

##### Descriptive statistics length open-ended answers
dict_text = {}

### Meat
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
data_pilot['meat']['asked_carbon_footprint_argument'] = data_pilot['meat']['asked_why_favorable']

dict_text['meat'] = {}
for question in ['why_against', 'why_neutral', 'why_favorable', 'landscape_argument', 'carbon_footprint_argument']:
    data_pilot['meat']['nb_words_meat_{}_open'.format(question)] = data_pilot['meat']['meat_{}_open'.format(question)].str.len()
    dict_text['meat'][question] = {}

    dict_text['meat'][question]['nb_asked'] = data_pilot['meat']['asked_{}'.format(question)].sum()
    dict_text['meat'][question]['nb_answered'] = len(data_pilot['meat'][data_pilot['meat']['nb_words_meat_{}_open'.format(question)] > 0])
    dict_text['meat'][question]['length_answer_mean'] = data_pilot['meat']['nb_words_meat_{}_open'.format(question)].mean()
    for i in [10,25,50,75,90]:
        dict_text['meat'][question]['length_answer_percentile_{}'.format(i)] = \
            data_pilot['meat']['nb_words_meat_{}_open'.format(question)].quantile(i/100)
    dict_text['meat'][question]['length_answer_max'] = data_pilot['meat']['nb_words_meat_{}_open'.format(question)].max()

del question, i

### Airtravel
data_pilot['airtravel']['asked_why_against'] = (
    1*(data_pilot['airtravel']['airtravel_frequency_desirable'] == 'jamais')
    + 1*(data_pilot['airtravel']['airtravel_frequency_desirable'] == u'au moins une fois dans leur vie')
    )
data_pilot['airtravel']['asked_why_neutral'] = (
    1*(data_pilot['airtravel']['airtravel_frequency_desirable'] == u'NSP (Ne sait pas, ne se prononce pas).')
    )
data_pilot['airtravel']['asked_why_favorable'] = (
    1 - data_pilot['airtravel']['asked_why_against'] - data_pilot['airtravel']['asked_why_neutral']
    )
data_pilot['airtravel']['asked_open_mindedness_argument'] = (
    data_pilot['airtravel']['asked_why_against'] + data_pilot['airtravel']['asked_why_neutral']
    )
data_pilot['airtravel']['asked_carbon_footprint_argument'] = data_pilot['airtravel']['asked_why_favorable']

dict_text['airtravel'] = {}
for question in ['why_against', 'why_neutral', 'why_favorable', 'open_mindedness_argument', 'carbon_footprint_argument']:
    data_pilot['airtravel']['nb_words_airtravel_{}_open'.format(question)] = data_pilot['airtravel']['airtravel_{}_open'.format(question)].str.len()
    dict_text['airtravel'][question] = {}

    dict_text['airtravel'][question]['nb_asked'] = data_pilot['airtravel']['asked_{}'.format(question)].sum()
    dict_text['airtravel'][question]['nb_answered'] = len(data_pilot['airtravel'][data_pilot['airtravel']['nb_words_airtravel_{}_open'.format(question)] > 0])
    dict_text['airtravel'][question]['length_answer_mean'] = data_pilot['airtravel']['nb_words_airtravel_{}_open'.format(question)].mean()
    for i in [10,25,50,75,90]:
        dict_text['airtravel'][question]['length_answer_percentile_{}'.format(i)] = \
            data_pilot['airtravel']['nb_words_airtravel_{}_open'.format(question)].quantile(i/100)
    dict_text['airtravel'][question]['length_answer_max'] = data_pilot['airtravel']['nb_words_airtravel_{}_open'.format(question)].max()

del question, i

### Vehicle
data_pilot['vehicle']['asked_why_against'] = (
    1*(data_pilot['vehicle']['vehicle_desirable_future'] == u'de cesser de les utiliser très rapidement (d\'ici 2030 ou avant)')
    + 1*(data_pilot['vehicle']['vehicle_desirable_future'] == u'de cesser de les utiliser progressivement (d\'ici 2040 ou 2050)')
    )
data_pilot['vehicle']['asked_why_neutral'] = (
    1*(data_pilot['vehicle']['vehicle_desirable_future'] == u'NSP (Ne sait pas, ne se prononce pas).')
    )
data_pilot['vehicle']['asked_why_diesel'] = (
    1*(data_pilot['vehicle']['vehicle_desirable_future'] == u'de cesser d\'utiliser les véhicules diesel mais pas les véhicule essence')
    )
data_pilot['vehicle']['asked_why_favorable'] = (
    1 - data_pilot['vehicle']['asked_why_against'] - data_pilot['vehicle']['asked_why_neutral'] - data_pilot['vehicle']['asked_why_diesel']
    )
data_pilot['vehicle']['asked_electric_pollutes_more_argument'] = (
    data_pilot['vehicle']['asked_why_against'] + data_pilot['vehicle']['asked_why_neutral']
    )
data_pilot['vehicle']['asked_thermal_pollutes_more_argument'] = 1 - data_pilot['vehicle']['asked_electric_pollutes_more_argument']

dict_text['vehicle'] = {}
for question in ['why_against', 'why_neutral', 'why_diesel', 'why_favorable', 'electric_pollutes_more_argument', 'thermal_pollutes_more_argument']:
    data_pilot['vehicle']['nb_words_vehicle_{}_open'.format(question)] = data_pilot['vehicle']['vehicle_{}_open'.format(question)].str.len()
    dict_text['vehicle'][question] = {}

    dict_text['vehicle'][question]['nb_asked'] = data_pilot['vehicle']['asked_{}'.format(question)].sum()
    dict_text['vehicle'][question]['nb_answered'] = len(data_pilot['vehicle'][data_pilot['vehicle']['nb_words_vehicle_{}_open'.format(question)] > 0])
    dict_text['vehicle'][question]['length_answer_mean'] = data_pilot['vehicle']['nb_words_vehicle_{}_open'.format(question)].mean()
    for i in [10,25,50,75,90]:
        dict_text['vehicle'][question]['length_answer_percentile_{}'.format(i)] = \
            data_pilot['vehicle']['nb_words_vehicle_{}_open'.format(question)].quantile(i/100)
    dict_text['vehicle'][question]['length_answer_max'] = data_pilot['vehicle']['nb_words_vehicle_{}_open'.format(question)].max()

del question, i


### Vaccine
data_pilot['vaccine']['asked_why_against'] = (
    1*(data_pilot['vaccine']['vaccine_desirable'] == u'tous les Français se fassent vacciner à partir de 12 ans')
    + 1*(data_pilot['vaccine']['vaccine_desirable'] == u'tous les Français se fassent vacciner à partir de 18 ans')
    )
data_pilot['vaccine']['asked_why_neutral'] = (
    1*(data_pilot['vaccine']['vaccine_desirable'] == u'NSP (Ne sait pas, ne se prononce pas).')
    )
data_pilot['vaccine']['asked_why_favorable'] = (
    1 - data_pilot['vaccine']['asked_why_against'] - data_pilot['vaccine']['asked_why_neutral']
    )
data_pilot['vaccine']['asked_poor_country_argument'] = (
    data_pilot['vaccine']['asked_why_against'] + data_pilot['vaccine']['asked_why_neutral']
    )
data_pilot['vaccine']['asked_protecting_others_argument'] = 1 - data_pilot['vaccine']['asked_poor_country_argument']

dict_text['vaccine'] = {}
for question in ['why_against', 'why_neutral', 'why_favorable', 'poor_country_argument', 'protecting_others_argument']:
    data_pilot['vaccine']['nb_words_vaccine_{}_open'.format(question)] = data_pilot['vaccine']['vaccine_{}_open'.format(question)].str.len()
    dict_text['vaccine'][question] = {}

    dict_text['vaccine'][question]['nb_asked'] = data_pilot['vaccine']['asked_{}'.format(question)].sum()
    dict_text['vaccine'][question]['nb_answered'] = len(data_pilot['vaccine'][data_pilot['vaccine']['nb_words_vaccine_{}_open'.format(question)] > 0])
    dict_text['vaccine'][question]['length_answer_mean'] = data_pilot['vaccine']['nb_words_vaccine_{}_open'.format(question)].mean()
    for i in [10,25,50,75,90]:
        dict_text['vaccine'][question]['length_answer_percentile_{}'.format(i)] = \
            data_pilot['vaccine']['nb_words_vaccine_{}_open'.format(question)].quantile(i/100)
    dict_text['vaccine'][question]['length_answer_max'] = data_pilot['vaccine']['nb_words_vaccine_{}_open'.format(question)].max()

del question, i


### End of survey box
data_pilot['full']['nb_words_end_of_survey_box_open'] = data_pilot['full']['end_of_survey_box'].str.len()
dict_text_end_survey = {}

dict_text_end_survey['nb_asked'] = len(data_pilot['full'])
dict_text_end_survey['nb_answered'] = len(data_pilot['full'].query('nb_words_end_of_survey_box_open > 0'))
dict_text_end_survey['length_answer_mean'] = data_pilot['full']['nb_words_end_of_survey_box_open'].mean()
for i in [10,25,50,75,90]:
    dict_text_end_survey['length_answer_percentile_{}'.format(i)] = \
        data_pilot['full']['nb_words_end_of_survey_box_open'].quantile(i/100)
dict_text_end_survey['length_answer_max'] = data_pilot['full']['nb_words_end_of_survey_box_open'].max()

del i


##### Create latex file with summary statistics
data_pilot['labels'] = \
    pd.read_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_pilot_narratives_labels.csv', sep=',', index_col=0)

dict_variables = data_pilot['labels'].to_dict()


latex_file = open(r"C:\Users\TDOUENN\Documents\Projects\Narratives\Data\latex_template.txt").read()

dict_latex_tables = {}
dict_latex_tables['full_tables'] = {}

dict_frequency_tags = {}
for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
    dict_latex_tables[topic] = {}
    dict_frequency_tags[topic] = {}
    dict_latex_tables['full_tables'][topic] = ' '

    if topic == 'meat':
        section_title = '\section{Meat}'
    elif topic == 'airtravel':
        section_title = '\section{Air travel}'
    elif topic == 'vehicle':
        section_title = '\section{Vehicle}'
    elif topic == 'vaccine':
        section_title = '\section{Vaccine}'

    for question in dict_tags[topic]:
        dict_frequency_tags[topic][question] = {}
        for tag in dict_tags[topic][question].keys():
            dict_frequency_tags[topic][question][tag] = data_pilot[topic]['tags_answer_{}'.format(question)].str.count(tag).sum()

        dict_frequency_tags[topic][question][u'Total number of answers'] = dict_text[topic][question]['nb_answered']

        title = dict_variables['Question_survey'][topic + '_' + question + '_open']
        short_title = title.replace(u'Merci de détailler votre réponse afin que nous puissions prendre en compte votre opinion le mieux possible.', '').rstrip('\n')
        
        dict_latex_tables[topic][question] = \
        pd.DataFrame.from_dict(dict_frequency_tags[topic][question], orient='index',
                           columns=['Number']).sort_values(by='Number', ascending=False).to_latex(
            caption='\"{}\"'.format(short_title),
            float_format="{:.0%}".format,
            )

        dict_latex_tables['full_tables'][topic] = (
            dict_latex_tables['full_tables'][topic] + '\n' + dict_latex_tables[topic][question]
            )

    latex_file = latex_file.replace("\end{document}",
        '\\clearpage' + '\n' + '{}'.format(section_title) + '\n' + dict_latex_tables['full_tables'][topic] + '\n' + "\end{document}" )
        
latex_file = latex_file.replace("begin{table}", "begin{table}[h!]")

del topic, question, tag, title, short_title, section_title


### Common occurrence tags
dict_cross_frequency_tags = {}
for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
    dict_cross_frequency_tags[topic] = {}
    for question in dict_tags[topic]:
        tags = dict_tags[topic][question].keys()
        df_cross_frequency = pd.DataFrame(index=tags, columns=tags).fillna(0)
        for tag_raw in tags:
            for tag_col in tags:
                df_cross_frequency[tag_raw][tag_col] = (
                    data_pilot[topic][data_pilot[topic]['tags_answer_{}'.format(question)].str.contains(tag_raw, regex=True)]['tags_answer_{}'.format(question)].str.contains(tag_col, regex=True).sum()
                    )
        dict_cross_frequency_tags[topic][question] = df_cross_frequency

del df_cross_frequency, topic, question, tags, tag_raw, tag_col
