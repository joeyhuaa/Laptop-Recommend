import numpy as np
import pandas as pd
import re

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 15)

# csv into pd data frame
study_df = pd.read_csv('study_laptops_raw.csv', sep=',')
gaming_df = pd.read_csv('gaming_laptops_raw.csv', sep=',')

# temporarily fill all N/A with -1
study_df = study_df.fillna(-1)

# turn all prices into floats
def clean_prices(df):
    for i in range(len(df['price'])):
        if type(df.loc[i, 'price']) == str:
            df.loc[i, 'price'] = float(df.loc[i, 'price'].replace(',', ''))

    return df

# remove strings from cpu_speed, leave only GHz, turn into floats
def clean_cpu_speed(df):
    for i in range(len(df['cpu_speed'])):
        # missing values
        if df.loc[i, 'cpu_speed'] == -1:
            pass

        # case with extra words at beginning
        elif '(' in df.loc[i, 'cpu_speed']:
            df.loc[i, 'cpu_speed'] = float(df.loc[i,'cpu_speed'].split('(')[1].replace(')', '').split(' ')[0])

        # when GHz is at the end
        elif df.loc[i, 'cpu_speed'].split(' ')[1] == 'GHz':
            df.loc[i, 'cpu_speed'] = float(df.loc[i, 'cpu_speed'].split(' ')[0])

    return df

# convert cores into integer values
def clean_cores(df):
    for i in range(len(df['cores'])):
        if df.loc[i, 'cores'] == -1:
            pass
        elif 'Dual' in df.loc[i, 'cores']:
            df.loc[i, 'cores'] = 2
        elif 'Quad' in df.loc[i, 'cores']:
            df.loc[i, 'cores'] = 4
        elif '6' in df.loc[i, 'cores']:
            df.loc[i, 'cores'] = 6

    return df

# leave only GB in storage, convert to int
# create a new column called cpu_type that = SSD or HDD
def clean_storage(df):
    for i in range(len(df['storage'])):
        if df.loc[i, 'storage'] != -1:
            # df.loc[i, 'storage'] = re.split('[A-z]|,', df.loc[i, 'storage'])[0]
            df.loc[i, 'storage'] = df.loc[i, 'storage'].replace('+', ',')
            storage_split_list = re.split('[A-z]|,', df.loc[i, 'storage'])

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
            df.loc[i, 'storage'] = storage_int

    return df

def clean_memory(df):
    # retrieve GB ints from raw data
    for i in range(len(df['memory'])):
        df.loc[i, 'memory'] = int(df.loc[i, 'memory'].split(' ')[0])

    return df


def clean_screen_sizes(df):
    # turn all screen sizes into floats
    for i in range(len(df['screen'])):
        if df.loc[i, 'screen'] == 'No':
            df.loc[i, 'screen'] = -1
        if type(df.loc[i, 'screen']) == str:
            df.loc[i, 'screen'] = float(df.loc[i, 'screen'].replace('"', ''))

    return df


## MAIN ##
study_df = clean_prices(study_df)
study_df = clean_cpu_speed(study_df)
study_df = clean_cores(study_df)
study_df = clean_storage(study_df)
study_df = clean_memory(study_df)
study_df = clean_screen_sizes(study_df)

# write to csv

