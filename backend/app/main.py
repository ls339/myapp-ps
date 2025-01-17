from typing import Annotated
from fastapi import FastAPI, Query, Depends
from sqlmodel import select, Session, create_engine
from .db import get_db_connection_string, MyTable

app = FastAPI()
connection = get_db_connection_string()
engine = create_engine(connection, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@app.get("/strings/")
def read_strings(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[MyTable]:
    string_values = session.exec(select(MyTable).offset(offset).limit(limit)).all()
    return string_values
