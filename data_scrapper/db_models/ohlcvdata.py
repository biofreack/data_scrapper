# pylint: disable=E0402
from sqlalchemy import Column, Integer, BigInteger, Text, String, DateTime, Float, DECIMAL
from ..db_config import Base

class OhlcvdataModel(Base):

    __tablename__ = 'ohlcvdata'
    id = Column(Integer, primary_key=True)
    cryptoid = Column(Integer())
    name = Column(String(length=70))
    event_date = Column(DateTime)
    open = Column(DECIMAL(22,8))
    high = Column(DECIMAL(22,8))
    low = Column(DECIMAL(22,8))
    close = Column(DECIMAL(22,8))
    volume = Column(DECIMAL(22,8))
    marketcap = Column(DECIMAL(22,8))
    import_date = Column(DateTime)
