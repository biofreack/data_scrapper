# pylint: disable=C0103
"""Database setup"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.environ.get('DATABASE'), pool_size=20, max_overflow=0)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

