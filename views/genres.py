from flask_restx import Resource, Namespace

from dao.models.genre import genres_schema, genre_schema
from container import genre_service

genres_ns = Namespace("genres")

# вью для работы с http запросами по namespace genres


@genres_ns.route("/")
class GenresView(Resource):  # Получение всех
    def get(self):
        """
        получает все жанры
        """
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genres_ns.route("/<int:gid>")
class GenresView(Resource):
    def get(self, gid: int):
        """
        получает один жанр по его id
        """
        try:
            genre = genre_service.get_one(gid)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return str(e), 404



