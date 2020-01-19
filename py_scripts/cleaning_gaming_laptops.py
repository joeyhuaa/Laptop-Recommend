#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import re
# In[267]:
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 15)

# Storing Gaming Laptops info
gaming_laptops_df = pd.read_csv("../data/gaming_laptops_raw.csv", sep=",")
gaming_laptops_df.head()

# In[268]:


gaming_laptops_df.cpu_speed.unique()

# Replacing the NaN Values that are in Gaming Laptops info
gaming_laptop_title = gaming_laptops_df.loc[0, "name"]
gaming_laptop_title.split(" ")
gaming_laptops_df = gaming_laptops_df.fillna(-1)  # Will get back to later

# Converting Rating Values into Integers
def clean_ratings(df):
    for i in range(len(df["rating"])):
        df["rating"] = int(df.loc[i, "rating"])
    return df

gaming_laptops_df = gaming_laptops_df.fillna(-1)

# Converting Screen Size Values into Floats
def clean_screen_sizes(df):
    # turn all screen sizes into floats
    for i in range(len(df['screen'])):
        if df.loc[i, 'screen'] == 'No':
            df.loc[i, 'screen'] = -1
        if type(df.loc[i, 'screen']) == str:
            df.loc[i, 'screen'] = float(df.loc[i, 'screen'].split(' ')[0].replace('"', ''))

    return df

def clean_cores(df):
    for i in range(len(df['cores'])):
        if df.loc[i, 'cores'] == -1:
            pass
        elif 'Dual' in df.loc[i, 'cores']:
            df.loc[i, 'cores'] = 2
        elif 'Quad' in df.loc[i, 'cores']:
            df.loc[i, 'cores'] = 4
        elif '7' in df.loc[i, 'cores']:
            df.loc[i, 'cores'] = 7
        elif "9" in df.loc[i, "cores"]:
            df.loc[i, "cores"] = 9

    return df

