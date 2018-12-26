# db commands from lab 1 using ORM

from db_schemes import Base
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date

from db_schemes import DeveloperScheme
from db_schemes import ProjectScheme
from db_schemes import TeamLeadScheme
from db_schemes import TeamScheme

from texttable import Texttable

#TODO
class Database:

    _engine_ = create_engine('postgresql://postgres:122531@localhost:5433/test_db')
    _session_ = sessionmaker(bind=_engine_)

    def __init__(self):
        _engine_ = create_engine('postgresql://postgres:122531@localhost:5433/test_db')
        _Session_ = sessionmaker(bind=_engine_)
        Base.metadata.create_all(_engine_)
        self._session_ = _Session_()

    def close(self):
        self._session_.close()

    # def get_developer(self, developer_id):
    #     return self._session_.query(DeveloperScheme).get(developer_id)

    def create_developer(self, developer_scheme: DeveloperScheme):
        self._session_.add(developer_scheme)
        self._session_.commit()
    # def insert_developers_list(self, developer_scheme_list):
    #     for dev in developer_scheme_list:
    #         self.insert_developer(dev)
    def update_developer(self, developer_scheme: DeveloperScheme):
        self.create_developer(developer_scheme)

    def delete_developer(self, developer_id):
        self._session_.query(DeveloperScheme).filter_by(id=developer_id).delete()
        self._session_.commit()

    # def get_teamlead(self, teamlead_id):
    #     return self._session_.query(DeveloperScheme).get(teamlead_id)

    def create_teamlead(self, teamlead_scheme: TeamLeadScheme):
        self._session_.add(teamlead_scheme)
        self._session_.commit()

    def delete_teamlead(self, teamlead_id):
        self._session_.query(TeamLeadScheme).filter_by(id=teamlead_id).delete()
        self._session_.commit()

    def update_teamlead(self, teamlead_scheme: TeamLeadScheme):
        self.create_teamlead(teamlead_scheme)



    # def get_team(self, team_id):
    #     return self._session_.query(DeveloperScheme).get(team_id)

    def сreate_team(self, team_scheme: TeamScheme):
        self._session_.add(team_scheme)
        self._session_.commit()

    def delete_team(self, team_id):
        self._session_.query(TeamScheme).filter_by(id=team_id).delete()
        self._session_.commit()

    def update_team(self, team_scheme: TeamScheme):
        self.create_team(team_scheme)


    # def get_project(self, project_id):
    #     return self._session_.query(DeveloperScheme).get(project_id)

    def create_project(self, project_scheme: ProjectScheme):
        self._session_.add(project_scheme)
        self._session_.commit()

    def delete_project(self, project_id):
        self._session_.query(ProjectScheme).filter_by(id=project_id).delete()
        self._session_.commit()

    def update_project(self, project_scheme: ProjectScheme):
        self.create_project(project_scheme)

    #TODO
    def add_project_for_team(self, team_id, project_id):
        pass

    def delete_project_for_team(self, team_id, project_id):
        pass

    def change_team_for_dev(self, dev_id, new_team_id):
        pass

    def get_table_toString(self, table_name):
        return self._session_.query(Base.metadata.tables[table_name]).all()

    def search_by_date(self, field_name, left_boundary, right_boundary):
        pass

    def search_by_bool(self, bool_value):
        pass

    def fulltext_search(self, tablename, fields, query):
        pass

    def clear_all(self):
        pass

db = Database()
