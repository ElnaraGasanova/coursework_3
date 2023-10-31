from src import utils
import datetime

def main():
    filename = 'operations.json'
    amount_of_operation = 5

    data = utils.get_data(filename)
    operations_executed = utils.get_operations_executed(data)
    last_num_operations = utils.get_last_num_operations(operations_executed, amount_of_operation)
    formatted = utils.get_formatted(last_num_operations)

    for string in formatted:
        print(f"{string}\n")


if __name__ == "__main__":
    main()