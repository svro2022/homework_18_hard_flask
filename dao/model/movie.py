# здесь модель SQLAlchemy для сущности,
# также могут быть дополнительные методы работы с моделью
# (но не с базой, с базой мы работает в классе DAO)

from setup_db import db
from marshmallow import Schema, fields
from .genre import Genre
from .director import Director


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    rating = db.Column(db.Float)
    year = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = db.relationship('Genre')
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    director = db.relationship('Director')

class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    rating = fields.Float()
    year = fields.Int()

    #genre_id = fields.Int()
    #director_id = fields.Int()

