"""
This file joins the raw csv produced from a an xgboost backtest

The input files should be saved in the results folder with the format"
- "Backtest_horizon_{HORIZON}_year_{YEAR}.csv"
- where HORIZON and YEAR correspond to the relative variables for the backtest.
- base_directory should be changed to the respective location to where the csvs are.

The output csv file will have the following columns:
- Init Time
- 0 Hour Forecast
- 1 Hour Forecast
....
- 36 Hour Forecast
"""

import pandas as pd
import os

# change base_directory to reflect the location of the data
base_directory = "./uk-pv-national-xg/results"
final_df = pd.DataFrame()

# loop through the years and horizons
for year in range(2016, 2023):
    year_df = pd.DataFrame()
    print("Year:", year)
    
    for horizon in range(41):
        print("Horizon:", horizon)
        file_name = f"Backtest_test_horizon_{horizon}_year_{year}.csv"
        file_path = os.path.join(base_directory, file_name)
        
        # check if the file exists
        if os.path.exists(file_path):
            
            df = pd.read_csv(file_path)
            
            # convert the 'Unnamed: 0' column to datetime and set it as the index then drop
            df['Init Time'] = pd.to_datetime(df['Unnamed: 0'])
            df.set_index('Init Time', inplace=True)
            df.drop(columns=['Unnamed: 0'], inplace=True) 
            
            # filter rows where the year matches, as the data is cross-validated
            df = df[df.index.year == year]
            
            # rename the 'pred' column according to the horizon
            df.rename(columns={'pred': f'{horizon} Hour Forecast'}, inplace=True)
        
            if horizon == 0:
                year_df = df[[f'{horizon} Hour Forecast']]
            else:
                # concatenate the forecast columns to the year_df
                year_df = year_df.join(df[f'{horizon} Hour Forecast'])

    # concatenate the year's data to the final DataFrame
    if not year_df.empty:
        final_df = pd.concat([final_df, year_df])

# reset index to make a Init time a column
final_df = final_df.reset_index()

# drop nans
print("removing nans")
df_cleaned = final_df.dropna()

print("saving to csv")
df_cleaned.to_csv("./data/full_predictions_cross_validation_v3.csv", index=False)
print("done")