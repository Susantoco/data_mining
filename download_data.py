import gdown
import os

OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

url = "https://drive.google.com/drive/u/0/folders/1-8VtHC916P6kavmyP72kjjJlF_cSepsj"
gdown.download_folder(url, output=OUTPUT_DIR, quiet=False)

