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

## file format

The file format is a csv file: 
`forecast_v={v_id}__model_name={model_name}__model_version={model_version}__start_date={start_date}__end_date={end_date}.csv`

where 
- forecast_v: int, fore forecast version
- model name: string, the ml model used e.e.g national_xg
- model version: string, the ml model version e.g. 0.0.1
- start and end dates of the forecast: YYYY-MM-DD
