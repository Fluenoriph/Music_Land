import datetime
from sqlalchemy import create_engine, Column, Integer, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import ARRAY, REAL
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
import json
import requests


'''
engine = create_engine("postgresql://postgres:robov@localhost:5432/lab_calcs", echo=True)
base = declarative_base()


class CalculatorType(base):
    __tablename__ = 'calculator_type'
    calc_type_id = Column(Integer, primary_key=True, autoincrement=False, nullable=False) # не автоинкр., так как нужен ручной контроль.
    calc_type_name = Column(Text, nullable=False)


class RegistrationTime(base):
    __tablename__ = 'registration_time'
    reg_time_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    reg_time_value = Column(DateTime, insert_default=datetime.datetime.now())
    calc_type_id = Column(Integer, ForeignKey('calculator_type.calc_type_id'), nullable=False)


class FormulaTypeCalculatorData(base):
    __tablename__ = 'formula_type_calculator_data'
    data_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    parameter = Column(ARRAY(REAL)) # not null ???
    result = Column(ARRAY(REAL))
    reg_time_id = Column(Integer, ForeignKey('registration_time.reg_time_id'), nullable=False)


class NoiseCalculatorData(base):
    __tablename__ = 'noise_calculator_data'
    data_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    source_level = Column(ARRAY(REAL))
    background_level = Column(ARRAY(REAL))
    delta = Column(ARRAY(REAL))
    result = Column(ARRAY(REAL))
    reg_time_id = Column(Integer, ForeignKey('registration_time.reg_time_id'), nullable=False)


with Session(autoflush=False, bind=engine) as database_session:
    reg_time_data = RegistrationTime(calc_type_id = 2) # ВРЗ
    database_session.add(reg_time_data)
    database_session.commit()
    database_session.refresh(reg_time_data)

    formula_type_calculator_data = FormulaTypeCalculatorData(parameter = [3000, 21.4, 758, 0.00025, 0.00147],
                                                             result = [1.0, 0], reg_time_id = reg_time_data.reg_time_id)
    database_session.add(formula_type_calculator_data)
    database_session.commit()

print("\nДанные добавлены в базу !")
'''

# Получаем данные от интерфейса юзера -------------------------------------------------

# Ventilation_calc. data
user_typed_data = [63.4, 3.2, 3.8, 15, 15, 307.8, 1.5] # 7 item, is rectangle hole

calc_data_json_dump = json.dumps(user_typed_data)
print(calc_data_json_dump)

response = requests.post("http://localhost:8000/", json=calc_data_json_dump)
print(response.text)













