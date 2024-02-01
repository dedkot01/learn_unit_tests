import time


class User:
    def __init__(self, user_data) -> None:
        self.user = user_data

    def get_user(self, user_id):
        return self.user.get(user_id)

    def upload_photo(self, photo):
        time.sleep(30)  # имитируем медленную работу метода
        return 'OK'

    def create_user_profile(self, photo_path):   # создаём профиль пользователя
        result = self.upload_photo(photo_path)
        if result == 'OK':
            return 'Профиль создан'
        else:
            return 'Не удалось создать профиль'
