import pytest
from src.cinema_entry import can_watch


@pytest.mark.parametrize(
    ("age", "expected"),
    [
        (0, False),  # infant
        (15, False),  # below 16
        (16, True),  # exactly 16 — allowed per spec
        (17, True),  # above 16
        (65, True),  # adult
    ],
)
def test_can_watch_valid(age, expected):
    result = can_watch(age)
    assert result is expected
    assert type(result) is bool


@pytest.mark.parametrize(
    "age",
    [
        16.0,  # float is not int
        "16",  # string is not int
        True,  # bool is not a valid int per spec
        None,
        {"age": 16},
    ],
)
def test_can_watch_invalid_type_raises_type_error(age):
    with pytest.raises(TypeError):
        can_watch(age)


def test_can_watch_negative_raises_value_error():
    with pytest.raises(ValueError):
        can_watch(-1)
