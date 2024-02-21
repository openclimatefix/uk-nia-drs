import pandas as pd

# load data
print("Loading Forecast data")
data = pd.read_csv("/home/zak/projects/DRS/data/full_predictions_cross_validation_v4_without_prob_with_30min.csv")

# join with pvlive capacity data
print("Loading PVLive data")
pvlive = pd.read_csv("/home/zak/projects/DRS/uk-nia-drs/pvlive_2016_2022.csv")
pvlive["end_datetime_utc"] = pd.to_datetime(pvlive["end_datetime_utc"])

# unnormalize data
print("Unnormalizing data")
data["Init Time"] = pd.to_datetime(data["Init Time"])
data['Init Time'] = data['Init Time'].dt.tz_localize('UTC')
data = data.merge(pvlive, left_on="Init Time", right_on="end_datetime_utc")
for c in data.columns:
    if "Hour Forecast" in c:
        data[c] = data[c].astype(float)
        idx_night = data[c] <=0.000234
        data.loc[idx_night, c] = 0
        data[c] = data[c] * data["installedcapacity_mwp"]

# drop columns
data.drop(columns=["installedcapacity_mwp", "capacity_mwp", "start_datetime_utc", "end_datetime_utc"], inplace=True)

data.to_csv("/home/zak/projects/DRS/data/full_predictions_cross_validation_v4_without_prob_with_30min_unormalised.csv", index=False)