"""
This script analyzes forecasting data to identify and report any missing dates or gaps. It includes functionality to:

- Load forecasting data from a CSV file.
- Determine the time intervals between forecast entries.
- Identify any intervals that are larger than expected.
- Summarize and print the findings.
- Save the details of these gaps for further examination.
"""

import pandas as pd

df = pd.read_csv(
    "../../data/forecast_v=8__model_name_1=national_xg__model_version_1=1.0.23__model_name_2=pv_net__model_version_2=3.0.1__start_date=2016-12-01__end_date=2022-08-08.csv.gz"
)

# get unique init times
init_times = pd.DataFrame(
    df["forecasting_creation_datetime_utc"].unique(),
    columns=["forecasting_creation_datetime_utc"],
)
init_times["forecasting_creation_datetime_utc"] = pd.to_datetime(
    init_times["forecasting_creation_datetime_utc"]
)

# find the differences
init_times["next_forecasting_creation_datetime_utc"] = init_times.shift(-1)
init_times["diff"] = (
    init_times["next_forecasting_creation_datetime_utc"]
    - init_times["forecasting_creation_datetime_utc"]
)

# remove any 30 minute gaps
gaps = init_times[init_times["diff"] != pd.Timedelta("30T")]

# look at distribution of gaps
gaps["count"] = 1
gaps_sum = gaps[["diff", "count"]].groupby("diff").sum()

# Print summary of gaps
print(gaps_sum)

# Print dates where there are gaps
print("Dates with gaps:")
print(gaps[["forecasting_creation_datetime_utc", "diff"]])

# Save the gaps information to a CSV file
gaps.to_csv("../../data/forecast_gaps_v7_2.csv", index=False)
print("Gaps information saved")
