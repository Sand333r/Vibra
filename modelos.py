from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Discos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    artista = db.Column(db.String(30), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    imagen_url = db.Column(db.String(255))