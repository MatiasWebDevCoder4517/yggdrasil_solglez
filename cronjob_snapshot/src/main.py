# Standard Library
import os

# External
import pandas as pd
import psycopg2
from psycopg2 import extras

# Project
from app.config import FAMILY_PROCESSES_CSV, FAMILY_PROCESSES_TABLES, LOGGER
from app.db.postgresql import get_db


def load_csv_to_df(process: int):
    """Load CSV data into a DataFrame, attempting different encodings if necessary"""
    filename = FAMILY_PROCESSES_CSV.get(process)
    search_path = "."
    try:
        filepath = next(
            os.path.join(root, filename)
            for root, _, files in os.walk(search_path)
            if filename in files
        )
        return pd.read_csv(filepath, encoding="utf-8")
    except StopIteration:
        LOGGER.error(f"No CSV file found for process {process}")
        return None
    except UnicodeDecodeError:
        try:
            LOGGER.info("Retrying read CSV with latin1...")
            return pd.read_csv(filepath, encoding="latin1")
        except UnicodeDecodeError:
            LOGGER.info("Retrying read CSV with cp1252...")
            return pd.read_csv(filepath, encoding="cp1252")


## Todo: refactor this function with dynamic identification of the process and obtaining the correct database table
def update_data_db(db_session, df, table: str):
    """Insert DataFrame data into PostgreSQL table"""
    with psycopg2.connect(db_session) as conn:
        with conn.cursor() as cursor:
            tuples = [tuple(x) for x in df.to_numpy()]
            cols = ",".join(list(df.columns))
            query = f"INSERT INTO {table}({cols}) VALUES %s"
            try:
                extras.execute_values(cursor, query, tuples)
                conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                LOGGER.error(f"Error: {error}")
                conn.rollback()
            cursor.close()


def cronjob(process: int):
    db_session = next(get_db())
    if not process:
        LOGGER.critical(
            f"Process does not exists or wrong type! -> process: {process} | type: {type(process)}"
        )
        return "Invalid Process!"

    if process in FAMILY_PROCESSES_TABLES.keys():
        data_table = FAMILY_PROCESSES_TABLES.get(process, "")
        df = load_csv_to_df(process)
        insert_data = update_data_db(db_session, df, data_table)

        if not insert_data:
            LOGGER.error(
                f"Error trying to update data in the database!: data_table: {data_table} | type_table: {type(data_table)}"
            )
            return

        LOGGER.info(f"Data inserted successfully! -> data_table modified: {data_table}")
        db_session.close()


if __name__ == "__main__":
    process_input = int(input("Choose process to insert into the clan database [1,2,3]: "))
    cronjob(process_input)
