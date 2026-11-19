import pytest
from src.cinema_price import ticket_price


@pytest.mark.parametrize(
    ("ticket_count", "expected"),
    [
        (0, 0),  # zero tickets costs zero (spec requirement)
        (1, 1200),  # one ticket at 1200 cents
        (2, 2400),  # multiple tickets
        (5, 6000),
    ],
)
def test_ticket_price_valid(ticket_count, expected):
    result = ticket_price(ticket_count)
    assert result == expected
    assert type(result) is int


@pytest.mark.parametrize(
    "ticket_count",
    [
        1.5,  # float is not int
        "2",  # string is not int
        True,  # bool is not a valid int per spec
        None,
        [1],
    ],
)
def test_ticket_price_invalid_type_raises_type_error(ticket_count):
    with pytest.raises(TypeError):
        ticket_price(ticket_count)


def test_ticket_price_negative_raises_value_error():
    with pytest.raises(ValueError):
        ticket_price(-1)
