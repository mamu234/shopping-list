
from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash,check_password_hash
from flask_migrate import Migrate



app = Flask(__name__)





app.config['SECRET_KEY']='123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True

db = SQLAlchemy(app)

migrate = Migrate(app,db)

bootstrap = Bootstrap(app)

class PitchForm(FlaskForm):
    first_name  = StringField('firstname', validators=[DataRequired()])
    last_name  = StringField('lastname', validators=[DataRequired()])
    user_name  = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    submit = SubmitField('add')

  






  






if __name__ == "__main__":
    
    app.run(debug=True)