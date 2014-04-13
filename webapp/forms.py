from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, validators,BooleanField
from wtforms.validators import Required, Email, EqualTo

class RegisterForm(Form):
    email    = TextField('email', [Required(), Email()])
    password = PasswordField('New Password', [Required(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
 
class LoginForm(Form):
    email = TextField('email', validators = [Required(), Email()])
    password = PasswordField('password', validators = [Required()])
    
    #email = TextField('email')
    #password = PasswordField('password')
'''
class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)    
'''   