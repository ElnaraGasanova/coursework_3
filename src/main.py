from src import utils


def main():
    filename = 'operations.json'
# можно ввести любое необходимое количество операций для вывода.
    amount_of_operation = 7

    data = utils.get_data(filename)
    operations_executed = utils.get_operations_executed(data)
    last_five_operations = utils.get_last_five_operations(operations_executed, amount_of_operation)
    formatted = utils.get_formatted(last_five_operations)

    for string in formatted:
        print(f"{string}\n")


if __name__ == "__main__":
    main()