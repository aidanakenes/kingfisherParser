from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

Base = declarative_base()


class ItemTable(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(String)
    title = Column(String)
    category = Column(String)
    subcategory = Column(String)
    price = Column(String)
    city = Column(String)
    url = Column(String)
