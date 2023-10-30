import pandas as pd

forecast_file = 'forecast_v=4__model_name=national_xg__model_version=1.0.13__start_date=2016-12-01__end_date=2022-08-08.csv.gz'



df = pd.read_csv(f"./data/{forecast_file}")

# group by init time
creation_times = df[['forecasting_creation_datetime_utc']]
creation_times['forecasting_creation_datetime_utc'] = pd.to_datetime(creation_times['forecasting_creation_datetime_utc'])
creation_times['count'] = 1
creation_times_sum = creation_times.groupby('forecasting_creation_datetime_utc').sum()

mask = creation_times_sum['count'] != 37
sum(mask)


# get unique init times
init_times = pd.DataFrame(df['forecasting_creation_datetime_utc'].unique(), columns=['forecasting_creation_datetime_utc'])
init_times['forecasting_creation_datetime_utc'] = pd.to_datetime(init_times['forecasting_creation_datetime_utc'])

# find the differences
init_times['next_forecasting_creation_datetime_utc']= init_times.shift(-1)
init_times['diff'] = init_times['next_forecasting_creation_datetime_utc'] - init_times['forecasting_creation_datetime_utc']

# remove any 30 minute gaps
gaps = init_times[init_times['diff'] != pd.Timedelta('30T')]

# look at distribution of gaps
gaps['count'] = 1
gaps_sum = gaps[['diff','count']].groupby('diff').sum()
