from unittest.mock import Mock


def test_mockachino():
    mock_one = Mock()
    mock_one.mockachino = '1 чашка'
    assert mock_one.mockachino == '1 чашка'


def test_sugar():
    mock_one = Mock()
    mock_one.configure_mock(sugar="1 ложка")
    assert mock_one.sugar == "1 ложка"


def test_calculate():
    mock_one = Mock()
    mock_one.calculate.return_value = 505
    assert mock_one.calculate() == 505
