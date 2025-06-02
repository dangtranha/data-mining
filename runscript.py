import papermill as pm

notebooks = [
    "1_data_preprocessing.ipynb",
    "2_eda_visualization.ipynb",
    "3_customer_features.ipynb"
]

for nb in notebooks:
    print(f"Running {nb}...")
    pm.execute_notebook(
        nb,
        nb  # ghi đè lên chính nó
    )