from flask_restx import Resource, Namespace
from flask import request

from dao.models.movie import movies_schema, movie_schema
from container import movie_service, director_service, genre_service

movies_ns = Namespace("movies")


# вью для работы с http запросами по namespace movies

@movies_ns.route("/")
class MoviesView(Resource):
    def get(self):
        """
        получает все фильмы
        """
        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        """
        добавляет новый фильм
        """
        request_json = request.json
        genre_service.check_and_add_genre(request_json)
        director_service.check_and_add_director(request_json)
        movie_service.create(request_json)
        return "", 201, {'location': 'sqlite:///movies.db'}


@movies_ns.route("/<int:mid>")
class MoviesView(Resource):
    def get(self, mid: int):
        """
        получает один фильм по его id
        """
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return str(e), 404

    def put(self, mid: int):
        """
        обновляет один фильм по его id
        """
        data = request.json
        data["id"] = mid

        genre_service.check_and_add_genre(data)
        director_service.check_and_add_director(data)
        movie_service.update(data)

        return "", 200

    def delete(self, mid: int):
        """
        удаляет один фильм по его id
        """
        try:
            movie_service.delete(mid)
            return "", 204
        except:
            return f" Такой записи в базе нет", 404
