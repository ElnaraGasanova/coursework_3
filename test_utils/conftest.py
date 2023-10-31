import pytest


@pytest.fixture
def test_data():
    return [
        {
            "id": 542678139,
            "state": "CANCELED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": "90582.51",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        {
            "id": 558167602,
            "state": "EXECUTED",
            "date": "2023-04-12T17:27:27.896421",
            "operationAmount": {
                "amount": "43861.89",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 73654108430135874305",
            "to": "Счет 89685546118890842412"
        },
        {
            "id": 407169720,
            "state": "EXECUTED",
            "date": "2018-02-03T14:52:08.093722",
            "operationAmount": {
                "amount": "67011.26",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 4047671689373225",
            "to": "Maestro 3806652527413662"
        },
        {
            "id": 361044570,
            "state": "EXECUTED",
            "date": "2018-03-02T02:03:11.563721",
            "operationAmount": {
                "amount": "7484.91",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 96008924215040031147",
            "to": "Счет 30377212495530283001"
        },
        {
            "id": 536723678,
            "state": "EXECUTED",
            "date": "2018-06-12T07:17:01.311610",
            "operationAmount": {
                "amount": "26334.08",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Classic 4195191172583802",
            "to": "Счет 17066032701791012883"
        }
    ]