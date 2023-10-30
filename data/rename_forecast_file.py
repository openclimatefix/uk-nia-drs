import shutil

dir = "data"
old_file = "formatted_forecasts_v2.csv.gz"

v_id = "4"
model_name = "national_xg"
model_version = "1.0.13"
start_date = "2016-12-01"
end_date = "2022-08-08"

new_file = (
    f"forecast_v={v_id}__"
    f"model_name={model_name}__"
    f"model_version={model_version}__"
    f"start_date={start_date}__"
    f"end_date={end_date}.csv.gz"
)

import pandas as pd
df = pd.read_csv(f"./{dir}/{old_file}")
df.to_csv(f"./{dir}/{new_file}", index=False)


