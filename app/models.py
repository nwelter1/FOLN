# from app import app, db
# from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime
# from flask_login import UserMixin

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), nullable=False, unique=True)
#     email = db.Column(db.String(150), nullable=False, unique=True)
#     password = db.Column(db.String(256), nullable=False)
#     post = db.relationship('Post', backref='author', lazy=True)
#     comment = db.relationship('Comment', backref='author', lazy=True)

#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = self.set_password(password)

#     def set_password(self, password):
#         return self.pw_hash

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200))
#     post = db.Column(db.String(200))
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     user_id = db.relationship('User', db.ForeignKey('user.id'))
#     comment = db.relationship('Comment', db.ForeignKey('comment.id'), lazy=True)

#     def __init__(self, title, post, user_id):
#         self.title = title
#         self.post = post
#         self.user_id = user_id

#     def __repr__(self):
#         return f'The title of the post is {self.title} \n and the content is {self.post}.'

# class Comment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     comment = db.Column(db.String(500))
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     user_id = db.relationship('User', db.ForeignKey('user.id'), nullable=False)
#     post = db.relationship('Post', db.ForeignKey('post.id'), nullable=False)

#     def __init__(self, title, user_id):
#         self.comment = title
#         self.user_id = user_id

#     def __repr__(self):
#         return f'The title of the post is {self.comment} \n has been added to {self.post}.'