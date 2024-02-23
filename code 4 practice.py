import pandas as pd

df = pd.read_csv("big-mac-full-index.csv")
year = 2020 
query_text = f"date > '{year}-01-01' and date < '{year}-12-31' "
df_year = df.query(query_text)