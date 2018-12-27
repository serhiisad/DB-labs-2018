from entities.entities import *
import randomize_db
from database import Database
from check_input import CheckInput
from datetime import datetime
from db_schemes import *
db = Database()

def input_developer():
   params = input("type <fullname,birth-date,married(1,0)>:").split(",")
   print(params)
   return DeveloperScheme(*params)

def input_teamlead():
   fullname = input("type <fullname>:")
   return TeamLeadScheme(fullname)

def input_team():
   name = input("type <team_name>:")
   return TeamScheme(name)

def input_project():
   params = input("type <title, type>:").split(",")
   return ProjectScheme(*params)

def input_teamid_and_projectid():
   params = input("type <team_id, project_id>:").split(",")
   print(params)
   return TeamProjectScheme(params[0], params[1])
   # return {"team_id": params[0], "project_id": params[1]}

def input_dates_range():
   date1 = input("enter date1(%Y-%m-%d): ")
   date2 = input("enter date2: ")
   return [date1, date2]


def input_dates_range():
   date1 = input("enter date 1 (format:  %H:%M:%S): ")
   while not CheckInput.test_date(date1):
      date1 = input("Wrong input!\nTry again: ")
   date2 = input("enter date 2 (format:  %H:%M:%S): ")
   while not CheckInput.test_date(date2):
      date1 = input("Wrong input!\nTry again: ")

   return [datetime.strptime(date1, '%Y-%m-%d'), datetime.strptime(date2, '%Y-%m-%d')]

#for full text search
def input_fulltextsearch_data():
   table_name = input("Enter table_name: ")
   field_names_list = input("Enter fields to search among: ").replace(" ", "").split(",")
   #myList = ','.join(map(str, myList))
   field_names_str = ",".join(field_names_list)
   query = input("Enter query:<using <->, |, &, ! etc>: ")
   return [table_name, field_names_str, query]

#for UI
entities_d = {
   1: "Developer",
   2: "Team",
   3: "Project",
   4: "Teamlead",
   5: "Team_Project"
}

tables_to_get_d = {
   1: "Developers_teams_teamleads",
   2: "teams_projects",
   3: "teams",
   4: "developers",
   5: "teamleads",
   6: "projects"
}

search_methods_d = {
   1: "search for developers by birth in range",
   2: "search for married developers"
}


def create():
   while True:
      print("-----Create-----")
      print_menu(entities_d)
      command = input("choose entity:")
      if command == 'q': break
      elif int(command) == 1:
         db.create_developer(input_developer())
         # 1
         break
      elif int(command) == 2:
         db.create_team(input_team())
         break
      elif int(command) == 3:
         db.create_project(input_project())
         break
      elif int(command) == 4:
         db.create_teamlead(input_teamlead())
         break
      elif int(command) == 5:
         db.add_project_for_team(input_teamid_and_projectid())
         break
      else: pass


def update():
   while True:
      print("-----Update-----")
      print_menu(entities_d, maxlen=4)
      command = input("choose entity:")
      _id = input("enter id: ")
      if command == 'q': break
      else:
         if int(command) == 1:
            new_dev = input_developer()
            new_dev.id = _id
            new_dev.team_id = input("input new_team_id(optional): ")
            db.update_developer(new_dev)
            break
         elif int(command) == 2:
            new_team = input_team()
            new_team.id = _id
            db.update_team(new_team)
            break
         elif int(command) == 3:
            new_proj = input_project()
            new_proj.id = _id
            db.update_project(new_proj)
            break
         elif int(command) == 4:
            new_tl = input_teamlead()
            new_tl.id = _id
            db.update_teamlead(new_tl)
            break
         else: pass

def delete():
   while True:
      print("-----Delete-----")
      print_menu(entities_d, maxlen=4)
      command = input("choose entity:")
      entity_id = int(input("enter id: "))
      if command == 'q': break
      elif int(command) == 1:
         db.delete_developer(entity_id)
         break
      elif int(command) == 2:
         db.delete_team(entity_id)
         break
      elif int(command) == 3:
         db.delete_project(entity_id)
         break
      elif int(command) == 4:
         db.delete_teamlead(entity_id)
         break
      else: pass

#fine
def get():
   while True:
      # try:
         print("-----Get------")
         print_menu(tables_to_get_d)
         command = input("Choose a table to print: ")
         if command == 'q':
            break
         elif int(command) in tables_to_get_d:
            print(db.get_table_toString(tables_to_get_d.get(int(command))))
         else: pass

def search():
   while True:
      try:
         print("-----Get------")
         print_menu(search_methods_d)
         command = int(input("Choose search method: "))
      except ValueError: pass
      if command == 1:
         dates = input_dates_range()
         print(db.search_by_date(dates[0], dates[1]))
         break
      elif command == 2:
         ismarried = input("input <True/False>: ")
         if(ismarried == "true"): ismarried = True
         else: ismarried = False
         print(db.table_toString(db.search_for_married_devs(ismarried)))
         break
      else: pass

def fulltext_search():

   print("-----full text search------")
   search_data = input_fulltextsearch_data()
   print(db.fulltext_search(*search_data))

def random_fill():
   params = input("type<how many projects, teamleads, teams, devs> in DB:").split(",")
   num_params = list(int(par) for par in params)
   randomize_db.random_fill_db(*num_params)

commands_d = {
   1: create,
   2: update,
   3: delete,
   4: get,
   5: search,
   6: fulltext_search,
   7: random_fill
}

def print_menu(menu_dict, maxlen=None):
   print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
   if maxlen is None:
      maxlen = len(menu_dict.items())
   if isinstance(list(menu_dict.values())[0], str):
      for key, value in list(menu_dict.items())[0:maxlen]:
         print(key, value)
   else:
      for key, value in list(menu_dict.items())[0:maxlen]:
         print(key, value.__name__)
   print("<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

def listen():
   while True:
      print_menu(commands_d)
      command = input("Enter command: ")
      if not command.isdigit():
         if command == 'q':
            print("END")
            break
         elif command == 'h':
            print_menu(commands_d)
         else: pass
      elif int(command) in commands_d:
         # try:
            commands_d[int(command)]()
         # except: print("incorrect input")
      else: pass










