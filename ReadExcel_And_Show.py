# 必要インストールライブラリ
# pip install openpyxl

import pandas as pd
import plotly.express as px

df = pd.read_excel("input/ReadExcel_And_Show.xlsx")

fig = px.line(df, x="x", y="y")
fig.show()