import json
import os

LIBRARY_FILE = 'library.json'
AVAILABLE_BOOKS_FILE = 'available_books.txt'

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return []

def save_library(library):
    with open(LIBRARY_FILE, 'w', encoding='utf-8') as file:
        json.dump(library, file, ensure_ascii=False, indent=4)

def view_all_books():
    library = load_library()
    if not library:
        print("Библиотека пуста.")
    else:
        for book in library:
            print(
                f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Доступность: {book['available']}")

def search_book(query):
    library = load_library()
    found_books = [book for book in library if
                   query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]
    if not found_books:
        print("Книга не найдена.")
    else:
        for book in found_books:
            print(
                f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Доступность: {book['available']}")

def add_book():
    library = load_library()
    new_id = len(library) + 1
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = int(input("Введите год издания книги: "))
    available = input("Книга доступна? (Да/Нет): ").lower() == 'Да1'
    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year,
        "available": available
    }
    library.append(new_book)
    save_library(library)
    print("Книга добавлена в библиотеку.")

def change_availability():
    library = load_library()
    book_id = int(input("Введите ID книги для изменения статуса: "))
    book = next((book for book in library if book['id'] == book_id), None)
    if book:
        book['available'] = not book['available']
        save_library(library)
        print(f"Статус доступности книги '{book['title']}' изменен.")
    else:
        print("Книга с таким ID не найдена.")

def delete_book():
    library = load_library()
    book_id = int(input("Введите ID книги для удаления: "))
    book = next((book for book in library if book['id'] == book_id), None)
    if book:
        library.remove(book)
        save_library(library)
        print(f"Книга '{book['title']}' удалена из библиотеки.")
    else:
        print("Книга с таким ID не найдена.")

def export_available_books():
    library = load_library()
    available_books = [book for book in library if book['available']]
    with open(AVAILABLE_BOOKS_FILE, 'w', encoding='utf-8') as file:
        for book in available_books:
            file.write(f"Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}\n")
    print("Список доступных книг экспортирован в файл available_books.txt.")

def main_menu():
    while True:
        print("\nМеню:")
        print("1. Просмотр всех книг")
        print("2. Поиск книги по автору/названию")
        print("3. Добавление новой книги")
        print("4. Изменение статуса доступности книги")
        print("5. Удаление книги по ID")
        print("6. Экспорт списка доступных книг")
        print("7. Выход")
        choice = input("Выберите действие (1-7): ")

        if choice == '1':
            view_all_books()
        elif choice == '2':
            query = input("Введите название или автора для поиска: ")
            search_book(query)
        elif choice == '3':
            add_book()
        elif choice == '4':
            change_availability()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            export_available_books()
        elif choice == '7':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main_menu()