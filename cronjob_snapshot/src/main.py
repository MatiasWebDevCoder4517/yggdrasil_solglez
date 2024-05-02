# External
import pandas as pd
import psycopg2
from psycopg2 import extras

# Project
from app.config import CHILDREN_TABLE, CSV_PATH, DB_CONFIG, LOGGER


##Todo: reorder, clean code structure and modularization
def load_csv_to_df(filepath):
    """Load CSV data into a DataFrame, attempting different encodings if necessary"""
    try:
        return pd.read_csv(filepath, encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return pd.read_csv(filepath, encoding="latin1")
        except UnicodeDecodeError:
            return pd.read_csv(filepath, encoding="cp1252")


def insert_data(df, table):
    """Insert DataFrame data into PostgreSQL table"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            tuples = [tuple(x) for x in df.to_numpy()]
            cols = ",".join(list(df.columns))

            ##Todo: Implement lightweight ORM for dealing with raw SQL queries in the code
            query = f"INSERT INTO {table}({cols}) VALUES %s"
            try:
                extras.execute_values(cursor, query, tuples)
                conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(f"Error: {error}")
                conn.rollback()
            cursor.close()


def cronjob():
    ##Todo: Make code logic for before paste data into db, build dump and save it
    ## Dump data from database (backup folder)
    ##{timestamp}_clan_data_base.csv
    ##{timestamp}_clan_data_conjugal.csv
    ##{timestamp}_clan_data_conjugal.csv

    df = load_csv_to_df(CSV_PATH)
    insert_data(df, CHILDREN_TABLE)
    LOGGER.info("Data inserted successfully.")


if __name__ == "__main__":
    cronjob()
