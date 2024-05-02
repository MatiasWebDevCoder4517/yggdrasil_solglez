# External
from sqlalchemy import CHAR, VARCHAR, BigInteger, Column, Date, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class ConjugalsChildren(Base):
    __tablename__ = "conjugals_children"

    child_id = Column(BigInteger, primary_key=True)
    generation = Column(Integer, nullable=False)
    num_son_couple = Column(Integer, nullable=False)
    gender = Column(CHAR, nullable=False)
    birth_date = Column(Date, nullable=False)
    names = Column(VARCHAR, nullable=False)
    father_lastname = Column(VARCHAR, nullable=False)
    mother_lastname = Column(VARCHAR, nullable=False)
    relative_id = Column(Integer, nullable=False)
