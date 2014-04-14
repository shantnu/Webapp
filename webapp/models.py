from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from passlib.apps import custom_app_context as pwd_context
import pdb

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(128))
    
    def __init__(self, email, password):
        self.email = email.lower()
        self.password_hash = self.hash_password(password)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def hash_password(self, password):
        return pwd_context.encrypt(password)

    def verify_password(self, password):
        try:
            return pwd_context.verify(password, self.password_hash)        
        except:
            return False

if __name__ == '__main__':
    manager.run()
    
#a = User(email = "a@a.com", password = "a")
#db.session.add(a)
#db.session.commit()    

#>>> User.query.get(1).email
#u'a@a.com'

#>>> User.query.filter_by(email = "ssa@ass.cdom").all()  ->wronmg
#[]

# Correct
#>>> uu= User.query.filter_by(email = "a@a.com").all()
#>>> for u in uu:
#...   print u.id
#...
#1
#>>> for u in uu:
#...   print u.email
#...
#a@a.com