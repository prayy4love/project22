from functools import reduce

users = [
    {
        'username': 'john_doe',
        'password': 'password123',
        'role': 'user',
        'subscription_type': 'Premium',
        'history': ['Роза', 'Тюльпан'],
        'created_at': '2024-09-01'
    },
    {
        'username': 'admin_user',
        'password': 'admin123',
        'role': 'admin'
    }
]

flowers = [
    {
        'name': 'Роза',
        'price': 50,
        'rating': 4.5,
        'added_date': '2024-09-01'
    },
    {
        'name': 'Тюльпан',
        'price': 30,
        'rating': 4.2,
        'added_date': '2024-09-02'
    },
    {
        'name': 'Лилия',
        'price': 40,
        'rating': 4.7,
        'added_date': '2024-09-03'
    },
    {
        'name': 'Гвоздика',
        'price': 25,
        'rating': 4.0,
        'added_date': '2024-09-04'
    },
    {
        'name': 'Орхидея',
        'price': 60,
        'rating': 4.9,
        'added_date': '2024-09-05'
    }
]

additional_items = [
    {
        'name': 'Плюшевый мишка',
        'price': 100,
        'added_date': '2024-09-06'
    },
    {
        'name': 'Игрушка',
        'price': 80,
        'added_date': '2024-09-07'
    },
    {
        'name': 'Открытка',
        'price': 20,
        'added_date': '2024-09-08'
    },
    {
        'name': 'Ваза',
        'price': 150,
        'added_date': '2024-09-09'
    },
    {
        'name': 'Шоколад',
        'price': 70,
        'added_date': '2024-09-10'
    }
]

bouquets = [
    {
        'name': 'Романтический букет',
        'flowers': ['Роза', 'Тюльпан'],
        'price': 100,
        'rating': 4.8,
        'added_date': '2024-09-11'
    },
    {
        'name': 'Свадебный букет',
        'flowers': ['Лилия', 'Орхидея'],
        'price': 150,
        'rating': 4.9,
        'added_date': '2024-09-12'
    },
    {
        'name': 'Детский букет',
        'flowers': ['Гвоздика', 'Тюльпан'],
        'price': 80,
        'rating': 4.5,
        'added_date': '2024-09-13'
    },
    {
        'name': 'Поздравительный букет',
        'flowers': ['Роза', 'Лилия'],
        'price': 120,
        'rating': 4.7,
        'added_date': '2024-09-14'
    },
    {
        'name': 'Букет на день рождения',
        'flowers': ['Орхидея', 'Гвоздика'],
        'price': 130,
        'rating': 4.6,
        'added_date': '2024-09-15'
    }
]

