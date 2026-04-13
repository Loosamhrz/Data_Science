import json

path = 'polyregression.ipynb'

with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for c in nb.get('cells', []):
    if c.get('cell_type') == 'code':
        source = "".join(c.get('source', []))
        if "from sklearn.metrics import r2_score" in source:
            c['source'] = [
                "from sklearn.metrics import r2_score\n",
                "energy_consumption_predicted_all = model.predict(x_poly)\n",
                "r2 = r2_score(df['Energy_Consumption'], energy_consumption_predicted_all)\n",
                "print(f\"{r2}\")"
            ]
            c['outputs'] = []
            if 'execution_count' in c:
                c['execution_count'] = None

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook modified successfully!")
