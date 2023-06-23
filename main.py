import pandas as pd

print ("Hello wld")

melbourne_file_path = '/Volumes/Feina/ML/melb_data.csv'

melbourne_data = pd.read_csv(melbourne_file_path)

melbourne_data.describe()