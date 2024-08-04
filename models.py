from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    __table_args__ = {'extend_existing': True}
    def __repr__(self):
        return f'<User {self.username}>'

