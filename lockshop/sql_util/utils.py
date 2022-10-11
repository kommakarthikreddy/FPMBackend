import logging
import json
import datetime
import uuid

from sqlalchemy.sql.sqltypes import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, attributes
from sqlalchemy.orm import Session

from lockshop.common.env import SQL_INSTANCE_URI

# Use this engine all over the project
engine = create_engine(SQL_INSTANCE_URI)

# Use this Base all over the project
Base = declarative_base()

# Use this Session to create new session objects whenever needed to interact with the DataBase
Session = sessionmaker(bind=engine)

def session_wrap():
    def wrap(functionHandler):
        def inner_function(*args, **kwargs):
            # session = Session(engine)
            session = Session()
            kwargs['session'] = session

            try:
                result = functionHandler(*args, **kwargs)
            except Exception as e:
                session.rollback()
                logging.error("SQL Commit Error: {}".format(e))
                raise e
            finally:
                session.close()
            return result

        return inner_function

    return wrap


def generate_uuid():
    return str(uuid.uuid4())
