from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class InfoLog(Base):
    __tablename__ = 'info'
    id = Column(Integer, primary_key=True)
    file_name = Column(String(255), nullable=False)
    info_frequency = Column(Integer, nullable=False)
