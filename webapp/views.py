from flask import render_template, flash, redirect, request, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm, RegisterForm
from models import User
from webapp import webapp, login_manager
from models import db, User

login_manager.login_view = 'login'

@webapp.route('/', methods=['GET', 'POST'])
@webapp.route('/<error>', methods=['GET', 'POST'])
def login(error = None):
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data.lower()).first()
        if user and user.verify_password(form.password.data):
            login_user(user, remember = True)
            return redirect(url_for('secret'))

        else:
            error = "Wrong username or password"
            return render_template('login.html', form=form, error=error)
    else:
        return render_template('login.html', form=form, error = error)

@webapp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_manager.user_loader
def load_user(id):
    return User.query.get((id))

@webapp.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data.lower()).first()
        if user is not None:
            error = "You already have an account. Please log in"
            return redirect(url_for('login', error = error))
        else:
            user = User(form.email.data.lower(), form.password.data)            
            db.session.add(user)
            db.session.commit()
            login_user(user, remember = True)
            return redirect(url_for('secret'))

    return render_template('register.html', form=form)

@webapp.route('/secret')
@login_required
def secret():
    #with open('pigs.txt') as f:        
    #    data = f.readlines()
    #if current_user.is_authenticated():
    data = ["Secret Page man!"]
    return render_template('secret.html', data=data)        