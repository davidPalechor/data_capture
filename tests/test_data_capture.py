import pytest

from data_capture import DataCapture


@pytest.fixture
def setup_data_capture():
    capture = DataCapture()
    capture.add(4)
    capture.add(2)
    capture.add(5)
    capture.add(1)
    capture.add(3)
    capture.add(3)
    capture.add(6)
    capture.add(9)
    capture.add(7)
    capture.add(8)
    return capture.build_stats()


@pytest.mark.parametrize('number, greater_than', [
    (4, 5),
    (8, 1),
    (7, 2),
    (1, 9),
    (2, 8)
])
def test_greater(setup_data_capture, number: int, greater_than: int):
    assert setup_data_capture.greater(number) == greater_than


@pytest.mark.parametrize('number, less', [
    (1, 0),
    (9, 9),
    (8, 8),
    (7, 7),
    (2, 1),
    (4, 4)
])
def test_less(setup_data_capture, number, less):
    assert setup_data_capture.less(number) == less


@pytest.mark.parametrize('start, end, between', [
    (3, 6, 5),
    (1, 4, 5),
    (2, 8, 8),
    (8, 9, 2),
])
def test_less(setup_data_capture, start, end, between):
    assert setup_data_capture.between(start, end) == between
