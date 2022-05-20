from app import app
from app import db, render_template,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash,check_password_hash
from flask_migrate import Migrate

class PitchForm(FlaskForm):
    first_name  = StringField('firstname', validators=[DataRequired()])
    last_name  = StringField('lastname', validators=[DataRequired()])
    user_name  = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    submit = SubmitField('add')


class User(db.Model):
   id = db.Column(db.Integer,primary_key = True)
   user = db.Column(db.String(255))
   
def __repr__(self):
 return f'User {self.username}'

class Pitches(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    user = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return f'User {self.name}'



@app.route('/')
def index():
    pitch = Pitches.query.all()
    return render_template('index.html',post=pitch)


@app.route('/pitches',methods=['GET','POST'])   
def pitches():
    form = PitchForm()
    if form.validate_on_submit():
        user= User(user=form.user_name.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('pitch.html', data=form)

@app.route('/delete/<int:pitch_id>')
def delete(pitch_id):
    pitch = Pitches.query.filter_by(id=pitch_id).first()
    db.session.delete(pitch)
    db.session.commit()
    return redirect(url_for('index'))



@app.shell_context_processor
def make_shell_context():
    return dict(app = app,db = db,User = User, Pitches = Pitches)