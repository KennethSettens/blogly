from flask import Flask, render_template, url_for, redirect
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.app_context().push()

connect_db(app)

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('list_users.html', users=users)


# @app.route('/users/<int:user_id>')
# def show_user(user_id):
#     return render_template('user_detail.html', user_id=user_id)


# @app.route('/users/new', methods=['GET'])
# def new_user():
#     return render_template('add_user.html')


# @app.route('/users/new', methods=['POST'])
# def add_user():
#     return redirect(url_for('list_users'))


# @app.route('/users/<int:user_id>/edit', methods=['GET'])
# def edit_user(user_id):
#     return render_template('edit_user.html', user_id=user_id)


# @app.route('/users/<int:user_id>/edit', methods=['POST'])
# def update_user(user_id):
#     return redirect(url_for('show_user', user_id=user_id))


# @app.route('/users/<int:user_id>/delete', methods=['POST'])
# def delete_user(user_id):
#     return redirect(url_for('list_users'))


