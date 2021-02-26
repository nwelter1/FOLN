from app import app, db
from flask import render_template, request, redirect, url_for
from app.models import User, check_password_hash
from app.forms import UserInfoForm, LoginForm
from flask_login import login_required, login_user, current_user, logout_user

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/12wk')
def program():
    return render_template('12wk.html')

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n", username, password, email)
        #Create User instance
        user = User(username,email,password)
        #Open and insert into db
        db.session.add(user)
        db.session.commit()
        return redirect('login')
        #Email sender
        # msg = Message(f'Thanks for signing up, {username}!', recipients=[email])
        # msg.body = ('Congrats on your new DJ Pool account! Looking forward to seeing your posts!')
        # msg.html = ('<h1>Welcome to The Chicago DJ Pool</h1>' '<p>You can now access and post to the blog and music database! https://dj-pool.herokuapp.com</p>')
        # mail.send(msg)
    return render_template('register.html', form=form)

    #Login Route
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html', form=form)

#log out route
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

    #admin route
@app.route('/admin')
def admin():
    return render_template('admin.html')