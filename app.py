from flask import Flask, render_template, redirect, session, flash
# from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, User, db
from forms import UserForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///feedbackdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

# toolbar = DebugToolbarExtension(app)

@app.route('/')
def root():
    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])
def create_user():

    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        # new_user = User.register(username, password, email, first_name, last_name)
        # db.session.add(new_user)
        # db.session.commit()
        return redirect('/secret')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data