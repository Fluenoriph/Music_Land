from sqlalchemy import create_engine, Column, Integer, DateTime, ForeignKey, Text, Sequence
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://postgres:robov@localhost:5432/lab_calcs", echo=True)

base = declarative_base(engine)

class CalculatorType(base):
    __tablename__ = 'calculator_type'
    calc_type_id = Column(Integer, primary_key=True, autoincrement=False, nullable=True)
    calc_type_name = Column(Text, nullable=True)


class RegistrationTime(base):
    __tablename__ = 'registration_time'
    reg_time_id = Column(Integer, primary_key=True, autoincrement=True)
    reg_time_value = Column(DateTime)
