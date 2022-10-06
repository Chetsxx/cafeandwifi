from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

engine = create_engine("sqlite:///cafes.db")

Base.prepare(autoload_with=engine)

Cafe = Base.classes.cafe

session = Session(engine)

cafes = session.query(Cafe).all()

for cafe in cafes:
    if cafe.name == "here":
        session.delete(cafe)
        session.commit()


# collection-based relationships are by default named
# "<classname>_collection"