import json
import pandas as pd
import matplotlib.pyplot as plt

with open("results/good_results.json") as f:
    df = pd.DataFrame(json.load(f)).set_index('model')

# Save the full table
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

# Save a table for each algorithm (column)
for alg in df.columns:
    plt.clf()
    fig, ax = plt.subplots()
    ax.axis('off')
    # Single column DataFrame for this algorithm
    single_col_df = df[[alg]]
    table = ax.table(
        cellText=single_col_df.values,
        colLabels=[alg],
        rowLabels=single_col_df.index,
        loc='center',
        cellLoc='center'
    )
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.auto_set_column_width(col=[0])
    plt.tight_layout(pad=0.5)
    plt.savefig(f"results/good_results_table_{alg}.png", bbox_inches='tight', dpi=200)
    plt.close()