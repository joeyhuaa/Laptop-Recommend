import numpy as np
import pandas as pd

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 15)

# print number of missing values in each column
# for col in study_df.columns:
#     print(col, study_df[study_df[col].isna()].shape)
# print('~'*20)

# csv into pd data frame
study_df = pd.read_csv('newegg_study_laptops.csv', sep=',')

# temporarily fill all N/A with -1
study_df = study_df.fillna(-1)

# turn all prices into floats
for i in range(len(study_df['price'])):
    if type(study_df.loc[i, 'price']) == str:
        study_df.loc[i, 'price'] = float(study_df.loc[i, 'price'].replace(',', ''))

# remove strings from cpu_speed, leave only GHz, turn into floats
for i in range(len(study_df['cpu_speed'])):

    # missing values
    if study_df.loc[i, 'cpu_speed'] == -1:
        pass

    # case with extra words at beginning
    elif '(' in study_df.loc[i, 'cpu_speed']:
        study_df.loc[i, 'cpu_speed'] = float(study_df.loc[i,'cpu_speed'].split('(')[1].replace(')', '').split(' ')[0])

    # when GHz is at the end
    elif study_df.loc[i, 'cpu_speed'].split(' ')[1] == 'GHz':
        study_df.loc[i, 'cpu_speed'] = float(study_df.loc[i, 'cpu_speed'].split(' ')[0])

# convert cores into integer values
for i in range(len(study_df['cores'])):
    if study_df.loc[i, 'cores'] == -1:
        pass
    elif 'Dual' in study_df.loc[i, 'cores']:
        study_df.loc[i, 'cores'] = 2
    elif 'Quad' in study_df.loc[i, 'cores']:
        study_df.loc[i, 'cores'] = 4
    elif '6' in study_df.loc[i, 'cores']:
        study_df.loc[i, 'cores'] = 6

# leave only GB in storage, convert to int
# create a new column called cpu_type that = SSD or HDD
import re
for i in range(len(study_df['storage'])):
    study_df.loc[i, 'storage'] = re.split('[A-z]', study_df.loc[i, 'storage'])

# turn all screen sizes into floats
for i in range(len(study_df['screen'])):
    if study_df.loc[i, 'screen'] == 'No':
        study_df.loc[i, 'screen'] = 0
    if type(study_df.loc[i, 'screen']) == str:
        study_df.loc[i, 'screen'] = float(study_df.loc[i, 'screen'].replace('"', ''))


# remove duplicate rows




