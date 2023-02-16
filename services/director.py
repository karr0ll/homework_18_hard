from dao.director import DirectorDAO

# сервисы для работы с сущностью Director

class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        """
        реализует логику получения данных об одном режиссере по его id
        """
        return self.dao.get_one(did)

    def get_all(self):
        """
        реализует логику получения данных обо всех режиссерах
        """
        return self.dao.get_all()




