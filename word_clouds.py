#import numpy as np
import pandas as pd
#from os import path
#from PIL import Image
from wordcloud import WordCloud#, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
## % matplotlib inline

#import nltk
from nltk.corpus import stopwords

stopwords = stopwords.words('french')

# Load in the dataframe
data_pilot = {}

data_pilot['full'] = \
    pd.read_csv(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\data_qualtrics_pilot_narratives_prepared.csv', sep=',', index_col=0)

data_pilot['meat'] = data_pilot['full'].query('topic_meat == 1').copy()
data_pilot['airtravel'] = data_pilot['full'].query('topic_airtravel == 1').copy()
data_pilot['vehicle'] = data_pilot['full'].query('topic_vehicle == 1').copy()
data_pilot['vaccine'] = data_pilot['full'].query('topic_vaccine == 1').copy()

##### End of survey box
# Create list of words
text_end_box = ' '.join([str(item) for item in data_pilot['full']['end_of_survey_box'].dropna().tolist()])

# Create and generate a word cloud image:
wordcloud = WordCloud(
    stopwords=stopwords,
    background_color='white'
    ).generate(text_end_box)

# Display and save the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

wordcloud.to_file(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Word_clouds\open_end_box.png')


##### Four topics
text_topics = {}
for topic in ['meat', 'airtravel', 'vehicle', 'vaccine']:
    text_topics[topic] = {}
    
    if topic == 'meat':
        counter_arguments = ['landscape_argument', 'carbon_footprint_argument']
    elif topic == 'airtravel':
        counter_arguments = ['carbon_footprint_argument', 'open_mindedness_argument']
    elif topic == 'vehicle':
        counter_arguments = ['why_diesel', 'electric_pollutes_more_argument', 'thermal_pollutes_more_argument']
    elif topic == 'vaccine':
        counter_arguments = ['poor_country_argument', 'protecting_others_argument']
    
    
    for question in ['why_against', 'why_neutral', 'why_favorable'] + counter_arguments:
        text_topics[topic][question] = \
            ' '.join([str(item) for item in data_pilot[topic]['{0}_{1}_open'.format(topic, question)].dropna().tolist()])

        wordcloud = WordCloud(
        stopwords=stopwords,
        background_color='white'
        ).generate(text_topics[topic][question])
    
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        
        wordcloud.to_file(r'C:\Users\TDOUENN\Documents\Projects\Narratives\Data\Word_clouds\{0}\{1}.png'.format(topic, question))
