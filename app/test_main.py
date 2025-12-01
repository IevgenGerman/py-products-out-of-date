import pytest

from unittest import mock

import datetime

from app.main import outdated_products


def get_data() -> list:
    outdated_products_list = ([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ])
    return [
        (datetime.date(2022, 1, 10), outdated_products_list, []),
        (datetime.date(2025, 3, 1), outdated_products_list,
         ["salmon", "chicken", "duck"]),
    ]


data_for_test = get_data()


@pytest.mark.parametrize("dataset",
                         data_for_test)
@mock.patch("app.main.datetime.date")
def test_outdated_products(mock_datatime: mock.MagicMock,
                           dataset: list) -> None:
    dat_now, data_outdated_products, expected = dataset
    mock_datatime.today.return_value = dat_now
    result = outdated_products(data_outdated_products)
    assert result == expected
