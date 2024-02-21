import pandas as pd


def blend_data(data_xg, data_pvnet, blend=True):

    data_xg["Init Time"] = pd.to_datetime(data_xg["Init Time"], utc=True)
    data_pvnet["Init Time"] = pd.to_datetime(data_pvnet["Init Time"], utc=True)

    data_combined = pd.merge(
        data_xg, data_pvnet, on="Init Time", how="left", suffixes=("", "_pvnet")
    )

    blend_ratios = {
        "7 Hour Forecast": (0.75, 0.25),
        "7.5 Hour Forecast": (0.5, 0.5),
        "8 Hour Forecast": (0.25, 0.75),
    }

    for col in data_pvnet.columns:
        if col in data_xg.columns and col != "Init Time":
            if blend and col in blend_ratios.keys():
                pvnet_ratio, xgb_ratio = blend_ratios[col]
                data_combined[col] = (data_combined[col + "_pvnet"] * pvnet_ratio) + (
                    data_combined[col] * xgb_ratio
                )
            else:
                data_combined[col] = data_combined[col + "_pvnet"]
            data_combined.drop(columns=[col + "_pvnet"], inplace=True)

    data_combined = data_combined[
        data_combined["Init Time"] >= "2020-01-01 03:00:00+00:00"
    ]
    data_combined = data_combined[
        data_combined["Init Time"] <= "2022-08-08 08:00:00+00:00"
    ]

    data_combined_shift = data_combined.copy()
    # As XGb makes a 0 hour forecast but PVNet does not, its better to use the forecast from PVnet 30 mins ahead
    # for the successive init time, 30 mins later.
    data_combined_shift["0 Hour Forecast"] = data_combined_shift[
        "0.5 Hour Forecast"
    ].shift(1)

    # Now to create the other bit of the dataset
    xgb_p2 = data_xg.copy()
    # Needs to be less than but not including this date
    xgb_p2 = xgb_p2[xgb_p2["Init Time"] < "2020-01-01 03:00:00+00:00"]
    merged_data = pd.concat([xgb_p2, data_combined_shift])

    return merged_data


# Two step merging process for the datasets
data_xg = pd.read_csv(
    "../../data/full_predictions_cross_validation_v4_without_prob_with_30min_unormalised.csv"
)
data_pvnet = pd.read_csv("../../data/pvnet_predicitons_2021-2023_preformat_v2.csv")

print("Merging")
merged_data = blend_data(data_xg, data_pvnet, blend=True)
merged_data.to_csv("../../data/full_pred_v6_3_xgb_pvnet_blended.csv", index=False)
print("Save")
