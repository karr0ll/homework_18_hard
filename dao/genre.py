from dao.models.genre import Genre
from sqlalchemy import func


# DAO для работы с сущностью Genre

class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """
        загружает список всех жанров
        """
        genres_list = self.session.query(Genre).all()
        return genres_list

    def get_one(self, gid):
        """
        загружает данные одного жанра
        """
        genre = self.session.query(Genre).get(gid)
        return genre

    def get_max_id(self):
        """
        получает последний id
        """
        max_id = self.session.query(Genre, func.max(Genre.id)).one()
        return max_id

    def create(self, requested_genre):
        """
        создает новый фильм
        """
        genre = Genre(**requested_genre)
        self.session.add(genre)
        self.session.commit()

        return genre
