# Standard Library
from os import getenv


MEMBER_PROCESS = 1
CONJUGAL_PROCESS = 2
CHILDREN_PROCESS = 3

FAMILY_PROCESSES = {
    MEMBER_PROCESS: "MEMBER_PROCESS",
    CONJUGAL_PROCESS: "CONJUGAL_PROCESS",
    CHILDREN_PROCESS: "CHILDREN_PROCESS",
}

POSTGRESQL_USER = getenv("POSTGRESQL_USER")
POSTGRESQL_PASSWORD = getenv("POSTGRESQL_PASSWORD", "")
POSTGRESQL_SERVER = getenv("POSTGRESQL_SERVER")
POSTGRESQL_DATABASE = getenv("POSTGRESQL_DATABASE", "")
POSTGRESQL_PORT = getenv("POSTGRESQL_PORT", 5432)

DB_CONFIG = {
    "host": POSTGRESQL_SERVER,
    "database": POSTGRESQL_DATABASE,
    "user": POSTGRESQL_USER,
    "password": POSTGRESQL_PASSWORD,
    "port": POSTGRESQL_PORT,
}

MEMBER_CSV = "clan_data.csv"
CONJUGAL_CSV = "clan_data_conjugal.csv"
CHILDREN_CSV = "clan_data_conjugal_children.csv"
CSV_PATH = r"C:\Users\matia\DesktopLocal\yggdrasil_solglez\cronjob_snapshot\src\app\files\clan_data_conjugal_children.csv"

MEMBERS_TABLE = "family_members"
CONJUGAL_TABLE = "conjugals"
CHILDREN_TABLE = "conjugals_children"
