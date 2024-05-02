import nbformat

# Path to your notebook file
notebook_path = "/Users/carlosquintero/Desktop/soft_dev_project/notebooks/EDA.ipynb"

try:
    # Read the notebook
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    # Validate the notebook
    nbformat.validate(nb)

    print("Notebook validation successful.")
except Exception as e:
    print("Notebook validation failed with the following error:")
    print(e)
