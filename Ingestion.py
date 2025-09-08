import pandas as pd
import numpy as np
import os
import logging
import time
from sqlalchemy import create_engine

# Ensure log folder exists
os.makedirs("logs", exist_ok=True)

# Logging configuration
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Connect to SQLite DB
engine = create_engine("sqlite:///inventory.db")

# Save DataFrame to database
def ingest_db(df, table_name, engine):
    try:
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        logging.info(f"Successfully ingested data into table: {table_name}")
    except Exception as e:
        logging.error(f"Failed to ingest {table_name}: {e}")

# Load CSV files from 'data' directory
def load_raw_data():
    start = time.time()
    logging.info("Starting data ingestion...")

    for file in os.listdir("data"):
        if file.endswith(".csv"):
            try:
                df = pd.read_csv(os.path.join("data", file))
                logging.info(f'Ingesting file: {file}')
                ingest_db(df, file[:-4], engine)
            except Exception as e:
                logging.error(f"Error processing file {file}: {e}")

    end = time.time()
    total_time = (end - start) /60
    logging.info("-------- Ingestion Complete --------")
    logging.info(f"Total Time Taken: {total_time:.2f} minutes")

# Main entry point
if __name__ == "__main__":
    load_raw_data()