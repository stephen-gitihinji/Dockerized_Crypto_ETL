import pandas as pd

def transform_coins(extracted_coins):

#picking the relevant data from the coins data extracted
    cleaned_coins = []
    for coin in extracted_coins:
        coin_data = [
        coin['id'], 
        coin['name'], 
        coin['symbol'], 
        coin['total_supply'],
        coin['max_supply'], 
        coin['last_updated'],
        coin['quotes']['USD']['volume_24h'],
        coin['quotes']['USD']['price']
        ]
        cleaned_coins.append(coin_data)

    #creating a dataframe from the cleaned coins data
    columns = ["coin_id", "name", "symbol", "total_supply", "max_supply", "last_updated", "volume_24h", "price"]
    coins_df = pd.DataFrame(cleaned_coins,columns=columns)
    return coins_df