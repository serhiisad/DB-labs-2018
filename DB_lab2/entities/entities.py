class Developer:
    def __init__(self, fullname, birth, married):
        self.fullname = fullname
        self.birth = birth
        self.married = married

class Project:

    def __init__(self, title, type):
        self.title = title
        self.type = type

class Team:

    def __init__(self, _team_name):
        self.team_name = _team_name

class Teamlead:

    def __init__(self, _fullname):
        self.fullname = _fullname
