# This is the main application file. It contains the code for the routes, database models, and login functionality.

# Import the necessary modules
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import login_user, login_required, logout_user, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager

# Create the application instance
app = Flask(__name__)

# Set the secret key for the application
app.config['SECRET_KEY'] = "nitin"

# Set the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

# Create the SQLAlchemy instance
db = SQLAlchemy(app)
app.app_context().push()

# Create the LoginManager instance
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Define the user loader function
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


# Define the Todo model
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(300), nullable=False)
    status = db.Column(db.String(100), default='')
    Date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Define the representation of the Todo object
    # def __repr__(self):
    #     return '<Task %r>' % self.id
    # def __repr__(self) -> str:
    #     return f"{self.sno}-{self.title}"

# Define the User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # notes = db.relationship('Note')

# Define the route for the home page
@app.route("/", methods=['GET', 'POST'])
@login_required
def Add():
    # If the request method is POST, create a new Todo object
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc, user_id=current_user.id)
        db.session.add(todo)
        db.session.commit()

    # Get all the Todo objects for the current user
    newtodo = Todo.query.filter_by(user_id=current_user.id).all()

    # Render the home page template
    return render_template('index.html', newtodo=newtodo, user=current_user)

# Define the route for deleting a Todo object
@app.route('/delete/<int:sno>')
@login_required
def delete(sno):
    # Get the Todo object to be deleted
    todo = Todo.query.filter_by(sno=sno).first()

    # Delete the Todo object
    db.session.delete(todo)
    db.session.commit()

    # Redirect to the home page
    return redirect("/")

# Define the route for updating a Todo object
@app.route('/update/<int:sno>', methods=['GET', 'POST'])
@login_required
def update(sno):
    # If the request method is POST, update the Todo object
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        checked = ''
        try:
            checked = request.form['flexSwitchCheckChecked']
            print(checked)
        except:
            pass

        # Get the Todo object to be updated
        todo = Todo.query.filter_by(sno=sno).first()

        # Update the Todo object
        if checked == 'on':
            todo.status = 'on'
        else:
            todo.status = ''

        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()

        # Redirect to the home page
        return redirect("/")

    # Get the Todo object to be updated
    todo = Todo.query.filter_by(sno=sno).first()

    # Render the update page template
    return render_template('update.html', user=current_user, todo=todo)

# Define the route for signing up
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # If the request method is POST, create a new User object
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Check if the email already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstname) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Create a new User object
            new_user = User(email=email, first_name=firstname, password=generate_password_hash(password1, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash(f'Logged in as {new_user.first_name}!', category='success')
            return redirect('/')

    # Render the signup page template
    return render_template('signup.html', user=current_user)

# Define the route for logging in
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the request method is POST, check the credentials
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the email exists
        user = User.query.filter_by(email=email).first()
        if user:
            # Check if the password is correct
            if check_password_hash(user.password, password):
                flash(f'Logged in as {user.first_name}!', category='success')
                login_user(user, remember=True)
                return redirect('/')
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exists.', category='error')

    # Render the login page template
    return render_template('login.html', user=current_user)

# Define the route for logging out
@app.route('/logout')
@login_required
def logout():
    # Logout the user
    logout_user()
    return redirect('/login')

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
