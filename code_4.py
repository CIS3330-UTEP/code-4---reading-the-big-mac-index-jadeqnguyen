import pandas as pd
filename = "big-mac-full-index.csv"
df = pd.read_csv(filename)

def get_big_mac_price_by_year(year,country_code):
    #filter data first
    year = 2000
    query_text = f"date > '{year}-01-01' and date < '{year}-12-31'"
    df_year = df.query(query_text)
    return round(df_year["dollar_price"].mean(),2)
    
def get_big_mac_price_by_country(country_code):
    country_code = "iso_a3"
    query_text = f"iso_a3 == {country_code}"
    return round(df["dollar_price"].mean(),2)
    

# def get_the_cheapest_big_mac_price_by_year(year):
#     filt_df = df.loc[df["year"] == year]
#     min_price_country = filt_df.loc[filt_df["dollar_price"].idxmin()]
    
#     country_name = min_price_country["name"]
#     country_code = min_price_country["iso_a3"]
#     minimum_price = min_price_country["dollar_price"]
    
#     return f"{country_name}({country_code}): ${round(minimum_price, 2)}"

# def get_the_most_expensive_big_mac_price_by_year(year):
#     filt_df = df.loc[df["year"] == year]
#     max_price_country = df.loc[filt_df["dollar_price"].idxmax()]

#     country_name = max_price_country["name"]
#     country_code = max_price_country["iso_a3"]


# if __name__ == "__main__":
#     result_a = get_big_mac_price_by_year(2010,"arg")
#     print(result_a)
    # result_b = get_big_mac_price_by_country("mex")
    # print(result_b)
    # result_c = get_the_cheapest_big_mac_price_by_year(2008)
    # print()
    # result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    # print(result_d)