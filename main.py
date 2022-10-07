from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields import URLField, SelectField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

Base = automap_base()
engine = create_engine("sqlite:///cafes.db", connect_args={"check_same_thread": False})
Base.prepare(autoload_with=engine)
Cafe = Base.classes.cafe
session = Session(engine)
cafes = session.query(Cafe).all()


class AddCafe(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    map = URLField("Map Url", validators=[DataRequired(), URL(message="Invalid link")])
    img = URLField("Image Url", validators=[DataRequired(), URL(message="Invalid link")])
    seats = StringField('Seat Availability', validators=[DataRequired()])
    coffee_price = StringField('Coffee Price', validators=[DataRequired()])
    toilet = SelectField('Coffee', choices=['Yes', 'No'], validators=[DataRequired()])
    wifi = SelectField('Coffee', choices=['Yes', 'No'], validators=[DataRequired()])
    power = SelectField('Coffee', choices=['Yes', 'No'], validators=[DataRequired()])
    calls = SelectField('Coffee', choices=['Yes', 'No'], validators=[DataRequired()])
    submit = SubmitField('Add Cafe')


@app.route("/")
def home():
    return render_template("index.html", cafes=cafes)

@app.route("/delete-cafe")
def delete():
    cafe_name = request.args.get("name")
    for cafe in cafes:
        if cafe.name == cafe_name:
            session.delete(cafe)
            session.commit()
    return redirect(url_for('home'))

@app.route("/add-cafe", methods=["GET", 'POST'])
def add_cafe():
    form = AddCafe()
    if form.validate_on_submit():
        if form.power.data == "Yes":
            form.power.data = True
        else:
            form.power.data = False

        if form.wifi.data == "Yes":
            form.wifi.data = True
        else:
            form.wifi.data = False

        if form.calls.data == "Yes":
            form.calls.data = True
        else:
            form.power.data = False

        if form.toilet.data == "Yes":
            form.toilet.data = True
        else:
            form.toilet.data = False

        session.add(Cafe(name=form.cafe.data, map_url=form.map.data, img_url=form.img.data, location=form.location.data,
                         has_sockets=form.power.data, has_toilet=form.toilet.data, has_wifi=form.wifi.data,
                         can_take_calls=form.calls.data, seats=form.seats.data,
                         coffee_price=form.coffee_price.data))
        session.commit()
        return redirect(url_for('home'))
    return render_template("add_cafe.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)

