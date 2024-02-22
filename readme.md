# DRS NIA project

The idea of this project is to prove Solar forecast to the DRS (Dynamic Reserve Settings) NIA project.
More info [here](https://www.smithinst.co.uk/insights/national-grid-eso-and-smith-institute-begin-pioneering-drs-project/)

First OCF will provide PVlive data, and secondly we will provide OCF Forecasts

**PVLive** with the following fields:

- start_datetime_utc: datetime - the start datetime of the period
- end_datetime_utc: datetime - the end datetime of the period
- generation_mw: float - the solar generation value
- capacity_mwp: float - The estimated capacity of the system
- installedcapacity_mwp: float - The installed capacity (this changes is time)

**Forecast** with the following fields:

- start_datetime_utc: datetime - the start datetime of the period
- end_datetime_utc: datetime - the end datetime of the period
- forecasting_creation_datetime_utc: datetime, when the forecast is made
- generation_mw: float - the solar generation value

## file format

The file format for single model files is a csv file: 
`forecast_v={v_id}__model_name={model_name}__model_version={model_version}__start_date={start_date}__end_date={end_date}.csv`

where 
- forecast_v: int, fore forecast version
- model name: string, the ml model used e.e.g national_xg
- model version: string, the ml model version e.g. 0.0.1
- start and end dates of the forecast: YYYY-MM-DD

For files that utilise multiple models, the following format will be used:
`forecast_v={v_id}__model_name_1={model_name_1}__model_version_1={model_version_1}__model_name_2={model_name_2}__model_version_2={model_version_2}__start_date={start_date}__end_date={end_date}.csv.gz`