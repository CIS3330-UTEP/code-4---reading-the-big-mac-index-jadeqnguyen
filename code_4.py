import pandas as pd
df = pd.read_csv("big-mac-full-index.csv")
# print(df.head())

def get_big_mac_price_by_year(year,country_code):
    #filter data first
    year = "date"
    country_code = "iso_a3"
    query_text = f"iso_a3 == @county_code"
    print(round(df["dollar_price"].mean(),2))

def get_big_mac_price_by_country(country_code):
    print(round(df["dollar.price"].mean(),2))

def get_the_cheapest_big_mac_price_by_year(year):
    print(df["dollar_price"].min())

def get_the_most_expensive_big_mac_price_by_year(year):
    print(df["dollar.price"].max())

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010,"arg")
    print(result_a)
    result_b = get_big_mac_price_by_country("mex")
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print()
    result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    print(result_d)