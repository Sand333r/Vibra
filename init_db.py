from flask import Flask
from modelos import db, Discos

app = Flask('app')

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# with app.app_context():
#   db.create_all()

with app.app_context():
    disco_1 = Discos(nombre='Motomami', artista="Rosalía", precio="90000", imagen_url="https://i.scdn.co/image/ab67616d0000b2730c179967a265de0fc76382fe")
    disco_2 = Discos(nombre='Renaissance', artista="Beyoncé", precio="110000", imagen_url="https://ca-times.brightspotcdn.com/dims4/default/117d4b4/2147483647/strip/true/crop/3000x3000+0+0/resize/1200x1200!/quality/75/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F08%2Fe4%2F0086df3d4be796701c6c1f2385f5%2Frenaissance-42albumcrop-6-30.jpg")
    db.session.add(disco_1)
    db.session.add(disco_2)
    db.session.commit()