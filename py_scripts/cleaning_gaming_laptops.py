import pandas as pd
import numpy as np
import re

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 15)

# Storing Gaming Laptops info
gaming_laptops_df = pd.read_csv("../data/gaming_laptops_raw.csv", sep=",")
gaming_laptops_df = gaming_laptops_df.fillna(-1)  # Will get back to later

# Converting Rating Values into Integers
def clean_ratings():
    for i in range(len(gaming_laptops_df["rating"])):
        gaming_laptops_df["rating"] = int(gaming_laptops_df.loc[i, "rating"])

# Converting Screen Size Values into Floats
def clean_screen_sizes():
    # turn all screen sizes into floats
    for i in range(len(gaming_laptops_df['screen'])):
        if gaming_laptops_df.loc[i, 'screen'] == 'No':
            gaming_laptops_df.loc[i, 'screen'] = -1
        if type(gaming_laptops_df.loc[i, 'screen']) == str:
            gaming_laptops_df.loc[i, 'screen'] = float(gaming_laptops_df.loc[i, 'screen'].split(' ')[0].replace('"', ''))

def clean_cores():
    for i in range(len(gaming_laptops_df['cores'])):
        if gaming_laptops_df.loc[i, 'cores'] == -1:
            gaming_laptops_df.loc[i, 'cores'] = 6
        elif 'Dual' in gaming_laptops_df.loc[i, 'cores']:
            gaming_laptops_df.loc[i, 'cores'] = 2
        elif 'Quad' in gaming_laptops_df.loc[i, 'cores'] or '4' in gaming_laptops_df.loc[i, 'cores']:
            gaming_laptops_df.loc[i, 'cores'] = 4
        elif 'Six' in gaming_laptops_df.loc[i, 'cores'] or '6' in gaming_laptops_df.loc[i, 'cores']:
            gaming_laptops_df.loc[i, 'cores'] = 6
        elif "8" in gaming_laptops_df.loc[i, "cores"]:
            gaming_laptops_df.loc[i, "cores"] = 8


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


def clean_gpu_memory():
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


def clean_memory():
    # retrieve GB ints from raw data
    for i in range(len(gaming_laptops_df['memory'])):
        if type(gaming_laptops_df.loc[i, 'memory']) == int or type(gaming_laptops_df.loc[i, 'memory']) == 'numpy.64int':
            continue
        else:
            gaming_laptops_df.loc[i, 'memory'] = int(gaming_laptops_df.loc[i, 'memory'].split(' ')[0])


def clean_cpu_speed():
    for i in range(len(gaming_laptops_df['cpu_speed'])):
        # missing values
        if gaming_laptops_df.loc[i, 'cpu_speed'] == -1:
            pass

        # case with extra words at beginning
        elif '(' in gaming_laptops_df.loc[i, 'cpu_speed']:
            gaming_laptops_df.loc[i, 'cpu_speed'] = float(gaming_laptops_df.loc[i, 'cpu_speed'].split('(')[1].replace(')', '').split(' ')[0])

        # when GHz is at the end
        elif 'GHz' in gaming_laptops_df.loc[i, 'cpu_speed']:
            gaming_laptops_df.loc[i, 'cpu_speed'] = float(gaming_laptops_df.loc[i, 'cpu_speed'].split(' ')[0])

def clean_prices():
    for i in range(len(gaming_laptops_df['price'])):
        if type(gaming_laptops_df.loc[i, 'price']) == str:
            gaming_laptops_df.loc[i, 'price'] = float(gaming_laptops_df.loc[i, 'price'].replace(',', ''))
        elif gaming_laptops_df.loc[i, 'price'] == -1:
            gaming_laptops_df.loc[i, 'price'] = 1493.64  # fill missing with the mean price

def clean_storage():
    for i in range(len(gaming_laptops_df['storage'])):
        if gaming_laptops_df.loc[i, 'storage'] != -1:
            # gaming_laptops_df.loc[i, 'storage'] = re.split('[A-z]|,', gaming_laptops_df.loc[i, 'storage'])[0]
            gaming_laptops_df.loc[i, 'storage'] = gaming_laptops_df.loc[i, 'storage'].replace('+', ',')
            storage_split_list = re.split('[A-z]|,', gaming_laptops_df.loc[i, 'storage'])

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
            gaming_laptops_df.loc[i, 'storage'] = storage_int

## MAIN
clean_prices()
clean_ratings()
clean_cpu_speed()
clean_cores()
clean_storage()
clean_memory()
clean_gpu_memory()
clean_gpu_type()
clean_screen_sizes()

gaming_laptops_df.to_csv("gaming_laptop_cleaned.csv")