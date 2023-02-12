import json
import os.path
from peewee import *
from errors import DatabaseConfigNotFound, UndefinedDatabaseConnectionType

DB_CONFIG_FILE = "db.json"


def connect_db():
    if os.path.isfile(DB_CONFIG_FILE):
        db_config_file = open(DB_CONFIG_FILE)
        db_config = json.load(db_config_file)
        db_config_file.close()
        connection_type = db_config['connection']
        database_name = db_config['database']
        if connection_type == "sqlite":
            return SqliteDatabase(database_name)
        if connection_type == "mysql":
            return MySQLDatabase(database_name,
                                 user=db_config['username'],
                                 password=db_config['password'],
                                 host=db_config['host'],
                                 port=db_config['port']
                                 )
        if connection_type == "postgres":
            return PostgresqlDatabase(database_name,
                                      user=db_config['username'],
                                      password=db_config['password'],
                                      host=db_config['host'],
                                      port=db_config['port']
                                      )
        raise UndefinedDatabaseConnectionType
    else:
        raise DatabaseConfigNotFound


db = connect_db()
