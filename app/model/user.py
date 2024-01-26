from app.config.db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(70), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<User {}>'.format(self.name)
    
    def setPassword(self, password):
        self.password = generate_password_hash(password)
        
    def verifyPassword(self, password):
        return check_password_hash(self.password, password)