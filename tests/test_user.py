from unittest.mock import Mock, patch

from my_pck import User


class TestUser:
    def test_get_data_by_id(self):
        user_data = {"id": 1, "name": "test"}
        mock_data = Mock()
        mock_data.get.return_value = user_data

        user = User(mock_data)

        assert user.get_user(1) == user_data

    @patch("my_pck.User.upload_photo", return_value="OK")
    def test_create_user_profile(self, mock_upload_photo):
        user = User({})

        assert user.create_user_profile("photo.png") == "Профиль создан"
