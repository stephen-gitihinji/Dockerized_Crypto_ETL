from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

def load_coins(cleaned_coins):
	conn_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

	engine = create_engine(conn_string)

	#adding the coins data to the db
	cleaned_coins.to_sql("crypto_coins", con=engine, if_exists="replace", index=False)