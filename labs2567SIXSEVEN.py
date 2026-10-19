# 2

phone_book = {}


def add_contact():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    address = input("Введите адрес: ")

    phone_book[name] = {
        "телефон": phone,
        "адрес": address
    }


def show_contacts():
    if not phone_book:
        print("Телефонная книга пуста")
        return

    for name, data in phone_book.items():
        print(f"\nИмя: {name}")
        print(f"Телефон: {data['телефон']}")
        print(f"Адрес: {data['адрес']}")


def find_contact():
    name = input("Введите имя для поиска: ")

    if name in phone_book:
        print("Имя:", name)
        print("Телефон:", phone_book[name]["телефон"])
        print("Адрес:", phone_book[name]["адрес"])
    else:
        print("Контакт не найден")


def delete_contact():
    name = input("Введите имя для удаления: ")

    if name in phone_book:
        del phone_book[name]
        print("Контакт удалён")
    else:
        print("Контакт не найден")


while True:
    print("\n--- Телефонная книга ---")
    print("1. Добавить контакт")
    print("2. Показать все контакты")
    print("3. Найти контакт")
    print("4. Удалить контакт")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        find_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Выход из программы")
        break
    else:
        print("Неверный выбор")


# 5

def average(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)


numbers = [67, 322, 228, 1337, 1488]

result = average(numbers)

print(result)
