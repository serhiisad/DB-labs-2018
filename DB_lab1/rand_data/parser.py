import xml.etree.ElementTree as xml_parser
from entities.entities import *

def tolist_projects():
  projects = xml_parser.parse('/home/serhiisad/PycharmProjects/DB_LABS/lab1/rand_data/projects.xml').getroot()
  list = []
  for proj in projects.findall('project'):
      title = proj.find('title').text
      type = proj.find('type').text
      new_p = Project(title, type)
      list.append(new_p)
  return list

def tolist_teams():
    teams = xml_parser.parse('/home/serhiisad/PycharmProjects/DB_LABS/lab1/rand_data/teams.xml').getroot()
    list = []
    # for team in teams.iter('team'):
    for team in teams.findall('team'):
        name = team.get('name')
        # name = team.find('name').text
        list.append(Team(str(name)))
    return list
