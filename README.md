## AWS EC2 Hosted webapp Link:
## http://ec2-18-224-60-49.us-east-2.compute.amazonaws.com:8080/

## flask_app setup

### $ pip install Flask

### $ pip install -U Flask-SQLAlchemy

### $ pip install flask-bcrypt

### $ pip install flask-login

### $ pip install Flask-Mail

### $ pip install flask-wtf

### $ pip install email_validator

### //create a bash profile
#### $ touch .bash_profile

### //open the bash profile
#### $ nano .bash_profile

### //add these tenvironment variables
#### export EMAIL_USER='youremail@gmail.com'
#### export EMAIL_PASS='Yourpassword'
#### export SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
#### export SECRET_KEY='secretkeyxxxxxxxxxxxxxxxx'

