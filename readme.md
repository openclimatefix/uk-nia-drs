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