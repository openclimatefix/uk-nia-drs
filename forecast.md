# Forecasts

**Forecast** will have the following fields:

- start_datetime_utc: datetime - the start datetime of the period
- end_datetime_utc: datetime - the end datetime of the period
- forecasting_creation_datetime_utc: datetime, when the forecast is made
- generation_mw: float - the solar generation value

The first version of forecast is from `national_xg` version 1.0.13. 
This was run using cross validation. Dates are from `2017-01-01` to `2022-01-01` 

- `formatted_forecasts.csv.gz` was sent on 2023-08-15. Error it didnt contain "generation_mw" column
- `formatted_forecasts_cross_validation_v2.csv` was sent on 2023-08-16. 
- `formatted_forecasts_v2.csv` was sent on 2023-08-30. 

New file format
- `forecast_v=3__model_name=national_xg__model_version=1.0.13__start_date=2016-12-01__end_date=2022-08-08.csv.gz` was sent on 2023-10-05. 
- `forecast_v=4__model_name=national_xg__model_version=1.0.13__start_date=2016-12-01__end_date=2022-08-08.csv.gz` was sent on 2023-10-05, with the correctly named file in the zip folder.

Extended forecast horizon to 40 Hours
- `forecast_v=5__model_name=national_xg__model_version=1.0.23__start_date=2016-12-01__end_date=2022-08-08.csv.gz` was sent on 2023-11-13. Dates are from `2016-12-01 to 2022-08-08`. Fixed missing day of data on `2016-12-31`, `2017-12-31`, `2018-12-31`, `2019-12-31` and `2020-12-31`.

Of the ~100,000 forecast made there were ~100 gaps in the creation times.
The gaps were distributed as follows:

| Gap length           | Number of gaps | Comments                                                                            | 
|----------------------|----------------|-------------------------------------------------------------------------------------|
| 1 hour               | 81             | These are on 2017-03-16, 2017-03-17, 2017-05-16, 2019-07-01, 2019-07-02             |
| 3 hour               | 2              | These are on 2018-12-31 and 2019-12-31                                              |
| 6.5 hour             | 6              | These are on 2019-02-07, 2019-02-13, 2019-02-18, 2019-02-21, 2019-02-22, 2019-02-23 |
| 12.5 hour            | 4              | There are on 2019-02-05, 2019-02-06, 2019-02-12, 2019-02-20|                        |
| 1 day and 30 minutes | 1              | This was on 2019-02-16                                                              |
| 53 days              | 1              | This was on 2021-11-08                                                              |

This largest gap on 2021-11-08 is due to missing NWP data.

Probabilistic forecasts
- `forecast_v=6__model_name=national_xg__model_version=1.0.23__start_date=2016-12-01__end_date=2022-08-08.csv.gz` was sent on 2023-11-28. Dates are from `2016-12-01 to 2022-08-08`. This contains the normal, p10 and p90 generation values for the same model used in v5, with the corresponding forecasts under each column: `generation_mw`, `generation_mw_p10` and `generation_mw_p90`. The gaps in creation time remain the same as shown in the table above, for v5.

PVNet and NationalXG merged forecast
*  `forecast_v=7__model_name_1=national_xg__model_version_1=1.0.23__model_name_2=pv_net__model_version_2=2.6.10__start_date=2016-12-01__end_date=2022-08-08.csv.gz` was sent over on 2024-02-06. 
* Dates are from `2016-12-01 to 2022-08-08`. 
* This contains a sinlge generation forecast that uses PVNet forecasts from 0-8 hours and then national xg from 8.5 to 40 hours. 
* This forecast has a 30 minute resolution. 
* PVNet forecasts were generated from `2020-01-01` to `2022-08-08`. 
* PVNet was trained on data from `2020-01-01` to `2022-05-01`.

* MAE values for forecast horizon:
  - MAE: 115.40 MW for 0
  - MAE: 149.40 MW for 1
  - MAE: 188.35 MW for 2
  - MAE: 192.72 MW for 4
  - MAE: 200.90 MW for 8
  - MAE: 224.80 MW for 12
  - MAE: 233.91 MW for 24
  - MAE: 252.83 MW for 36

Improved PVNet and NationalXG merged forecast
* `forecast_v=8__model_name_1=national_xg__model_version_1=1.0.23__model_name_2=pv_net__model_version_2=3.0.1__start_date=2016-12-01__end_date=2022-08-08.csv.gz` was sent over on 2024-03-28.
* Dates are from `2016-12-01 to 2022-08-08`. 
* This contains a single generation forecast that uses PVNet forecasts from 0-6.5 hours, a blend is used between 7-8 hours and then national xg from 8.5 to 40 hours. 
* This forecast has a 30 minute resolution. 
* National xg is used for all of 2017.
* A newer version of PVNet has been used for this backtest referred to as PVNet Summation Model.
* PVNet with satellite is used from `2019-01-01` to `2022-08-08`.
* PVNet without satellite is used for 2018.
* PVNet was trained on data from `2020-01-01` to `2022-05-01`.
* p10 and p90 probabilistic forecasts are provided.
* The gaps present are the same as reported in v5.

* MAE values for forecast horizon:
  - MAE: 98.33 MW for 0
  - MAE: 111.02 MW for 1
  - MAE: 128.17 MW for 2
  - MAE: 132.18 MW for 4
  - MAE: 192.36 MW for 8
  - MAE: 224.80 MW for 12
  - MAE: 233.91 MW for 24
  - MAE: 252.83 MW for 36