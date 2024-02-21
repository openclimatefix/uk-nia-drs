import pandas as pd
import pytest
from data.merge_scripts.merge_and_blend import blend_data

# Sample data preparation
@pytest.fixture
def sample_data_xg():
    return pd.DataFrame({
        'Init Time': ['2021-01-01 02:00:00', '2021-01-01 04:00:00', '2019-01-01 04:00:00'],  # Added new init time
        '6 Hour Forecast': [90, 180, 270],  
        '6.5 Hour Forecast': [95, 185, 275], 
        '7 Hour Forecast': [100, 200, 300],  
        '7.5 Hour Forecast': [105, 205, 305],  
        '8 Hour Forecast': [150, 250, 350],  
        '8.5 Hour Forecast': [155, 255, 355],  
        '9 Hour Forecast': [160, 260, 360], 
        '0 Hour Forecast': [50, 150, 250]  
    })

@pytest.fixture
def sample_data_pvnet():
    return pd.DataFrame({
        'Init Time': ['2021-01-01 02:00:00', '2021-01-01 04:00:00', '2019-01-01 04:00:00'],  # Added new init time
        '6 Hour Forecast': [95, 185, 275], 
        '6.5 Hour Forecast': [100, 190, 280], 
        '7 Hour Forecast': [110, 210, 320],
        '7.5 Hour Forecast': [115, 215, 325], 
        '8 Hour Forecast': [160, 260, 360], 
        '0.5 Hour Forecast': [55, 155, 255] 
    })

# Test blending functionality
def test_blend_data_with_blending(sample_data_xg, sample_data_pvnet):
    result = blend_data(sample_data_xg, sample_data_pvnet, blend=True)
    assert not result.empty
    assert '7 Hour Forecast' in result.columns
    assert '7.5 Hour Forecast' in result.columns
    assert '8 Hour Forecast' in result.columns

    # Define the date range for blending
    start_date = pd.to_datetime('2020-01-01 03:00:00+00:00', utc=True)
    end_date = pd.to_datetime('2022-08-08 08:00:00+00:00', utc=True)

    within_range = result[(result['Init Time'] >= start_date) & (result['Init Time'] <= end_date)]

    # Assuming 'Init Time' can be used as a unique key for matching
    for _, row in within_range.iterrows():
        # Extract the 'Init Time' for the current row
        current_time = row['Init Time']
        
        # Find the corresponding rows in sample_data_xg and sample_data_pvnet by 'Init Time'
        row_xg = sample_data_xg[sample_data_xg['Init Time'] == current_time].iloc[0]
        row_pvnet = sample_data_pvnet[sample_data_pvnet['Init Time'] == current_time].iloc[0]
        
        # Calculate expected values based on the matching rows and blending ratios
        expected_value_7 = (row_pvnet['7 Hour Forecast'] * 0.75) + (row_xg['7 Hour Forecast'] * 0.25)
        expected_value_7_5 = (row_pvnet['7.5 Hour Forecast'] * 0.5) + (row_xg['7.5 Hour Forecast'] * 0.5)
        expected_value_8 = (row_pvnet['8 Hour Forecast'] * 0.25) + (row_xg['8 Hour Forecast'] * 0.75)
        
        assert row['6.5 Hour Forecast'] == row_pvnet['6.5 Hour Forecast'], f"Mismatch in '6.5 Hour Forecast' for Init Time {current_time}"
        assert row['7 Hour Forecast'] == pytest.approx(expected_value_7, abs=1e-5)
        assert row['7.5 Hour Forecast'] == pytest.approx(expected_value_7_5, abs=1e-5)
        assert row['8 Hour Forecast'] == pytest.approx(expected_value_8, abs=1e-5)
        assert row['8.5 Hour Forecast'] == row_xg['8.5 Hour Forecast'], f"Mismatch in '8.5 Hour Forecast' for Init Time {current_time}"

    before_start = result[(result['Init Time'] < start_date)]

    for _, row in before_start.iterrows():

        # Extract the 'Init Time' for the current row
        current_time = row['Init Time']
        
        # Find the corresponding rows in sample_data_xg and sample_data_pvnet by 'Init Time'
        row_xg = sample_data_xg[sample_data_xg['Init Time'] == current_time].iloc[0]
        row_pvnet = sample_data_pvnet[sample_data_pvnet['Init Time'] == current_time].iloc[0]

        assert row['6.5 Hour Forecast'] == row_xg['6.5 Hour Forecast'], f"Mismatch in '6.5 Hour Forecast' for Init Time {current_time}"
        assert row['8 Hour Forecast'] == row_xg['8 Hour Forecast'], f"Mismatch in '8 Hour Forecast' for Init Time {current_time}"
        assert row['8.5 Hour Forecast'] == row_xg['8.5 Hour Forecast'], f"Mismatch in '8.5 Hour Forecast' for Init Time {current_time}"

# Test without blending
def test_blend_data_without_blending(sample_data_xg, sample_data_pvnet):
    result = blend_data(sample_data_xg, sample_data_pvnet, blend=False)
    # Example check: ensure that columns from data_pvnet overwrite those in data_xg
    assert result['7 Hour Forecast'][0] == sample_data_pvnet['7 Hour Forecast'][0]
    assert result['8 Hour Forecast'][0] == sample_data_pvnet['8 Hour Forecast'][0]
    assert result['9 Hour Forecast'][0] == sample_data_xg['9 Hour Forecast'][0]