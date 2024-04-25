"""
This script is designed to unnormalize forecast data by merging it with PVLive capacity data. The process involves several key steps:

- Loading forecast data from a CSV file.
- Loading PVLive capacity data from a CSV file and converting the 'end_datetime_utc' column to datetime format.
- Unnormalizing the forecast data by merging it with the PVLive data based on the 'Init Time' and 'end_datetime_utc' columns.
- For each 'Hour Forecast' column, converting negative forecasts to 0 and scaling the forecasts by the 'installedcapacity_mwp' column from the PVLive data.
- Dropping unnecessary columns related to capacity and datetime from the merged dataset.
- Saving the unnormalized forecast data to a new CSV file.

This script ensures that the forecast data is adjusted according to actual installed capacity, providing a more accurate representation of expected generation.
"""

import pandas as pd

# load data
print("Loading Forecast data")
data = pd.read_csv(
    "../../data/full_predictions_cross_validation_v8_(from_v4)_prob_full_formated_xg.csv"
)

# join with pvlive capacity data
print("Loading PVLive data")
pvlive = pd.read_csv("../../pvlive_2016_2023.csv")
pvlive["end_datetime_utc"] = pd.to_datetime(pvlive["end_datetime_utc"])

# unnormalize data
print("Unnormalizing data")
data["Init Time"] = pd.to_datetime(data["Init Time"])
data["Init Time"] = data["Init Time"].dt.tz_localize("UTC")
data = data.merge(pvlive, left_on="Init Time", right_on="end_datetime_utc")
for c in data.columns:
    if "Hour Forecast" in c:
        data[c] = data[c].astype(float)
        idx_night = data[c] <= 0.000234
        data.loc[idx_night, c] = 0
        data[c] = data[c] * data["installedcapacity_mwp"]

# drop columns
data.drop(
    columns=[
        "installedcapacity_mwp",
        "capacity_mwp",
        "start_datetime_utc",
        "end_datetime_utc",
    ],
    inplace=True,
)

data.to_csv(
    "../../data/full_predictions_cross_validation_v8_(from_v4)_prob_full_formated_xg_unnorm.csv",
    index=False,
)
