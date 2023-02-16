from dao.models.director import Director
from dao.models.genre import Genre
from dao.models.movie import Movie
from data import data
from setup_db import db


def create_data():
    """создает и наполняет БД"""
    with db.session.begin():
        db.create_all()

    for movie in data["movies"]:
        m = Movie(
            id=movie["pk"],
            title=movie["title"],
            description=movie["description"],
            trailer=movie["trailer"],
            year=movie["year"],
            rating=movie["rating"],
            genre_id=movie["genre_id"],
            director_id=movie["director_id"]
        )
        db.session.add(m)

    for director in data["directors"]:
        d = Director(
            id=director["pk"],
            name=director["name"]
        )
        db.session.add(d)

    for genre in data["genres"]:
        d = Genre(
            id=genre["pk"],
            name=genre["name"],
        )
        db.session.add(d)
        db.session.commit()