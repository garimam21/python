print("Running check.py script...")
import nbformat

with open('modeltraining2.ipynb', 'r', encoding='utf-8') as f:
    try:
        nb = nbformat.read(f, as_version=4)
        print("Notebook is valid JSON.")
    except nbformat.reader.NotJSONError:
        print("Notebook is not valid JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")
