import json

notebook_path = 'c:/Users/Lenovo/Desktop/MultipleandPolynomialRegression/polyregression.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
        if any("r2_score(df['Temperature']" in x for x in cell.get('source', [])):
            cell['source'] = [
                "from sklearn.metrics import r2_score\n",
                "energy_consumption_predicted_all = model.predict(x_poly)\n",
                "r2 = r2_score(df['Energy_Consumption'], energy_consumption_predicted_all)\n",
                "print(f\"{r2}\")"
            ]
            # Optionally clear outputs if we changed the source so it runs clean
            cell['outputs'] = []
            cell['execution_count'] = None

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)