def clean_gpu_type():
    for i in range(len(gaming_laptops_df["gpu_type"])):
        if "0" in gaming_laptops_df["gpu_type"]:
            pass
        elif "AMD Radeon RX Vega M Gl" in gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 1
        elif "Integrated Grpahics" in gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 2
        elif "AMD Radeon RX Vega 56" in gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 56
        elif "NVIDIA GeForce MX150" in gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 150
        elif "AMD Radeon RX 560X" in gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 560
        elif "NVIDIA GeForce GTX 860M" in gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 860
        elif "NVIDIA GeForce GTX 950M" in gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 950
        elif "NVIDIA GeForce GTX 960M" in gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 960
        elif "NVIDIA GeForce GTX 970M" in gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 970
        elif "NVIDIA GeForce GTX 980" in gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 980
        elif "NVIDIA GeForce GTX 1050 Ti" in gaming_laptops_df["gpu_type"] or "NVIDIA GeForce GTX 1050" in \
            gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 1050
        elif "NVIDIA GeForce GTX 1060" in gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 1060
        elif "NVIDIA GeForce GTX 1070 Max-Q" in gaming_laptops_df["gpu_type"] or "NVIDIA GeForce GTX 1070" in \
            gaming_laptops_df["gpu_type"] or "NVIDIA GeForce GTX 1070 SLI" in gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 1070
        elif "NVIDIA GeForce GTX 1080" in gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 1080
        elif "NVIDIA GeForce GTX 1650" in gaming_laptops_df["gpu_type"] or "NVIDIA GeForce GTX 1650 Max-Q" in \
            gaming_laptops_df["gpu_type"] or "GeForce GTX 1650 Ti":
            gaming_laptops_df.loc[i, "gpu_type"] = 1650
        elif "NVIDIA GeForce GTX 1660 Ti" in gaming_laptops_df["gpu_type"] or "GeForce GTX 1660 Ti" in gaming_laptops_df[
        "gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 1660
        elif "NVIDIA GeForce RTX 2060" in gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 2060
        elif "NVIDIA GeForce RTX 2070" in gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 2070
        elif "NVIDIA GeForce RTX 2080" in gaming_laptops_df["gpu_type"] or "NVIDIA GeForce RTX 2080 Max-Q" in \
            gaming_laptops_df["gpu_type"]:
            gaming_laptops_df.loc[i, "gpu_type"] = 2080


for i in range(len(gaming_laptops_df["gpu_memory"])):
    if "-1" in gaming_laptops_df["gpu_memory"]:
        pass
    elif "shared system memory" in gaming_laptops_df["gpu_memory"]:
        gaming_laptops_df.loc[i, "gpu_memory"] = 1
    elif "2" in gaming_laptops_df["gpu_memory"]:
        gaming_laptops_df.loc[i, "gpu_memory"] = 2
    elif "3" in gaming_laptops_df["gpu_memory"]:
        gaming_laptops_df.loc[i, "gpu_memory"] = 3
    elif "4" in gaming_laptops_df["gpu_memory"] or "Up to 4" in gaming_laptops_df["gpu_memory"] or "4 GB GDDR5" in \
            gaming_laptops_df["gpu_memory"]:
        gaming_laptops_df.loc[i, "gpu_memory"] = 4
    elif "6" in gaming_laptops_df["gpu_memory"] or "6G GDDR6" in gaming_laptops_df["gpu_memory"]:
        gaming_laptops_df.loc[i, "gpu_memory"] = 6
    elif "16" in gaming_laptops_df["gpu_memory"]:
        gaming_laptops_df.loc[i, "gpu_memory"] = 16

# In[279]:


# Cleaning Gaming Laptop's General Memory
gaming_laptops_df.memory.unique()


# In[280]:
gaming_laptops_df["memory"].fillna("16 GB", inplace = True)

def clean_memory(df):
    # retrieve GB ints from raw data
    for i in range(len(df['memory'])):
        if type(df.loc[i, 'memory']) == int or type(df.loc[i, 'memory']) == 'numpy.64int':
            continue
        else:
            print(i, df.loc[i, 'memory'])
            df.loc[i, 'memory'] = int(df.loc[i, 'memory'].split(' ')[0])

    return df


# In[281]:


# In[282]:


# Cleaning Laptop's CPU Speed
gaming_laptops_df.cpu_speed.unique()


# In[284]:


def clean_cpu_speed(df):
    for i in range(len(df['cpu_speed'])):
        # missing values
        if df.loc[i, 'cpu_speed'] == -1:
            pass

        # case with extra words at beginning
        elif '(' in df.loc[i, 'cpu_speed']:
            df.loc[i, 'cpu_speed'] = float(df.loc[i, 'cpu_speed'].split('(')[1].replace(')', '').split(' ')[0])

        # when GHz is at the end
        elif 'GHz' in df.loc[i, 'cpu_speed']:
            df.loc[i, 'cpu_speed'] = float(df.loc[i, 'cpu_speed'].split(' ')[0])

    return df


# In[285]:


# Cleaning Gaming Laptops' Prices
float(gaming_laptops_df.loc[14, 'cpu_speed'].split('(')[1].replace(')', '').split(' ')[0])


# In[286]:


def clean_prices(df):
    for i in range(len(df['price'])):
        if type(df.loc[i, 'price']) == str:
            df.loc[i, 'price'] = float(df.loc[i, 'price'].replace(',', ''))

    return df


# In[287]:


# Cleaning Gaming Laptops' Storage
gaming_laptops_df.storage.unique()


# In[288]:


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


# In[289]:


# Write to astudy_df = clean_prices(study_df)
gaming_laptops_df = clean_cpu_speed(gaming_laptops_df)
gaming_laptops_df = clean_cores(gaming_laptops_df)
gaming_laptops_df = clean_storage(gaming_laptops_df)
gaming_laptops_df = clean_memory(gaming_laptops_df)
gaming_laptops_df = clean_screen_sizes(gaming_laptops_df)

gaming_laptops_df.to_csv("gaming_laptop_cleaned.csv")

# In[219]:


gaming_laptops_df.cpu_speed.unique()

