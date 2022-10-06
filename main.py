from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

app = Flask(__name__)
Base = automap_base()
engine = create_engine("sqlite:///cafes.db")
Base.prepare(autoload_with=engine)
Cafe = Base.classes.cafe
session = Session(engine)
cafes = session.query(Cafe).all()

@app.route("/")
def home():
    return render_template("index.html", cafes=cafes)

if __name__ == '__main__':
    app.run(debug=True)

