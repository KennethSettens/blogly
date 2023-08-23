from flask import Flask, render_template, redirect, request, url_for
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.app_context().push()

connect_db(app)
db.create_all()

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def list_users():
    users = User.query.all()
    print(users)
    return render_template('list_users.html', users=users)


@app.route('/users/<int:user_id>')
def show_user(user_id):
    user = User.query.get(user_id)
    return render_template('userDetails.html', user=user)


@app.route('/users/new', methods=['GET'])
def new_user():
    return render_template('newUser.html')


@app.route('/users/new', methods=['POST'])
def add_user():
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    image_url = request.form['imageurl']

    new_user = User(
        FirstName=first_name, LastName=last_name, imageurl=image_url)

    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')    


@app.route('/users/<int:user_id>/edit', methods=["GET"])
def users_edit(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('editUser.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=['POST'])
def users_update(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user_to_delete = User.query.get(user_id)  
    if user_to_delete:
        db.session.delete(user_to_delete)  
        db.session.commit() 
        print("User deleted successfully")
    else:
        print("User not found")
    
    return redirect('/users')


