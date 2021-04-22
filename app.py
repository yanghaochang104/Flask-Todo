from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import keys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = keys.DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# setup schema
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    
    def __repr__(self):
        return f'Todo {self.id} {self.description}'

# create table
db.create_all()

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())
