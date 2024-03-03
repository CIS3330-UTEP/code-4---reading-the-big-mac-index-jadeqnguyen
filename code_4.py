import pandas as pd

filename = "big-mac-full-index.csv"
df = pd.read_csv(filename)

def get_big_mac_price_by_year(year,country_code):
    #filter data first 
    country_code = country_code.upper()
    query_text = f"(iso_a3 == '{country_code}' and (date > '{year}-01-01' and date < '{year}-12-31'))"
    price_by_year = df.query(query_text)
    mean_price_by_year = round(price_by_year['dollar_price'].mean(),2)
    
    return mean_price_by_year
    
def get_big_mac_price_by_country(country_code):
    country_code = country_code.upper()
    query_text = f"(iso_a3 == '{country_code}')"
    price_by_country = df.query(query_text)
    mean_price_by_country = round(price_by_country['dollar_price'].mean(),2)
    
    return mean_price_by_country
    
def get_the_cheapest_big_mac_price_by_year(year):
    query = f"(date == '{year}')"
    cheapest_year = df.query(query)
    min_idx = cheapest_year['dollar_price'].idxmin()
    # "country_name(country_code): $dollar_price"
    
    return cheapest_year.loc[min_idx]["dollar_price"]
    
def get_the_most_expensive_big_mac_price_by_year(year):
    query = f"(date == '{year}')"
    expensive_year = df.query(query)
    max_idx = expensive_year['dollar_price'].idxmax()
    
    return expensive_year.loc[max_idx]['dollar_price']

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010,"arg")
    print(result_a)
    result_b = get_big_mac_price_by_country("mex")
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    print(result_d)
