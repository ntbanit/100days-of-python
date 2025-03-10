# import os 
# script_dir = os.path.dirname(os.path.abspath(__file__))
# os.chdir(script_dir)

import pandas 
data = pandas.read_csv("squirrel_data.csv")

grouped_df = data.groupby('Primary Fur Color').size().reset_index(name='Counts')
# print(grouped_df)
pandas.DataFrame(grouped_df).to_csv("squirrel_count.csv")