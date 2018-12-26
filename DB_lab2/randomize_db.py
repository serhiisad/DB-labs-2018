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
    return bool(random.getrandbits(1))

def get_rand_date(min_year=1970, max_year=datetime.now().year):
    year = random.randint(1950, 2018)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    # hour = random.randint(0, 23)
    # minute = random.randint(00, 59)
    # second = random.randint(00, 59)
    return datetime.datetime(year, month, day)

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
        new_proj = random.choice(projects)
        db.create_project(new_proj)
    for k in range(teamleads_cnt-1):
        new_tl = Teamlead(names.get_full_name())
        db.create_teamlead(new_tl)
