import pandas as pd

# set plotly as backend plotting
pd.options.plotting.backend = "plotly"


df = pd.read_csv("data/forecast_v=6__model_name=national_xg__model_version=1.0.23__start_date=2016-12-01__end_date=2022-08-08.csv.gz")

pvlive_df = pd.read_csv("pvlive_2016_2022.csv")

# make start_datetime_utc and forecasting_creation_datetime_utc datetimes
df['start_datetime_utc'] = pd.to_datetime(df['start_datetime_utc'])
df['end_datetime_utc'] = pd.to_datetime(df['end_datetime_utc'])
df['forecasting_creation_datetime_utc'] = pd.to_datetime(df['forecasting_creation_datetime_utc'])
pvlive_df['start_datetime_utc'] = pd.to_datetime(pvlive_df['start_datetime_utc'])
pvlive_df['end_datetime_utc'] = pd.to_datetime(pvlive_df['end_datetime_utc'])

horizons = [0,1,2,4,8,12,24,36]
maes = {}


for horizon in horizons:
    df_subset = df[df['start_datetime_utc'] - df['forecasting_creation_datetime_utc'] == pd.Timedelta(f'{horizon} hours')]

    # merge with pv live
    df_subset = df_subset.merge(pvlive_df, left_on='start_datetime_utc', right_on='end_datetime_utc')


    # first 1000 values
    # df_subset_plot = df_subset.head(1000)
    # df_subset_plot = df_subset_plot[['start_datetime_utc', 'generation_mw_x', 'generation_mw_y']]
    # # set index as start_datetime_utc
    # df_subset_plot.set_index('start_datetime_utc', inplace=True)
    # # plot the first 1000 values
    # fig = df_subset_plot.plot(title=f'Generation vs Forecast for {horizon} Hour Forecast', labels={'value': 'Generation (MW)', 'index': 'Start Datetime UTC'})
    # fig.show(renderer='browser')

    mae = (df_subset['generation_mw_x'] - df_subset[f'generation_mw_y']).abs().mean()
    maes[horizon] = mae

for k, mae in maes.items():
    print(f'MAE: {mae:.2f} MW for {k} hours')