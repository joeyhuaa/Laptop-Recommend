import numpy as np
import pandas as pd
import re

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 15)

# csv into pd data frame
study_df = pd.read_csv('newegg_study_laptops.csv', sep=',')

# temporarily fill all N/A with -1
study_df = study_df.fillna(-1)

# turn all prices into floats
def clean_prices():
    for i in range(len(study_df['price'])):
        if type(study_df.loc[i, 'price']) == str:
            study_df.loc[i, 'price'] = float(study_df.loc[i, 'price'].replace(',', ''))

# remove strings from cpu_speed, leave only GHz, turn into floats
def clean_cpu_speed():
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
def clean_cores():
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
def clean_storage():
    for i in range(len(study_df['storage'])):
        if study_df.loc[i, 'storage'] != -1:
            # study_df.loc[i, 'storage'] = re.split('[A-z]|,', study_df.loc[i, 'storage'])[0]
            study_df.loc[i, 'storage'] = study_df.loc[i, 'storage'].replace('+', ',')
            storage_split_list = re.split('[A-z]|,', study_df.loc[i, 'storage'])

            # retrieve integer values from raw data
            storage_int = 0
            for n in range(len(storage_split_list)):
                # add up all the integers in the split up string
                try:
                    val = int(storage_split_list[n])
                    if val == 1:
                        val = 1000
                    elif val == 2:
                        val = 2000
                    storage_int += int(val)
                except ValueError:
                    pass

            # assign new value to storage column
            study_df.loc[i, 'storage'] = storage_int

def clean_memory():
    # retrieve GB ints from raw data
    for i in range(len(study_df['memory'])):
        study_df.loc[i, 'memory'] = int(study_df.loc[i, 'memory'].split(' ')[0])


def clean_screen_sizes():
    # turn all screen sizes into floats
    for i in range(len(study_df['screen'])):
        if study_df.loc[i, 'screen'] == 'No':
            study_df.loc[i, 'screen'] = -1
        if type(study_df.loc[i, 'screen']) == str:
            study_df.loc[i, 'screen'] = float(study_df.loc[i, 'screen'].replace('"', ''))


## MAIN ##
clean_prices()
clean_cpu_speed()
clean_cores()
clean_storage()
clean_memory()
clean_screen_sizes()

study_df.to_csv('newegg_study_laptops_cleaned.csv')




