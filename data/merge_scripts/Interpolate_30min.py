import pandas as pd

df_xg = pd.read_csv("/home/zak/projects/DRS/data/full_predictions_cross_validation_v4_without_prob_full.csv")

# Generate half-hourly forecasts by averaging between each hourly forecast
def generate_half_hourly_forecasts(df):
    hourly_columns = [col for col in df.columns if 'Hour Forecast' in col]
    for i in range(len(hourly_columns)-1):
        current_hour = hourly_columns[i]
        next_hour = hourly_columns[i+1]
        half_hour_column = f'{i + 0.5} Hour Forecast'
        df[half_hour_column] = (df[current_hour] + df[next_hour]) / 2

    # Reorder columns to maintain chronological order
    ordered_columns = ['Init Time']
    for i in range(len(hourly_columns)-1):
        ordered_columns.append(f'{i} Hour Forecast')
        ordered_columns.append(f'{i + 0.5} Hour Forecast')
    ordered_columns.append(f'{len(hourly_columns)-1} Hour Forecast')  # Add the last hour forecast column
    return df[ordered_columns]

df_xg_temp = df_xg.copy()

df_xg_30 = generate_half_hourly_forecasts(df_xg_temp)

df_xg_30.to_csv("/home/zak/projects/DRS/data/full_predictions_cross_validation_v4_without_prob_with_30min_0.csv", index=False)
