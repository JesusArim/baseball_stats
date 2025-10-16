import pandas as pd


def read_csv_file(path_file: str):
   if not path_file:
      raise "No path file found"
   try:
      data = pd.read_csv(path_file)
   except FileNotFoundError as e:
      return f'Error: {e}'
   else:
      return data
   

if __name__=='__main__':
   path_f = "sports_data_missing.csv"
   data = read_csv_file(path_f)
   print(data.head())
   print(data.info())