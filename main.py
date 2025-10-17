import pandas as pd
import matplotlib.pyplot as plt


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

##Function to create a scatter plot 
def create_scatter_plot(df, x_col, y_col, title):
   plt.figure(figsize = (10, 6))
   plt.scatter(df[x_col], df[y_col], alpha=0.7, edgecolors='w')
   plt.title(title)
   plt.xlabel(x_col)
   plt.ylabel(y_col)
   plt.grid(True)
   plt.tight_layout()
   plt.show()




   
   

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

   create_scatter_plot(data, 'BB', 'SO', 'Walk (BB) vs Strikeout (SO) Ratio')
   create_scatter_plot(data, 'HR', 'AB', 'Home Runs (HR) vs At Bats (AB) Ratio')
