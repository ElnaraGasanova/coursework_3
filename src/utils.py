import json
from datetime import datetime


def get_data(filename):
    """Функция загружает файл .json"""
    with open(filename, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        return data


def get_operations_executed(data):
    """Функция добавляет в список операции, в которых
    статус = "Выполнен" и указан Отправитель"""
    operations_executed = []
    for operation in data:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            operations_executed.append(operation)

    operations_from = []
    for operation in operations_executed:
        if 'from' in operation:
            operations_from.append(operation)
    return operations_from


def get_last_five_operations(operation_from, operations_num):
    """Функция выводит последние пять операций"""
    operations_sorted = sorted(operation_from, key=lambda operation: operation['date'], reverse=True)
    last_five_operations = operations_sorted[0:operations_num]
    return last_five_operations


def get_formatted(last_five_operations):
    """Функция форматирует вывод данных:
    дата перевода, описание перевода,
    откуда, куда, сумма перевода, валюта"""
    formatted_list = []
    for operation in last_five_operations:
        date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')

        description = operation['description']

        payer_info, payment_mathod = "", ""

        if "from" in operation:
            payer = operation['from'].split()
            payment_mathod = payer.pop(-1)
            if payer[0] == 'Счет':
                payment_mathod_from = f"**{payment_mathod[-4:]}"
            else:
                payment_mathod_from = f"{payment_mathod[-4:]} {payment_mathod[4:6]}** **** {payment_mathod[-4:]}"
            payer_info = " ".join(payer)
        beneficiary = f"{operation['to'].split()[0]} **{operation['to'][-4:]}"
        operation_amount = f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"
        formatted_list.append(f"{date} {description}\n{payer_info} {payment_mathod_from} -> {beneficiary}\n"
                              f"{operation_amount}")
    return formatted_list
