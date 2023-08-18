# Forecasts

**Forecast** will have the following fields:

- start_datetime_utc: datetime - the start datetime of the period
- end_datetime_utc: datetime - the end datetime of the period
- forecasting_creation_datetime_utc: datetime, when the forecast is made
- generation_mw: float - the solar generation value

The first version of forecast is from `national_xg` version 1.0.13. 
This was run using cross validation. Dates are from `2017-01-01` to `2022-01-01` 

- `formatted_forecasts.csv.gz` was sent on 2023-08-15. Error it didnt contain "generation_mw" column

- `formatted_forecasts_cross_validation_v2.csv.gz` was sent on 2023-08-16. 