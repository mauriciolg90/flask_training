# For class code and table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

# For database configuration
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Base class for the table
Base = declarative_base()

# Create the class and extend it from the base class
class Indicators(Base):
    __tablename__ = 'indicators'

    id = Column(Integer(), primary_key=True)
    location = Column(String(8), nullable=False)
    country = Column(String(24), nullable=False)
    indicator_code = Column(String(16))
    indicator_full = Column(String(64))
    measure_code = Column(String(8))
    measure_full = Column(String(24))
    inequality_code = Column(String(8))
    inequality_full = Column(String(24))
    unit_code = Column(String(8))
    unit_full = Column(String(24))
    powercode_code = Column(String(8))
    powercode_full = Column(String(16))
    reference_period_code = Column(String(24))
    reference_period_full = Column(String(24))
    value = Column(Float(2))
    flag_codes = Column(String(8))
    flags = Column(String(24))

    def __repr__(self):
        return "<Indicators(id='{0}', location='{1}', country='{2}')>".format(
            self.id, self.location, self.country)

    @property
    def serialize_all(self):
        return {
            'id': self.id,
            'location' : self.location,
            'country' : self.country,
            'indicator_code' : self.indicator_code,
            'indicator_full' : self.indicator_full,
            'measure_code' : self.measure_code,
            'measure_full' : self.measure_full,
            'inequality_code' : self.inequality_code,
            'inequality_full' : self.inequality_full,
            'unit_code' : self.unit_code,
            'unit_full' : self.unit_full,
            'powercode_code' : self.powercode_code,
            'powercode_full' : self.powercode_full,
            'reference_period_code' : self.reference_period_code,
            'reference_period_full' : self.reference_period_full,
            'value' : self.value,
            'flag_codes' : self.flag_codes,
            'flags' : self.flags,
        }

# Configure engine for the database (dialect and driver) FIXME: sacar la configuracion de un archivo
engine = create_engine('mysql+pymysql://mauri:280490mg@localhost:3306/flask_test', echo=True)
Base.metadata.create_all(engine)

# Create a session for the engine
Session = sessionmaker(bind=engine)
session = Session()