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
- `forecast_v=6__model_name=national_xg__model_version=1.0.23__start_date=2016-12-01__end_date=2022-08-08.csv` was sent on 2023-11-28. Dates are from `2016-12-01 to 2022-08-08`. This contains the normal, p10 and p90 generation values for the same model used in v5, with the corresponding forecasts under each column: `generation_mw`, `generation_mw_p10` and `generation_mw_p90`. The gaps in creation time remain the same as shown in the table above, for v5.