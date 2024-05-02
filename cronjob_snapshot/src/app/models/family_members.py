# External
from sqlalchemy import CHAR, VARCHAR, BigInteger, Column, Date, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class FamilyMembers(Base):
    __tablename__ = "family_members"

    member_id = Column(BigInteger, primary_key=True)
    generation = Column(Integer, nullable=False)
    num_gen = Column(Integer, nullable=False)
    gender = Column(CHAR, nullable=False)
    birth_date = Column(Date, nullable=False)
    names = Column(VARCHAR, nullable=False)
    father_lastname = Column(VARCHAR, nullable=False)
    mother_lastname = Column(VARCHAR, nullable=False)
    relative_id = Column(Integer, nullable=False)
