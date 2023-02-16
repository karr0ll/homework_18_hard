from dao.genre import GenreDAO

from flask import request


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

    def check_and_add_genres(self, data):
        """
        проверяет наличие жанра в таблице
        добавляет новый жанр, если его нет в таблицe
        """
        all_genres = self.dao.get_all()
        requested_genre = data.get("genre")

        all_genres_response = []
        for item in all_genres:
            all_genres_response.append(item.name)

        if requested_genre not in all_genres_response:
            genre_max_id = self.dao.get_max_id()
            requested_genre.id = genre_max_id[1] + 1,
            requested_genre.name = requested_genre.get("name")

            return self.dao.create(requested_genre)


