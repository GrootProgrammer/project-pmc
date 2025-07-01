import json
import pandas as pd
import matplotlib.pyplot as plt

with open("results/good_results.json") as f:
    df = pd.DataFrame(json.load(f)).set_index('model')

fig, ax = plt.subplots()
ax.axis('off')
table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    rowLabels=df.index,
    loc='center',
    cellLoc='center'
)
table.auto_set_font_size(False)
table.set_fontsize(12)
table.auto_set_column_width(col=list(range(len(df.columns))))
plt.tight_layout(pad=0.5)
plt.savefig("results/good_results_table.png", bbox_inches='tight', dpi=200)
plt.close()