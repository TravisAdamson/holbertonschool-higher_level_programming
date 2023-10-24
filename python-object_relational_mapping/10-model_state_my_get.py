#!/usr/bin/python3
""" Prints the the given state from the database hbtn_0e_6_usa """
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == argv[4]).first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print('Not found')
