from sqlalchemy import Column, String, Integer, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DeveloperScheme(Base):
    __tablename__ = "developers"

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    birth = Column(Date)
    married = Column(Boolean)
    team_id = Column(Integer)

    def __init__(self,
                 dev_id = "",
                 dev_fullname = "no_name",
                 dev_birth = "1984-01-01",
                 married_status = "false",
                 dev_team_id = "1"):
        self.id = dev_id,
        self.fullname = dev_fullname,
        self.birth = dev_birth,
        self.married = married_status,
        self.team_id = dev_team_id

class TeamLeadScheme(Base):
    __tablename__ = "teamleads"

    id = Column(Integer, primary_key=True)
    fullname = Column(String)

    def __init__(self,
                 tl_id = "1",
                 tl_name = "No_name"):
        self.id = tl_id,
        self.fullname = tl_name


class TeamScheme(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    teamlead_id = Column(Integer)
    team_name = Column(String)


    def __init__(self,
                 t_id = "1",
                 t_teamlead_id = "1",
                 t_name = "no_t_name"):
        self.id = t_id
        self.teamlead_id = t_teamlead_id
        self.team_name = t_name


class ProjectScheme(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    type = Column(String)
    status = Column(String)

    def __init__(self,
                 p_id = "1",
                 p_title = "untitled",
                 p_type = "undef_type",
                 p_status = "init"):
        self.id = p_id
        self.title = p_title
        self.type = p_type
        self.status = p_status
