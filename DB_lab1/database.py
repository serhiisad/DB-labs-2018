import psycopg2
from pprint import pprint
import datetime
from entities.entities import *
import pandas
from texttable import Texttable

class Database:

    def __init__(self):
        try:
            self.connection = psycopg2.connect("dbname='test_db' user='postgres' host='localhost' "
                                         "password='122531' port='5433'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            pprint("Connected")
        except:
            pprint("cannot connect to db_lab1")

    # def query(self, query, params):
    #     return self.cursor.execute(query, params)
    #
    #
    # def __exit__(self):
    #     self.connection.close()

#INSERT


#Create

    def create_team(self, new_team):
        self.cursor.execute("INSERT into teams (team_name) values('" + new_team.team_name + "')")

    def create_project(self, new_project):
        self.cursor.execute("insert into projects(title, type) values('" + new_project.title + "','"
                            + new_project.type + "')")

    def create_developer(self, new_dev):
        self.cursor.execute("insert into developers(fullname, birth, married) values" \
                "('" + new_dev.fullname +"','" + new_dev.birth + "','" + new_dev.married + "')")

    def create_teamlead(self, _new_teamlead):
        self.cursor.execute("insert into teamleads(fullname) values('" + _new_teamlead.fullname + "')")

    def add_project_for_team(self, team_id, project_id):
        self.cursor.execute(f"insert into team_project(team_id, project_id) values({team_id}, {project_id})")

#DELETE

    def delete_team(self, team_id):
        self.cursor.execute(f"delete from teams where id = {team_id}")
        # self.cursor.execute(f"delete from team_project where team_id = {id};") &&

    def delete_project(self, project_id):
        self.cursor.execute(f"delete from projects where id = {project_id}")

    def delete_developer(self, dev_id):
        self.cursor.execute(f"delete from developers where id = {dev_id}")

    def delete_teamlead(self, teamlead_id):
        self.cursor.execute(f"delete from teamleads where id = {teamlead_id}")

#UPDATE

    def update_team(self, team_id, new_team):
        self.cursor.execute(f"update teams set team_name = \'{new_team.team_name}\' where id = {team_id}")

    def update_project(self, project_id, _title, _type):
        self.cursor.execute(f"update projects set title = \'{_title}\', type = \'{_type}\' where id = {project_id}")

    # def update_project_for_team(self, team_id, project_id):
    #     self.cursor.execute(f"update team_project set ")...

    def update_teamlead(self, tl_id, new_teamlead):
        self.cursor.execute(f"update teamleads set fullname = \'{new_teamlead.fullname}\' where id = {tl_id}")

    def update_developer(self, dev_id, new_dev):
        self.cursor.execute(f"update developers set fullname = \'{new_dev.fullname}\', birth = \'{new_dev.birth}\', married = {new_dev.married} where id = {dev_id}")

    def change_team_for_dev(self, dev_id, new_team_id):
        self.cursor.execute("select id from teams")
        id_rows = self.cursor.fetchall()
        if str(new_team_id) in str(id_rows):
            self.cursor.execute(f"update developers set team_id = {new_team_id} where id = {dev_id}")
        else:
            raise Exception(f"cannot change team for developer with id = {dev_id}"
                            "UNKNOWN TEAM")
            pass #?

    def change_teamlead_for_team(self, _team_id, new_teamlead_id):
        self.cursor.execute(f"select id from teamleads")
        id_rows = self.cursor.fetchall()
        if str(new_teamlead_id) in str(id_rows):
            self.cursor.execute(f"update teams set teamlead_id = {new_teamlead_id} where id = {_team_id}")
        else:
            raise Exception(f"cannot change teamlead for team with id = {_team_id}"
                            f"UNKNOWN TEAMLEAD")
            pass  #?

    # def change_project_for_team(self, team_id, project_id):
    #     self.cursor.execute(f"insert into team_project(team_id, project_id) values({team_id}, {project_id})")
#SEARCH

    def search_for_devs_birth_in_range(self, date1, date2):
        # if date1 >= date2: raise Exception("dates are incorrect !")
        return f"select id, fullname, birth from developers where birth between \'{date1}\'  and \'{date2}\'"

    def search_for_married_devs(self, _married):
        return f"select id, fullname, married from developers where married = {_married}"

#Full text search

    # def fulltextsearch_by_query(self, table_name, field_names, query):
    #     return  f'CREATE OR REPLACE FUNCTION make_tsvector({field_names} TEXT)'\
    #                f'RETURNS tsvector AS $$'\
    #                f'BEGIN '\
    #                f'Return to_tsvector({field_names}); ' \
    #                f'END '\
    #                f'$$ LANGUAGE \'plpgsql\' IMMUTABLE; ' \
    #                f'CREATE INDEX IF NOT EXISTS _idx ON {table_name} ' \
    #                f'USING gin(make_tsvector()); ' \
    #                 f'SELECT id, ts_headline(fullname, q, "StartSel=<found>, StopSel=</found>") FROM developers '\
    #                 f'to_tsquery(\'{query}\') AS q'\
    #                 f'make_tsvector({field_names}) @@ q;'

    def fulltextsearch_by_query(self, table_name, field_name, query):
        return f'CREATE OR REPLACE FUNCTION make_tsvector({field_name} TEXT)\n' \
               f'   RETURNS tsvector AS $$\n' \
               f'BEGIN\n' \
               f'  RETURN to_tsvector({field_name});\n' \
               f'END\n' \
               f'$$ LANGUAGE \'plpgsql\' IMMUTABLE;\n\n' \
               f'CREATE INDEX IF NOT EXISTS idx_dev ON {table_name}\n' \
               f'USING gin(make_tsvector({field_name}));\n\n' \
               f'SELECT id, ts_headline({field_name}, q, \'StartSel=<found>, StopSel=</found>\') ' \
               f'FROM {table_name}, to_tsquery(\'{query}\') AS q\n' \
               f'WHERE make_tsvector({field_name}) @@ q;'

#get
    def get_devs_teams_teamleads(self):
        return  'select developers.id as dev_id, developers.fullname as dev_name, '\
                'teams.id as tm_id, teams.team_name, '\
                'teamleads.id as tmld_id, teamleads.fullname as tmld_name '\
 	            'from developers '\
                'inner join teams on developers.team_id = teams.id '\
                'inner join teamleads on teams.teamlead_id = teamleads.id'

    def get_teams_projects(self):
        return "select team_project.team_id, teams.team_name, "\
               "projects.id as project_id, projects.title as project_title, projects.type "\
                "from projects inner join team_project on projects.id = team_project.project_id "\
                "inner join teams on teams.id = team_project.team_id"

    def get_teams(self):
        return 'select * from teams'

    def get_projects(self):
        return 'select * from projects order by id'

    def get_teamleads(self):
        return 'select * from teamleads order by id'

    def get_developers(self):
        return 'select * from developers order by id'

    # clear up db
    def clear_all(self):
        self.cursor.execute("Delete from teamleads where id <> 1")
        self.cursor.execute("Delete from teams where id <> 1")
        self.cursor.execute("Delete from projects")
        self.cursor.execute("Delete from developers")

    # @classmethod
    def table_toString(self, query):
        out_table = Texttable()
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        col_names = [desc[0] for desc in self.cursor.description]
        # print(rows)
        # print(col_names)

        out_table.add_row(col_names)
        for r in rows:
            out_table.add_row(list(r))

        return out_table.draw()

        #todo
    #def random_fill(self, ...):
    #

