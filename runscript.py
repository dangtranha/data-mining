import subprocess
import sys
import os
import papermill as pm

def install_requirements():
    req_file = "requirements.txt"
    if os.path.exists(req_file):
        print("Đang cài đặt các thư viện từ requirements.txt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
        print("Cài đặt xong tất cả thư viện.\n")
    else:
        print("Không tìm thấy requirements.txt, bỏ qua bước cài đặt.")

def run_notebooks():
    notebooks = [
        "1_data_preprocessing.ipynb",
        "2_eda_visualization.ipynb",
        "3_customer_features.ipynb",
        "4_clustering.ipynb",
        "5_Customer_Segmentation.ipynb",
    ]

    for nb in notebooks:
        if not os.path.exists(nb):
            print(f" Notebook {nb} không tồn tại, bỏ qua.")
            continue
        print(f"▶ Đang chạy {nb}...")
        pm.execute_notebook(nb, nb)
        print(f" Đã chạy xong {nb}.\n")

if __name__ == "__main__":
    install_requirements()
    run_notebooks()
