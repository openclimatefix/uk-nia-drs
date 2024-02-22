"""
This script renames a forecast file based on specific model details and date range.

It takes an existing forecast file, reads it into a pandas DataFrame, and then writes it out to a new file 
with a name that reflects the version ID, model names, model versions, and the start and end dates of the forecast period. 
This helps in organizing and identifying forecast files more easily.
"""

import shutil
import pandas as pd

dir = "data"
old_file = "full_pred_v5_2_xgb_pvnet_merge_formated_fix_ts.csv.gz"

v_id = "7"
model_name_1 = "national_xg"
model_name_2 = "pv_net"
model_version_1 = "1.0.23"
model_version_2 = "2.6.10"
start_date = "2016-12-01"
end_date = "2022-08-08"

new_file = (
    f"forecast_v={v_id}__"
    f"model_name_1={model_name_1}__"
    f"model_version_1={model_version_1}__"
    f"model_name_2={model_name_2}__"
    f"model_version_2={model_version_2}__"
    f"start_date={start_date}__"
    f"end_date={end_date}.csv.gz"
)

df = pd.read_csv(f"/{dir}/{old_file}")
df.to_csv(f"/{dir}/{new_file}", index=False)
