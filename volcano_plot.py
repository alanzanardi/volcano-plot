import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# import the dataset
volcano_plot_dataset = "test_volcano_plot.csv"
dataframe = pd.read_csv(volcano_plot_dataset, sep=";")

Gene = dataframe["gene"].tolist()
Log2FoldChange = dataframe["log2"].tolist()
PValue = dataframe["LOG10_pvalue"].tolist()

# create the dataframe
data = {
    "Gene": Gene,
    "Log2FoldChange": Log2FoldChange,
    "PValue": PValue,
}

df = pd.DataFrame(data)

# setting significance threshold for pvalue: -Log(pvalue)=1.3, equivalent to p=0.05
significance_threshold = 1.3

# add a column to indicate significance
df["Significant"] = df["PValue"] < significance_threshold

# set all points inside the vertical lines and below the significance threshold as gray
df.loc[(df["Log2FoldChange"] > -1) & (df["Log2FoldChange"] < 1), "Significant"] = True

sns.scatterplot(
    x="Log2FoldChange",
    y=-1 * df["PValue"].apply(lambda x: -1 * (x + 1e-100)),
    hue="Significant",
    data=df,
    palette={True: "gray", False: "blue"},
    alpha=0.7,
    legend=False,  # remove unecessary legend
)
# add dashed lines at 1 and -1 on the x-axis
plt.axvline(x=1, color="black", linestyle="--", linewidth=1)
plt.axvline(x=-1, color="black", linestyle="--", linewidth=1)

plt.axhline(y=-1e-100, color="black", linestyle="--", linewidth=1)

plt.title(volcano_plot_dataset)
plt.xlabel("log2(Fold-Change)")
plt.ylabel("-log10(PValue)")
plt.show()
