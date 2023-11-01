from src import utils


def test_get_data():
    assert len(utils.get_data('operations.json')) > 0
    assert len(utils.get_data('operations.json')) is not None

def test_get_operetions_executed(test_data):
    assert len(utils.get_operations_executed(test_data)) > 0
    assert len(utils.get_operations_executed(test_data)) is not None
    assert len(utils.get_operations_executed(test_data)) == 4

def test_get_last_five_operations(test_data):
    assert len(utils.get_last_five_operations(test_data, 5)) > 0
    assert len(utils.get_last_five_operations(test_data, 5)) is not None
    assert len(utils.get_last_five_operations(test_data, 5)) == 5
    assert utils.get_last_five_operations(test_data, 5)[0]['date'] == '2023-04-12T17:27:27.896421'


def test_get_formatted(test_data):
    assert len(utils.get_formatted(test_data)) == 5
    assert utils.get_formatted(test_data) is not None