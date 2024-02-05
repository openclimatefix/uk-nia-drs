import pandas as pd

# Two step merging process for the datasets
data = pd.read_csv("/home/zak/projects/DRS/data/full_predictions_cross_validation_v4_without_prob_with_30min_unormalised.csv")
data_pvnet = pd.read_csv("/home/zak/projects/DRS/data/pvnet_predicitons_2021-2023_preformat_v2.csv")

data['Init Time'] = pd.to_datetime(data['Init Time'], utc=True)
data_pvnet['Init Time'] = pd.to_datetime(data_pvnet['Init Time'], utc=True)

data_combined_s1 = pd.merge(data, data_pvnet, on="Init Time", how="left", suffixes=('', '_pvnet'))

blend_ratios = {
    '7 Hour Forecast': (0.75, 0.25),
    '7.5 Hour Forecast': (0.5, 0.5),
    '8 Hour Forecast': (0.25, 0.75)
}

def blend_data(data_combined, blend=True):
    for col in data_pvnet.columns:
        if col in data.columns and col != "Init Time":
            if blend and col in blend_ratios.keys():
                pvnet_ratio, xgb_ratio = blend_ratios[col]
                data_combined[col] = (data_combined[col + '_pvnet'] * pvnet_ratio) + (data_combined[col] * xgb_ratio)
            else:
                data_combined[col] = data_combined[col + '_pvnet']
            data_combined.drop(columns=[col + '_pvnet'], inplace=True)
    
    data_combined = data_combined[data_combined['Init Time'] >= '2020-01-01 03:00:00+00:00']
    data_combined = data_combined[data_combined['Init Time'] <= '2022-08-08 08:00:00+00:00']
    return data_combined

data_combined_s1 = blend_data(data_combined_s1, blend=False)

data_combined_s1_shift = data_combined_s1.copy()

data_combined_s1_shift['0 Hour Forecast'] = data_combined_s1_shift['0.5 Hour Forecast'].shift(1)

data_combined_s1_shift
