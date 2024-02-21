import pandas as pd
import pytest
from data.merge_scripts.Interpolate_30min import generate_half_hourly_forecasts  # Adjust the import path as necessary

def test_generate_half_hourly_forecasts():
    # Create a sample DataFrame
    data = {
        'Init Time': ['2020-01-01 00:00:00', '2020-01-01 01:00:00', '2020-01-01 02:00:00', '2020-01-01 03:00:00'],
        '0 Hour Forecast': [100, 200, 300, 400],
        '1 Hour Forecast': [150, 250, 350, 450],
        '2 Hour Forecast': [200, 300, 400, 500],
        '3 Hour Forecast': [250, 350, 450, 550],
    }
    df = pd.DataFrame(data)
    
    # Expected DataFrame after interpolation
    expected_data = {
        'Init Time': ['2020-01-01 00:00:00', '2020-01-01 01:00:00', '2020-01-01 02:00:00', '2020-01-01 03:00:00'],
        '0 Hour Forecast': [100, 200, 300, 400],
        '0.5 Hour Forecast': [125, 225, 325, 425],  # Interpolated values
        '1 Hour Forecast': [150, 250, 350, 450],
        '1.5 Hour Forecast': [175, 275, 375, 475],  # Interpolated values
        '2 Hour Forecast': [200, 300, 400, 500],
        '2.5 Hour Forecast': [225, 325, 425, 525],  # Interpolated values
        '3 Hour Forecast': [250, 350, 450, 550]
    }
    expected_df = pd.DataFrame(expected_data)

    # Run the function under test
    result_df = generate_half_hourly_forecasts(df)

    # Check if the result matches the expected output
    pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True), check_dtype=False)