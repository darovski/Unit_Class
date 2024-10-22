class User:
    def __init__(self, ID, name, privileges):
        self._ID = ID
        self._name = name
        self._privileges = privileges

    # Методы для доступа к защищённым атрибутам
    def get_ID(self):
        return self._ID

    def get_name(self):
        return self._name

    def get_privileges(self):
        return self._privileges

    def set_name(self, name):
        self._name = name

    def set_privileges(self, privileges):
        self._privileges = privileges


class Admin(User):
    def __init__(self, ID, name, privileges):
        super().__init__(ID, name, privileges)
        self._users_list = []

    def add_user(self, ID, name, privileges):
        new_user = User(ID, name, privileges)
        self._users_list.append(new_user)
        print(f"Пользователь {name} добавлен.")

    def remove_user(self, name):
        for user in self._users_list:
            if user.get_name() == name:
                self._users_list.remove(user)
                print(f"Пользователь {name} удален.")
                return
        print(f"Пользователь {name} не найден.")

    # Метод для отображения всех пользователей
    def show_users(self):
        for user in self._users_list:
            print(f"ID: {user.get_ID()}, Имя: {user.get_name()}, Привилегии: {user.get_privileges()}")


admin = Admin("1", "AdminUser", "admin")
admin.add_user("1", "AdminUser", "admin")
admin.add_user("2", "Sergey", "user")
admin.add_user("3", "Alexey", "user")

print("Список пользователей:")
admin.show_users()

admin.remove_user("Sergey")

print("Список пользователей после удаления:")
admin.show_users()

