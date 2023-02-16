from dao.models.genre import Genre

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

    def get_one(self, did):
        """
        загружает данные одного жанра
        """
        genre = self.session.query(Genre).get(did)
        return genre