def register():
    try:
        username = input("Введите логин: ").strip()
        password = input("Введите пароль: ").strip()
        role = input("Выберите роль (user/admin): ").strip().lower()
        if role not in ['user', 'admin']:
            raise ValueError("Неверная роль. Пожалуйста, выберите 'user' или 'admin'.")
        users.append({
            'username': username,
            'password': password,
            'role': role,
            'subscription_type': 'Basic' if role == 'user' else None,
            'history': [],
            'created_at': '2024-09-01'
        })
        print("Регистрация успешна!")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def login():
    try:
        username = input("Введите логин: ").strip()
        password = input("Введите пароль: ").strip()
        user = next((user for user in users if user['username'] == username and user['password'] == password), None)
        if user:
            return user
        else:
            raise ValueError("Неверный логин или пароль.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    return None

def view_flowers():
    print("Доступные цветы:")
    for flower in flowers:
        print(f"{flower['name']} - {flower['price']} руб. (Рейтинг: {flower['rating']})")

def view_additional_items():
    print("Дополнительные товары:")
    for item in additional_items:
        print(f"{item['name']} - {item['price']} руб.")

def view_bouquets():
    print("Доступные букеты:")
    for bouquet in bouquets:
        print(f"{bouquet['name']} - {bouquet['price']} руб. (Рейтинг: {bouquet['rating']}) (Цветы: {', '.join(bouquet['flowers'])})")

def buy_item(user):
    try:
        item_type = input("Выберите тип товара (flower/additional/bouquet): ").strip().lower()
        if item_type not in ['flower', 'additional', 'bouquet']:
            raise ValueError("Неверный тип товара. Пожалуйста, выберите 'flower', 'additional' или 'bouquet'.")

        name = input("Введите название товара: ").strip()
        if item_type == 'flower':
            flower = next((flower for flower in flowers if flower['name'].lower() == name.lower()), None)
            if flower:
                user['history'].append(flower['name'])
                print(f"Цветок {flower['name']} добавлен в корзину.")
            else:
                raise ValueError("Цветок не найден.")
        elif item_type == 'additional':
            item = next((item for item in additional_items if item['name'].lower() == name.lower()), None)
            if item:
                user['history'].append(item['name'])
                print(f"Товар {item['name']} добавлен в корзину.")
            else:
                raise ValueError("Товар не найден.")
        elif item_type == 'bouquet':
            bouquet = next((bouquet for bouquet in bouquets if bouquet['name'].lower() == name.lower()), None)
            if bouquet:
                user['history'].append(bouquet['name'])
                print(f"Букет {bouquet['name']} добавлен в корзину.")
            else:
                raise ValueError("Букет не найден.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def view_history(user):
    print("История покупок:")
    for item in user['history']:
        print(item)

def sort_items():
    try:
        item_type = input("Выберите тип товара (flower/additional/bouquet): ").strip().lower()
        if item_type not in ['flower', 'additional', 'bouquet']:
            raise ValueError("Неверный тип товара. Пожалуйста, выберите 'flower', 'additional' или 'bouquet'.")

        criterion = input("Выберите критерий сортировки (price/rating): ").strip().lower()
        if criterion not in ['price', 'rating']:
            raise ValueError("Неверный критерий сортировки. Пожалуйста, выберите 'price' или 'rating'.")

        if item_type == 'flower':
            sorted_items = sorted(flowers, key=lambda x: x[criterion])
        elif item_type == 'additional':
            sorted_items = sorted(additional_items, key=lambda x: x[criterion])
        elif item_type == 'bouquet':
            sorted_items = sorted(bouquets, key=lambda x: x[criterion])

        for item in sorted_items:
            if item_type == 'bouquet':
                print(f"{item['name']} - {item['price']} руб. (Рейтинг: {item['rating']}) (Цветы: {', '.join(item['flowers'])})")
            else:
                print(f"{item['name']} - {item['price']} руб. (Рейтинг: {item.get('rating', 'N/A')})")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def update_profile(user):
    try:
        new_password = input("Введите новый пароль: ").strip()
        user['password'] = new_password
        print("Пароль успешно изменен.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def add_item():
    try:
        item_type = input("Выберите тип товара (flower/additional/bouquet): ").strip().lower()
        if item_type not in ['flower', 'additional', 'bouquet']:
            raise ValueError("Неверный тип товара. Пожалуйста, выберите 'flower', 'additional' или 'bouquet'.")

        name = input("Введите название товара: ").strip()
        price = float(input("Введите цену: ").strip())
        added_date = input("Введите дату добавления: ").strip()

        if item_type == 'flower':
            rating = float(input("Введите рейтинг: ").strip())
            flowers.append({
                'name': name,
                'price': price,
                'rating': rating,
                'added_date': added_date
            })
        elif item_type == 'additional':
            additional_items.append({
                'name': name,
                'price': price,
                'added_date': added_date
            })
        elif item_type == 'bouquet':
            rating = float(input("Введите рейтинг: ").strip())
            flowers_in_bouquet = input("Введите цветы в букете (через запятую): ").strip().split(',')
            bouquets.append({
                'name': name,
                'flowers': [flower.strip() for flower in flowers_in_bouquet],
                'price': price,
                'rating': rating,
                'added_date': added_date
            })
        print("Товар добавлен.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def delete_item():
    try:
        item_type = input("Выберите тип товара (flower/additional/bouquet): ").strip().lower()
        if item_type not in ['flower', 'additional', 'bouquet']:
            raise ValueError("Неверный тип товара. Пожалуйста, выберите 'flower', 'additional' или 'bouquet'.")

        name = input("Введите название товара для удаления: ").strip()
        if item_type == 'flower':
            global flowers
            flowers = [flower for flower in flowers if flower['name'].lower() != name.lower()]
        elif item_type == 'additional':
            global additional_items
            additional_items = [item for item in additional_items if item['name'].lower() != name.lower()]
        elif item_type == 'bouquet':
            global bouquets
            bouquets = [bouquet for bouquet in bouquets if bouquet['name'].lower() != name.lower()]
        print("Товар удален.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def edit_item():
    try:
        item_type = input("Выберите тип товара (flower/additional/bouquet): ").strip().lower()
        if item_type not in ['flower', 'additional', 'bouquet']:
            raise ValueError("Неверный тип товара. Пожалуйста, выберите 'flower', 'additional' или 'bouquet'.")

        name = input("Введите название товара для редактирования: ").strip()
        if item_type == 'flower':
            flower = next((flower for flower in flowers if flower['name'].lower() == name.lower()), None)
            if flower:
                flower['price'] = float(input("Введите новую цену: ").strip())
                flower['rating'] = float(input("Введите новый рейтинг: ").strip())
                print("Цветок отредактирован.")
            else:
                raise ValueError("Цветок не найден.")
        elif item_type == 'additional':
            item = next((item for item in additional_items if item['name'].lower() == name.lower()), None)
            if item:
                item['price'] = float(input("Введите новую цену: ").strip())
                print("Товар отредактирован.")
            else:
                raise ValueError("Товар не найден.")
        elif item_type == 'bouquet':
            bouquet = next((bouquet for bouquet in bouquets if bouquet['name'].lower() == name.lower()), None)
            if bouquet:
                bouquet['price'] = float(input("Введите новую цену: ").strip())
                bouquet['rating'] = float(input("Введите новый рейтинг: ").strip())
                bouquet['flowers'] = [flower.strip() for flower in input("Введите новые цветы в букете (через запятую): ").strip().split(',')]
                print("Букет отредактирован.")
            else:
                raise ValueError("Букет не найден.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def view_statistics():
    try:
        total_purchases = sum(len(user['history']) for user in users if user['role'] == 'user')
        average_purchase = reduce(lambda x, y: x + y, [sum(map(lambda item: next((flower['price'] for flower in flowers if flower['name'] == item), 0), user['history'])) for user in users if user['role'] == 'user']) / total_purchases if total_purchases > 0 else 0
        print(f"Общее количество покупок: {total_purchases}")
        print(f"Средняя стоимость покупок: {average_purchase:.2f} руб.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def manage_users():
    try:
        action = input("Выберите действие (add/delete/edit): ").strip().lower()
        if action not in ['add', 'delete', 'edit']:
            raise ValueError("Неверное действие. Пожалуйста, выберите 'add', 'delete' или 'edit'.")

        if action == 'add':
            register()
        elif action == 'delete':
            username = input("Введите логин пользователя для удаления: ").strip()
            global users
            users = [user for user in users if user['username'].lower() != username.lower()]
            print("Пользователь удален.")
        elif action == 'edit':
            username = input("Введите логин пользователя для редактирования: ").strip()
            user = next((user for user in users if user['username'].lower() == username.lower()), None)
            if user:
                user['password'] = input("Введите новый пароль: ").strip()
                print("Пользователь отредактирован.")
            else:
                raise ValueError("Пользователь не найден.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def main():
    while True:
        print("Добро пожаловать в цветочный магазин!")
        print("1. Регистрация")
        print("2. Вход")
        print("3. Выйти")
        choice = input("Выберите действие: ").strip()

        if choice == '1':
            register()
        elif choice == '2':
            user = login()
            if user:
                if user['role'] == 'user':
                    user_menu(user)
                elif user['role'] == 'admin':
                    admin_menu()
        elif choice == '3':
            break
        else:
            print("Неверный выбор.")

def user_menu(user):
    while True:
        print("Меню пользователя:")
        print("1. Просмотреть доступные цветы")
        print("2. Просмотреть дополнительные товары")
        print("3. Просмотреть доступные букеты")
        print("4. Купить товар")
        print("5. Просмотреть историю покупок")
        print("6. Сортировать товары")
        print("7. Обновить профиль")
        print("8. Выйти")
        choice = input("Выберите действие: ").strip()

        if choice == '1':
            view_flowers()
        elif choice == '2':
            view_additional_items()
        elif choice == '3':
            view_bouquets()
        elif choice == '4':
            buy_item(user)
        elif choice == '5':
            view_history(user)
        elif choice == '6':
            sort_items()
        elif choice == '7':
            update_profile(user)
        elif choice == '8':
            break
        else:
            print("Неверный выбор.")

def admin_menu():
    while True:
        print("Меню администратора:")
        print("1. Добавить товар")
        print("2. Удалить товар")
        print("3. Редактировать товар")
        print("4. Просмотреть статистику")
        print("5. Управление пользователями")
        print("6. Выйти")
        choice = input("Выберите действие: ").strip()

        if choice == '1':
            add_item()
        elif choice == '2':
            delete_item()
        elif choice == '3':
            edit_item()
        elif choice == '4':
            view_statistics()
        elif choice == '5':
            manage_users()
        elif choice == '6':
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
