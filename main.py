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
   

def create_list_data(frame, column_name):
   list_data = [data for data in frame[column_name]]
   return list_data

def display_info_df(frame):
   print(frame.info())


   
   

if __name__=='__main__':
   path_f = "sports_data_missing.csv"
   data = read_csv_file(path_f)
   print(data.head())
   display_info_df(data)

   data = data.fillna(data.mean(numeric_only=True))
   data = data.round(1)

   ##Inspect the cleaned data
   display_info_df(data)
   missing_values = data.isnull().sum()
   print(f'Missing values on each column:\n {missing_values}')
