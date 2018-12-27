import datetime
from database import Database

class CheckInput:

    def test_date(date_str):
        try:
            # datetime.datetime.strptime(time_str,  %H:%M:%S')  # '2004-10-19 10:23:54'
            datetime.datetime.strptime(date_str, '%Y-%m-%d')  # '2004-10-19'
            return True
        except ValueError:
            return False

    def check_teamlead_existence(teamlead_id):
        db = Database()
        return db.get_teamlead(teamlead_id) is not None

    def check_team_existence(team_id):
        db = Database()
        return db.get_team(team_id) is not None

    def check_project_existence(project_id):
        db = Database()
        return db.get_project(project_id) is not None

    def check_developer_existence(developer_id):
        db = Database()
        return db.get_developer(developer_id) is not None

