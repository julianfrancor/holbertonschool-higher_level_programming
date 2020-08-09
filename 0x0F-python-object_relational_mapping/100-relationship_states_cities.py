#!/usr/bin/python3


""" lists all State objects from the database hbtn_0e_6_usa
"""
import sys
# import library to create the connection with the db
from sqlalchemy import create_engine
# Import  library to Traslate from python to SQL language
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    # Cretate engine the starting point for any SQLAlchemy application
    # The call to create_engine doesn’t actually connect to the database
    # right away, it just prepares for when it does need to connect
    # mysql+mysqldb://user:passwd@localhost/my_db
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # This is the function that does the SQL CREATE TABLE...
    # or ALTER TABLE... commands.
    # We passed engine (from the code above) to this function to generate
    # the table(s) that are mapped to objects that inherit from Base.
    Base.metadata.create_all(engine)

    # Here we are defining a class called Session and an instance of that
    # class called sesh. The sessionmaker lets us talk to the database in
    # a controlled environment. This session is bound to our database using
    # the engine we defined above.
    Session = sessionmaker(bind=engine)
    sesh = Session()

    # Querying is done using the .query() method on a Session object.
    # keep in mind the diference btwn filter = SELECT and filter_by = CREATE

    instance_state = State()
    instance_state.name = "California"
    instance_city = City()
    instance_city.name = "San Francisco"
    instance_state.cities.append(instance_city)
    # Add the new elements
    sesh.add(instance_state)
    sesh.add(instance_city)
    # Save changes
    sesh.commit()
    # To close the connection with the db
    sesh.close()
