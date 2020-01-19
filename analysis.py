import pandas as pd

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 15)

study_df = pd.read_csv('study_laptops_cleaned.csv', sep=',')

# calculate weighted average for each value in each factor
# get budget from matt's end
def wa_price(row, budget):


# do this for each data point - loop thru everything
for rnum in list(study_df.index):
    study_df.loc[rnum, 'price'] = wa_price(rnum, budget)

