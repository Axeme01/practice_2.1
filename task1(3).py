import csv
import os

def read_csv(filename):
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['Название', 'Цена', 'Количество']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            initial_data = [
                {'Название': 'Яблоки', 'Цена': 100, 'Количество': 50},
                {'Название': 'Бананы', 'Цена': 80, 'Количество': 30},
                {'Название': 'Молоко', 'Цена': 120, 'Количество': 20},
                {'Название': 'Хлеб', 'Цена': 40, 'Количество': 100}
            ]
            writer.writerows(initial_data)
        return initial_data
    else:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)

def add_product(data):
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))

    data.append({
        'Название': name,
        'Цена': price,
        'Количество': quantity
    })

def search_product(data):
    name = input("Введите название товара для поиска: ").strip()
    for product in data:
        if product['Название'].lower() == name.lower():
            print(f"Товар '{product['Название']}' найден.")
            print(f"Цена: {product['Цена']} руб., Количество: {product['Количество']}")
            break
    else:
        print("Товар не найден")

def calculate_total_cost(data):
    total_cost = sum(float(product['Цена']) * int(product['Количество']) for product in data)
    print(f'Общая стоимость всех товаров на складе: {total_cost:.2f} рублей')

def save_to_csv(filename, data):
    fieldnames = ['Название', 'Цена', 'Количество']
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    filename = 'products.csv'
    data = read_csv(filename)

    while True:
        print("\nМеню:")
        print("1. Просмотреть список товаров")
        print("2. Добавить новый товар")
        print("3. Найти товар по названию")
        print("4. Посчитать общую стоимость товаров на складе")
        print("5. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            # Показываем таблицу товаров
            for i, product in enumerate(data):
                print(
                    f"{i + 1}. Название: {product['Название']}, Цена: {product['Цена']} руб., Количество: {product['Количество']}")

        elif choice == '2':
            add_product(data)
            save_to_csv(filename, data)

        elif choice == '3':
            search_product(data)

        elif choice == '4':
            calculate_total_cost(data)

        elif choice == '5':
            print("Завершение программы...")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")