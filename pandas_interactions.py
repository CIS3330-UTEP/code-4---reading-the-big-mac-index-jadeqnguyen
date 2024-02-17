import pandas as pd

df = pd.read_csv("big-mac-full-index.csv")

# print(df)
# print(df.columns)
# print(type(df.columns))
# print(len(df.columns))

# print(len(df))
#will tell us how many rows we have
# print(df.index)
# print(len(df.index))
# print(type(df.index))

# numbers = range(1631)
# print(numbers)

# for i in df.index:
    # print(i)
    # print(df["iso_a3"][i])
    # print(df["dollar_price"][i])
    # print(df.loc[i]["name"])
    # print(df.iloc[i])
    # print(type(df.loc[i]))

df_mex = df.query("iso_a3 == 'MEX'")
print(df_mex)
# for i in range(len(df_mex)):
#     print(df_mex.iloc[i])
    #you can go element by element with iloc
    # print(df_mex.loc[df_mex.index])

    # for index, row in df.iterrows():
    #     # print(row["name"])
    #     print(df["name"][index])

def get_new_name(row):
    # print(row)
    new_column_value = f"{row['name']} ({row('iso_a3')}"
    return new_column_value


df_mex.apply(get_new_name, axis=1)