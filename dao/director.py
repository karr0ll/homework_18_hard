from dao.models.director import Director

# DAO для работы с сущностью Director

class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """
        загружает список всех режиссеров
        """
        directors_list = self.session.query(Director).all()

        return directors_list

    def get_one(self, did):
        """
        загружает данные одного режиссера
        """
        director = self.session.query(Director).get(did)

        return director

