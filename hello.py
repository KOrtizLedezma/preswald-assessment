import pandas as pd
import plotly.express as px
from preswald import text, table, slider, plotly

# Load dataset
df = pd.read_csv("data/vgsales.csv")

# Page title
text("# Video Game Sales Dashboard")

# Section: Global Sales by Platform
text("## Global Sales by Platform")

platform_sales = (
    df.groupby("Platform", as_index=False)["Global_Sales"]
    .sum()
    .sort_values("Global_Sales", ascending=False)
)

fig = px.bar(
    platform_sales,
    x="Platform",
    y="Global_Sales",
    color="Platform",
    title="",
    labels={"Global_Sales": "Sales (millions)"}
)
plotly(fig)

# Section: Filter by NA Sales
text("## Filter by NA Sales")

threshold = slider("Minimum NA Sales (millions)", min_val=0, max_val=50, default=10)
filtered = df[df["NA_Sales"] > threshold]

display_columns = ["Name", "Platform", "Year", "Genre", "NA_Sales"]
filtered_display = filtered[display_columns]

table(filtered_display, title=f"Games with NA Sales > {threshold}M")

