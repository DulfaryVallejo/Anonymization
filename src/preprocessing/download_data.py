import requests
import os

base_url = 'https://api.github.com/repos/PlanTL-GOB-ES/SPACCC_MEDDOCAN/contents/corpus'

folders = ['dev', 'test', 'train']

# Local to save the files
local_folder = r'.\data\raw' 

# Create folder if doesn't exist
if not os.path.exists(local_folder):
    os.makedirs(local_folder)

def download_files(carpeta):
    url = f'{base_url}/{carpeta}/xml'
    response = requests.get(url)
    data = response.json()

    for files in data:
        file_name = files['name']
        url_file = files['download_url']
        r = requests.get(url_file).content

        with open(os.path.join(local_folder, file_name), 'wb') as f:
          f.write(r)

# Download files from each folder
for folder in folders:
    download_files(folder)