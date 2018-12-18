import rand_data.parser as parser
from database import Database as db
from datetime import *
import names
import random
from entities.entities import *
from database import Database

def get_random_name():
    return names.get_full_name()

def get_rand_boolean():
    return random.choice([True, False])

def get_rand_date(min_year=1970, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    # start = datetime(min_year, 1, 1, 00, 00, 00)
    start = date(min_year, 1, 1)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

def random_fill_db(projects_cnt=4, teamleads_cnt=3, teams_cnt=3, devs_cnt=13):

    db = Database() #better to pass it to the random_fill_db
    db.clear_all()

    for k in range(devs_cnt-1):
        new_dev = Developer(get_random_name(), str(get_rand_date()), str(get_rand_boolean()))
        db.create_developer(new_dev)

    teams_list = parser.tolist_teams()
    for k in range(teams_cnt-1):
        new_team = random.choice(teams_list)
        db.create_team(new_team)

    projects = parser.tolist_projects()
    for k in range(projects_cnt-1):
        new_proj = ran
    for k in range(teamleads_cnt-1):
        new_tl = Teamlead(names.get_full_name())
        db.create_teamlead(new_tl)
