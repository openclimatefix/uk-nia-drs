import subprocess

def download_from_gs(gs_path, local_path):
    """
    Download a file from Google Cloud Storage (gs) to a local path.
    
    Args:
    gs_path (str): The gs path to the file to download.
    local_path (str): The local path where to save the downloaded file.
    """
    try:
        subprocess.check_call(['gsutil', 'cp', gs_path, local_path])
        print(f"Successfully downloaded {gs_path} to {local_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download {gs_path}. Error: {e}")

if __name__ == "__main__":
    # Define the Google Storage path and the local path
    gs_path = "gs://solar-pv-nowcasting-data/backtest/drs_backtest/model_ensemble.nc"
    # gs_path = "gs://solar-pv-nowcasting-data/backtest/national_xg_2018_2022/full_predictions_cross_validation_v2.csv"
    local_path = "./model_ensemble.nc"

    # Download the data
    download_from_gs(gs_path, local_path)
