from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WarnLog(Base):
    __tablename__ = 'warn'
    id = Column(Integer, primary_key=True)
    file_name = Column(String(255), nullable=False)
    warn_frequency = Column(Integer, nullable=False)
