from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sql_alchemy.config.database import Base

class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True, Index = True)
    name = Column(String)
    email = Column(String)
    telefone = Column(String)