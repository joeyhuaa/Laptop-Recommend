import numpy as np
import pandas as pd

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 10)

# df.loc[] examples
# df.loc[0]  # 0th row
# df.loc[[0,5]]  # 0th and 5th rows
# df.loc[0:5] # 0th-5th rows

# csv into pd data frame
study_df = pd.read_csv('newegg_study_laptops.csv', sep=',')
gaming_df = pd.read_csv('newegg_gaming_laptops.csv', sep=',')

# group datasets for ease of cleaning
dfs = {'study': study_df, 'gaming': gaming_df}

for df in dfs.values():
    # turn all prices into floats
    for i in range(len(df['price'])):
        if type(df.loc[i, 'price']) == str:
            df.loc[i, 'price'] = float(df.loc[i, 'price'].replace(',', ''))

    # print number of missing values in each column
    for col in df.columns:
        print(col, df[df[col].isna()].shape)
    print('~'*20)



