import chardet
import requests
from io import StringIO
import pandas as pd

def load_data(csv_url):
    """
    Loads the dataset from a given CSV URL with auto-detected encoding.

    Parameters:
    - csv_url: str, URL of the CSV file

    Returns:
    - DataFrame containing the loaded data
    """
    response = requests.get(csv_url)
    response.raise_for_status()

    encoding = chardet.detect(response.content)['encoding']
    print(f"Detected encoding: {encoding}")

    decoded_csv = StringIO(response.content.decode(encoding))
    df = pd.read_csv(decoded_csv)

    return df