import plotly.express as px
import pandas as pd

# import the dataset
volcano_plot_dataset = "test_volcano_plot.csv"
dataframe = pd.read_csv(volcano_plot_dataset, sep=";")

# split the string in the 'protein_id' column and take only the first ID
dataframe["protein_id"] = dataframe["protein_id"].str.split(";").str[0]

# setting significance threshold for pvalue: -Log(pvalue)=1.3, equivalent to p=0.05
significance_threshold = 1.3

# add a column to indicate significance
dataframe["Significant"] = dataframe["LOG10_pvalue"] > significance_threshold

# create an interactive graph with Plotly Express
fig = px.scatter(
    dataframe,
    x="log2",
    y="LOG10_pvalue",
    color="Significant",
    color_discrete_map={True: "blue", False: "#6e7a85"},
    hover_data={
        "protein_id": True,
        "gene": True,
        "protein": True,
        "Significant": False,
    },
    labels={"gene": "gene"},
    title=volcano_plot_dataset,
)

# add dashed lines at 1 and -1 on the x-axis
fig.add_shape(
    dict(
        type="line",
        x0=1,
        x1=1,
        y0=0,
        y1=9,
        line=dict(color="black", dash="dash", width=0.5),
    )
)
fig.add_shape(
    dict(
        type="line",
        x0=-1,
        x1=-1,
        y0=0,
        y1=9,
        line=dict(color="black", dash="dash", width=0.5),
    )
)

# remove unecessary legend
fig.update_layout(showlegend=False)

# specify axis legends
fig.update_layout(
    xaxis_title="log2 Fold Change",
    yaxis_title="-Log10(pvalue)",
)

title = volcano_plot_dataset[:-4]
# show interactive graph
fig.write_html(f"{title}.html")
