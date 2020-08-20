from flask import Flask,render_template, url_for,flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '750dde4b9025b0222244fc643b99e32f'

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
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        flash('Account created for ' + username + '!', 'success')
        return(redirect( url_for('home')) )
    return render_template('register.html', title ='register', form=form)

@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in !', 'success')
            return(redirect( url_for('home')) )
        else:
            flash('login unsuccessful! please check username and password', 'danger')
    return render_template('login.html', title ='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)