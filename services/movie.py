from dao.movie import MovieDAO
from flask import request

# сервисы для работы с сущностью Movie

class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def create(self, data):
        """
        реализует логику внесния в БД данных о новом фильме
        """
        return self.dao.create(data)

    def get_one(self, mid):
        """
        реализует логику получения данных об одном фильме по его id
        """
        return self.dao.get_one(mid)

    def get_all(self, director_id=None, genre_id=None, year=None):
        """
        реализует логику получения данных о всех фильмах с фильтрацией по id
        режиссера, жанра, году выпуска
        """
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")

        if director_id:
            return self.dao.get_all_by_director(director_id)

        if genre_id:
            return self.dao.get_all_by_genre(genre_id)

        if year:
            return self.dao.get_all_by_year(year)

        return self.dao.get_all()

    def update(self, data):
        """
        реализует логику обновления данных об одном фильме по его id
        """
        mid = data.get("id")
        movie = self.get_one(mid)

        movie.id = mid
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.dao.update(movie)

    def delete(self, aid):
        """
        реализует логику удаления данных об одном фильме по его id
        """
        return self.dao.delete(aid)










