## Missing init times

We are looking at the forecast creation times in 
`forecast_v=4__model_name=national_xg__model_version=1.0.13__start_date=2016-12-01__end_date=2022-08-08.csv.gz`
 and seeing if there are missing init times. 
We want to also look to make sure all forecasts are 36 hours long

## Forecast horizons

We found all forecasts were 36 hours long, no missing ones. 

```python
import pandas as pd

df = pd.read_csv('data/forecast_v=4__model_name=national_xg__model_version=1.0.13__start_date=2016-12-01__end_date=2022-08-08.csv.gz')

# group by init time
creation_times = pd.DataFrame(pd.to_datetime(df['forecasting_creation_datetime_utc']), columns=['forecasting_creation_datetime_utc'])
creation_times['count'] = 1
creation_times_sum = creation_times.groupby('forecasting_creation_datetime_utc').sum()

mask = creation_times_sum['count'] != 37
```

## Gaps in forecast creation times

We also looked at the gaps in the creation times of the forecasts. 
We found a few. 

Of the ~100,000 forecast made there were ~100 gaps in the creation times.
The gaps were distributed as follows:

| Gap length           | Number of gaps | Comments                                                                            | 
|----------------------|----------------|-------------------------------------------------------------------------------------|
| 1 hour               | 81             | These are on 2017-03-16, 2017-03-17, 2017-05-16, 2019-07-01, 2019-07-02             |
| 6.5 hour             | 6              | These are on 2019-02-07 , 2019-02-13, 2019-02-18, 2019-02-21, 2019-02-22, 2019-02-23 |
| 12.5 hour            | 4              | There are on 2019-02-05, 2019-02-06, 2019-02-12, 2019-02-20|                          |
| 1 day                | 5              | These was on 2016-12-31, 2017-12-31, 2018-12-31, 2019-12-31 and 2020-12-31          |
| 1 day and 30 minutes | 1              | This was on 2019-02-16                                                              |
| 53 days              | 1              | This was on 2021-11-08                                                              |

This largest gap on 2021-11-08 is due to missing NWP data. 

I believe the `1 day` gaps are a bugs, and can be fixed, but I think the rest are due to missing NWP data. 


```python
import pandas as pd

df = pd.read_csv('data/forecast_v=4__model_name=national_xg__model_version=1.0.13__start_date=2016-12-01__end_date=2022-08-08.csv.gz')


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


```