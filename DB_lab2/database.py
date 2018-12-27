# db commands from lab 1 using ORM

from db_schemes import Base
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from db_schemes import DeveloperScheme
from db_schemes import ProjectScheme
from db_schemes import TeamLeadScheme
from db_schemes import TeamScheme
from db_schemes import TeamProjectScheme

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
        # self._session_.autocommit = True

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
        # self.create_developer(developer_scheme)
        dev = self._session_.query(DeveloperScheme).filter_by(id=developer_scheme.id).one()
        dev.fullname = developer_scheme.fullname
        dev.married = developer_scheme.married
        dev.birth = developer_scheme.birth
        if developer_scheme.team_id is not None:
            dev.team_id = developer_scheme.team_id
        self._session_.commit()

    def delete_developer(self, developer_id):
        self._session_.query(DeveloperScheme).filter_by(id=developer_id).delete()
        self._session_.commit()

    # def get_teamlead(self, teamlead_id):
    #     return self._session_.query(DeveloperScheme).filter(id=teamlead_id).first()

    def create_teamlead(self, teamlead_scheme: TeamLeadScheme):
        self._session_.add(teamlead_scheme)
        self._session_.commit()

    def delete_teamlead(self, teamlead_id):
        self._session_.query(TeamLeadScheme).filter_by(id=teamlead_id).delete()
        self._session_.commit()

    def update_teamlead(self, teamlead_scheme: TeamLeadScheme):
        tl = self._session_.query(TeamLeadScheme).filter_by(id=teamlead_scheme.id).one()
        tl.fullname = teamlead_scheme.fullname
        self._session_.commit()
        # self.create_teamlead(teamlead_scheme)

    def create_team(self, team_scheme: TeamScheme):
        self._session_.add(team_scheme)
        self._session_.commit()

    def delete_team(self, team_id):
        self._session_.query(TeamScheme).filter_by(id=team_id).delete()
        self._session_.commit()

    def update_team(self, team_scheme: TeamScheme):
        t = self._session_.query(TeamScheme).filter_by(id=team_scheme.id).one()
        t.team_name = team_scheme.team_name
        self._session_.commit()

    def create_project(self, project_scheme: ProjectScheme):
        self._session_.add(project_scheme)
        self._session_.commit()

    def delete_project(self, project_id):
        self._session_.query(ProjectScheme).filter_by(id=project_id).delete()
        self._session_.commit()

    def update_project(self, project_scheme: ProjectScheme):
        p = self._session_.query(ProjectScheme).filter_by(id=project_scheme.id).one()
        p.title = project_scheme.title
        p.type = project_scheme.type
        self._session_.commit()
        # self.create_project(project_scheme)

    def add_project_for_team(self, team_project_scheme: TeamProjectScheme):
        self._session_.add(team_project_scheme)

    def delete_project_for_team(self, t_id, p_id):
        self._session_.query(ProjectScheme).\
        filter_by(team_id=t_id).\
        filter_by(project_id=p_id).\
        delete()
        self._session_.commit()

    def change_team_for_dev(self, dev_id, new_team_id):
        pass

    def get_table_toString(self, table_name):
        # if table_name == "Developers_teams_teamleads" or table_name == "teams_projects":
        return self._session_.query(Base.metadata.tables[table_name]).all()

    def search_by_date(self, left_bound, right_bound):
        res = self._session_.query(DeveloperScheme)\
            .filter(DeveloperScheme.birth >= left_bound.date(),\
                    DeveloperScheme.birth < right_bound.date())\
            .all()
        strings = ""
        for row in res:
            strings += str(row.__dict__) + "\n"
        return strings

    def search_by_bool(self, bool_value):
        res = self._session_.query(DeveloperScheme)\
            .filter(DeveloperScheme.married == bool_value)\
        .all()
        strings = ""
        for row in res:
            strings += str(row.__dict__) + "\n"
        return strings

    def fulltext_search(self, tablename, fields, query):
        #Todo fields now is not a list
        # if isinstance(fields, list): fields = str(fields).split()
        #todo
        sql = f"""SELECT * FROM {tablename} 
                      WHERE to_tsvector({fields}) @@ phraseto_tsquery('english', '{query}');"""
        res = self._engine_.execute(sql).fetchall()

        strings = ""
        for row in res:
            strings += str(dict(row.items())) + "\n"
        return strings

    def clear_all(self):
        pass

db = Database()
