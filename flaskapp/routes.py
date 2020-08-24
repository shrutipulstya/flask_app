from flask import render_template, url_for, flash, redirect, request
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User, Post
from flaskapp import db, app, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author' : 'shruti pulstya',
        'title' : 'blog post 1',
        'content' : 'first post content',
        'date_posted' : 'aug 18,2020'   
    },
    {
        'author' : 'lionel messi',
        'title' : 'blog post 2',
        'content' : 'seocond post content',
        'date_posted' : 'aug 19,2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'about')   

@app.route('/register',methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        bcrypt.generate_password_hash(form.password.data)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('your Account has been created! you are now able to log in!', 'success')
        return(redirect( url_for('login')) )
    return render_template('register.html', title ='register', form=form)

@app.route('/login',methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
            user = User.query.filter_by(email = form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data ):
                login_user(user, remember = form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:
                flash('login unsuccessful! please check email and password', 'danger')
    return render_template('login.html', title ='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
   return render_template('account.html', title ='Account') 