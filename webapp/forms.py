from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, validators,BooleanField
from wtforms.validators import Required, Email, EqualTo
from models import db, User

class RegisterForm(Form):
    email    = TextField('email', [Required(), Email()])
    password = PasswordField('New Password', [Required(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
 
class LoginForm(Form):
    email = TextField('email', validators = [Required(), Email()])
    password = PasswordField('password', validators = [Required()])
    
    #email = TextField('email')
    #password = PasswordField('password')

    def validate(self, email, password):
        user = User.query.filter_by(email = self.email.data.lower()).all()
        if user and user[0].verify_password(self.password.data):
            return True
        else:
            return False    
            
#>>> user[0].verify_password("a")
#True
#>>> user[0].verify_password("b")
#False

            