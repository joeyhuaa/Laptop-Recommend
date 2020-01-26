import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 15)

study_df = pd.read_csv('../data/study_laptops_cleaned.csv', sep=',', encoding='latin')
gaming_df = pd.read_csv('../data/gaming_laptops_cleaned.csv', sep=',', encoding='latin')
all_df = pd.concat([study_df, gaming_df]).reset_index(drop=True)


## DATA VISUALIZATION
# histogram
def histogram(data, fc, ec):
    plt.hist(data, facecolor=fc, edgecolor=ec)
    plt.show()

# pie chart
def pie(percentages, data):
    plt.pie(percentages, labels=data, autopct='%.2f', explode=[0.1]*len(data))
    plt.show()

# histogram(all_df.price, 'orangered', 'black')

mem_percs = [all_df[all_df.memory==n].shape[0] / 966 for n in all_df.memory.unique()]
pie(mem_percs, all_df.memory.unique())


