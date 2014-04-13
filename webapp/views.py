from flask import render_template, flash, redirect, request, url_for
from webapp import webapp

from forms import LoginForm

@webapp.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Logged in!")
        return redirect(url_for('secret'))
    else:
        flash("Cne't pas logged in...")
        return render_template('login.html', form=form)
        
@webapp.route('/secret')
def secret():
    #with open('pigs.txt') as f:        
    #    data = f.readlines()
    #if current_user.is_authenticated():
    data = ["Secret Page man!"]
    return render_template('secret.html', data=data)        