#orm db queries from lab 1

from db_schemes import Base

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class Database:

    _engine = create_engine('postgresql://postgres:122531@localhost:5432/test_db')
    _session = sessionmaker(bind = _engine_)


    def __init__(self):
        pass

    def close(self):
        pass

    def get_developer(self, dev_id):
        pass

    def insert_developer(self, developer_scheme: DeveloperScheme):
