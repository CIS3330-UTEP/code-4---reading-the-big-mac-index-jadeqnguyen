import pandas as pd


# list_teams = ["49ers", "KC", "Cowboys", "Steelers"]

# print(type(list_teams))

# print(list_teams)

# series_teams = pd.Series(list_teams)

# print(series_teams)
# print(type(series_teams))

# students = {"Hawaii":"Isabella", "Ohio":"David","Iowa":"Justin","Colorado": "Robert"}
# print(type(students))
# print(students)
# # print(students.index)

# student_series = pd.Series(index=students.keys(),data=students.values())

# print(type(student_series))
# print(student_series)
# print(student_series.index)

df = pd.read_csv("big-mac-full-index.csv")

# print(type(df))
# print(df.columns)
# print(type(df.columns))

# print(df["name"])

# print(type(df["name"]))

# print((df["iso_a3"]))

# print(type(df["iso_a3"]))

country_code = ["USA"]
query_text = f"iso_a3 == @country_code"

df_usa = df.query(query_text)

# print(round(df_usa["local_price"]))
# print(df.median())

print(df_usa)

idx_dollar_price = df_usa["dollar_price"].idxmax()

print(idx_dollar_price)

usa_series = df_usa.loc[idx_dollar_price]

