import pandas as pd
import statsmodels.api as sm

# import the dataset
df = pd.read_csv("test_BH_correction.csv", sep=";")

# extract the p-value associated with the corresponding gene
pvalues = df["pvalue"]
gene_symbols = df["protein_id"]

# apply the FDR correction using the Benjamini-Hochberg method
reject, pvals_corrected, _, _ = sm.stats.multipletests(
    pvalues, method="fdr_bh", alpha=0.05
)

# add columns with correct p-values (q-value)
df["qvalue"] = pvals_corrected

# save dataframe as Excel file
path_file_excel = "pvalue_corrected.xlsx"
df.to_excel(path_file_excel, index=False)
