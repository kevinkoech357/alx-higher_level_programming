#!/usr/bin/python3

"""
Changes the name of a State object from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Search for state id to change name
    new_instance = session.query(State).filter_by(id=2).first()
    new_instance.name = 'New Mexico'

    # Commit to db
    session.commit()
