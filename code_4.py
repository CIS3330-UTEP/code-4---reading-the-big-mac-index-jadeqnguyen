import pandas as pd

filename = "big-mac-full-index.csv"
df = pd.read_csv(filename)

def get_big_mac_price_by_year(year,country_code):
    #filter data first 
    query_text = f"(date >= '{year}-01-01' and (date <= '{year}-12-31') and (iso_a3 == '{country_code})'"
    df_year = df.query(query_text)
    
    return round(df_year["dollar_price"].mean(),2)
    
def get_big_mac_price_by_country(country_code):
    query_text = f"iso_a3 == '{country_code}'"
    df_country_code = df.query(query_text)
    
    return round(df_country_code["dollar_price"].mean(),2)
    
def get_the_cheapest_big_mac_price_by_year(year):
    query_text = f"date == '{year}'"
    df_cheapest_year = df.query(query_text)
    
    return df_cheapest_year.loc[df_cheapest_year['dollar_price'].idxmax()]
    
def get_the_most_expensive_big_mac_price_by_year(year):
    query_text = f"date == '{year}'"
    df_expensive_year = df.query(query_text)
    
    return df_expensive_year.loc[df_expensive_year['dollar_price'].idxmin()]


    if __name__ == "__main__":