from etl.extract import extract_coins
from etl.transform import transform_coins
from etl.load import load_coins

if __name__ == "__main__":
	extracted_coins = extract_coins()
	transformed_coins = transform_coins(extracted_coins)
	load_coins(transformed_coins)