from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="admin", email="pl1_3@hotmail.com")
session.add(User1)
session.commit()

# Menu for Loving Hut
restaurant1 = Restaurant(name="Loving Hut", user_id="1")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Rolling Tango",
                     description="Entree",
                     price="$13.99", restaurant=restaurant1, user_id=1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Fried Rice",
                     description=" Rice with vegetables",
                     price="$14.50",  restaurant=restaurant1, user_id=1)

session.add(menuItem2)
session.commit()



# Menu for Taco Bell
restaurant2 = Restaurant(name="Taco Bell")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Bean Burrito",
                     description="Torilla with beans.",
                     price="$1.99", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Cheesy Bean and Rice Burrito",
                     description="Rice, beans and cheese burrito",
                     price="$2",  restaurant=restaurant2)

session.add(menuItem2)
session.commit()




print "Added order items!"
