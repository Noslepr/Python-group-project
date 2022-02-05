from .db import db

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    titleImage = db.Column(db.Text, nullable=False)
    overview = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    user = db.relationship('User', back_populates='project')
    instruction = db.relationship('Instruction', back_populates='project')
