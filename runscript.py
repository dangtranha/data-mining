import importlib
import subprocess
import sys

def import_or_install(package, import_name=None):
    try:
        importlib.import_module(import_name or package)
    except ImportError:
        print(f"Chưa có {package}, đang cài đặt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Đã cài xong {package}")

import_or_install("papermill")

import papermill as pm

notebooks = [
    "1_data_preprocessing.ipynb",
    "2_eda_visualization.ipynb",
    "3_customer_features.ipynb"
]

for nb in notebooks:
    print(f"Đang chạy {nb}...")
    pm.execute_notebook(
        nb,
        nb  
    )
    print(f"Đã chạy xong {nb}.\n")
print("Tất cả các notebook đã được chạy xong.")