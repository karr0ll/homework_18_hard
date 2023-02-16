from dao.genre import GenreDAO

# сервисы для работы с сущностью Genre

class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        """
        реализует логику получения данных об одном жанре по его id
        """
        return self.dao.get_one(gid)

    def get_all(self):
        """
        реализует логику получения данных обо всех жанрах
        """
        return self.dao.get_all()




