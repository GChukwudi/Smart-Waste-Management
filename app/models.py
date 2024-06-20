from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')
    schedules = db.relationship('Schedule', backref='author', lazy=True)
    recyclings = db.relationship('Recycling', backref='author', lazy=True)
    impact_metrics = db.relationship('ImpactMetric', backref='author', lazy=True)
    materials_recycled = db.relationship('MaterialRecycled', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Recycling(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Recycling('{self.materials}', '{self.date_posted}')"
    
class MaterialRecycled(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(120), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"MaterialRecycled('{self.material}', '{self.count}')"

class ImpactMetric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carbon_saved = db.Column(db.Float, nullable=False)
    energy_saved = db.Column(db.Float, nullable=False)
    date_tracked = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"ImpactMetric('{self.carbon_saved}', '{self.energy_saved}', '{self.date_tracked}')"
