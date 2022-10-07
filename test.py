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

#                 <!--{% extends 'bootstrap/base.html' %}-->
# <!--{% import 'bootstrap/wtf.html' as wtf %}-->
# <!--{% block styles %}-->
# <!--{{super()}}-->
# <!--<link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">-->
# <!--{% endblock %}-->
# <!--                      {{ wtf.quick_form(form, novalidate=True, button_map={"submit": "warning text-dark"}) }}-->