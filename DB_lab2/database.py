
#orm db queries from lab 1

from db_schemes import Base
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date

from db_schemes import DeveloperScheme
from db_schemes import ProjectScheme
from db_schemes import TeamLeadScheme
from db_schemes import TeamScheme


class Database:

    _engine_ = create_engine('postgresql://postgres:122531@localhost:5433/test_db')
    _session_ = sessionmaker(bind=_engine_)

    def __init__(self):
        _engine_ = create_engine('postgresql://postgres:122531@localhost:5433/test_db')
        _Session_ = sessionmaker(bind=_engine_)
        Base.metadata.create_all()
        self._session_ = _Session_()

    def close(self):
        self._session_.close()


    def get_developer(self, developer_id):
        return self._session_.query(DeveloperScheme).get(developer_id)

    def insert_developer(self, developer_scheme: DeveloperScheme):
        pass

    def insert_developers_list(self, developer_scheme_list):
        for dev in developer_scheme_list:
            self.insert_developer(dev)

    def update_developer(self, developer_scheme: DeveloperScheme):
        pass

    def delete_developer(self, developer_id):
        pass

    def


d = Database()
print(d.)
