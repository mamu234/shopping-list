from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


class ShoppingForm(FlaskForm):
    item = StringField('item', validators=[DataRequired()])
    quantity = StringField('quantity', validators=[DataRequired()])
    submit = SubmitField('add')

  


app = Flask(__name__)

app.config['SECRET_KEY']='123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://carolyne:123@localhost/list'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


class Shopping(db.Model):
    __tablename__ = 'lists'
    id = db.Column(db.Integer,primary_key = True)
    item = db.Column(db.String(255))
    amount = db.Column(db.String(150))
    


@app.route('/')
def index():
    items = Shopping.query.all()
    return render_template('index.html',goods=items)


@app.route('/items',methods=['GET','POST'])   
def items():
    form = ShoppingForm()
    if form.validate_on_submit():
        item = Shopping(item=form.item.data, amount=form.quantity.data)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('list.html', data=form)

@app.route('/delete/<int:item_id>')
def delete(item_id):
    item = Shopping.query.filter_by(id=item_id).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))



@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Shopping=Shopping)
        

if __name__ == "__main__":
    
    app.run(debug=True)