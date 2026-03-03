import logging
from datetime import datetime

logging.basicConfig(filename='calculator.log', level=logging.INFO, format='[%(asctime)s] %(message)s')


def show_last_operations():
    try:
        with open('calculator.log', 'r') as file:
            lines = file.readlines()
            print("Последние выполненные операции:")
            for line in lines[-5:]:
                print(line.strip())
    except FileNotFoundError:
        print("Файл лога пока пуст.")


def clear_log_file():
    """ Очистка содержимого log-файла """
    with open('calculator.log', 'w'):
        pass
    print("Лог-файл успешно очищен!")


def calculate_and_log(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            raise ValueError("Деление на ноль невозможно")
    else:
        raise ValueError(f"Операция '{operation}' неизвестна.")

    logging.info(f"{num1} {operation} {num2} = {result}")
    return result


if __name__ == "__main__":
    while True:
        print("\nПростой калькулятор с логированием\n")
        show_last_operations()

        choice = input("Выберите действие:\n1. Вычислить выражение\n2. Очистить журнал\n3. Выход\nВаш выбор: ")

        if choice == '1':
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                op = input("Введите операцию (+, -, *, /): ")

                result = calculate_and_log(num1, num2, op)
                print(f"Результат: {result}\nЗапись сохранена в лог-файл.")

            except Exception as e:
                print(f"Произошла ошибка: {e}")

        elif choice == '2':
            clear_log_file()

        elif choice == '3':
            break

        else:
            print("Неверный ввод. Попробуйте снова.")