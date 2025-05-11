from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin  # 🔑 Import this

db = SQLAlchemy()

class User(db.Model, UserMixin):  # ✅ Inherit from UserMixin
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<User {self.username}>'

class PersonalityResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    answers = db.Column(db.Text, nullable=False)
    result = db.Column(db.String(100), nullable=False)
    
    user = db.relationship('User', backref=db.backref('responses', lazy=True))
    
    def __repr__(self):
        return f'<PersonalityResponse {self.result}>'
