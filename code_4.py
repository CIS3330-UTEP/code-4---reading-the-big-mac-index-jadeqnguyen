import pandas as pd

filename = "big-mac-full-index.csv"
df = pd.read_csv(filename)

def get_big_mac_price_by_year(year,country_code):
    #filter data first 
    query = f"(iso_a3 == '{country_code}' and ('{year}-01-01' < date < '{year}-12-31'))"
    price_by_year = df.query(query)
    
    return round(price_by_year["dollar_price"].mean(),2)
    
def get_big_mac_price_by_country(country_code):
    query = f"(iso_a3 == '{country_code}')"
    price_by_country = df.query(query)
    
    return round(price_by_country["dollar_price"].mean(),2)
    
def get_the_cheapest_big_mac_price_by_year(year):
    query = f"date == '{year}'"
    df_cheapest_year = df.query(query)
    min_idx = df_cheapest_year["dollar_price"].idxmin()
    
    return df_cheapest_year.loc[min_idx]["dollar_price"]
    
def get_the_most_expensive_big_mac_price_by_year(year):
    query = f"date == '{year}'"
    df_expensive_year = df.query(query)
    max_idx = df_expensive_year["dollar_price"].idxmax()
    
    return df_expensive_year.loc[max_idx]['dollar_price']

if __name__ == "__main__":

    year = 2012
    country_code = "ARG"
    