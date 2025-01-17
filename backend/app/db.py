from typing import Union
from sqlmodel import Field, SQLModel
import os


class MyTable(SQLModel, table=True):
    id: Union[int, None] = Field(default=None, primary_key=True)
    string_value: str = Field(index=True)


def get_db_connection_string():
    config_path = os.getenv("DATABASE_URL_FILE")
    with open(config_path, "r") as file:
        connection_string = file.read().strip()
    return connection_string
