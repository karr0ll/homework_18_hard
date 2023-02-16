from flask_restx import Resource, Namespace

from dao.models.director import directors_schema, director_schema
from container import director_service

directors_ns = Namespace("directors")

# вью для работы с http запросами по namespace directors
@directors_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        """
        получает всех режиссеров
        """
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@directors_ns.route("/<int:did>")
class DirectorsView(Resource):
    def get(self, did: int):
        """
        получает одного режиссера по его id
        """
        try:
            director = director_service.get_one(did)
            return director_schema.dump(director), 200
        except Exception as e:
            return str(e), 404



