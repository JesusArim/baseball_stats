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


def create_box_plot(df, attributes, xlabel: str, ylabel: str, title: str):
   plt.figure(figsize = (10, 6))
   data = df[attributes]
   plt.boxplot(data, vert=False, patch_artist=True)
   plt.yticks(range(1, 5), attributes)
   plt.xlabel(xlabel)
   plt.ylabel(ylabel)
   plt.title(title)
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

   cols_name = ['Singles', 'Doubles', 'Triples', 'HR']
   x_label = 'Hits'
   y_label = 'Hit Type'
   box_plot_title = 'Distribution of Hits'

   create_box_plot(data, cols_name, x_label, y_label, box_plot_title)


   """ Calculate averages and remove outliers"""
   
   #Remove players with 0 walks
   data = data[data['BB'] != 0]

   #Remove players with 0 Strikeouts from de Dataframe 
   data = data[data['SO'] != 0]


   #Create column with Strikesout/Walk Ratio %
   data['SO/BB'] = data['SO'] / data['BB']

   #Use DataFrame functionality to calculate the mean 
   average_singles = data['Singles'].mean()
   average_doubles = data['Doubles'].mean()
   average_triples = data['Triples'].mean()
   average_hr = data['HR'].mean() 

   max_SO_BB = data['SO/BB'].max()
   min_SO_BB = data['SO/BB'].min()

   print(f'Singles: {average_singles}')
   print(f'Doubles: {average_doubles}')
   print(f'Triples: {average_triples}')
   print(f'Home Runs: {average_hr}')
   
   
