class User:
    def __init__(self, ID, name, privileges):
        self.ID = ID
        self.name = name
        self.privileges = privileges

    def read_user_list(self):
        list_users = []
        list_users = User
        print(f"Список пользователей: {list_users}" )

class Admin(User):
    def __init__(self, ID, name, privileges):
        super().__init__(ID, name, privileges)

    def add_user(self, ID, name, privileges):
        pass

    def delete_user(self, name):
        pass

user1 = User("2", "Sergey", "user")
user2 = User("0", "Genadiy", "admin")

print(f"Пользователь - {user1.name}, Уровень доступа - {user1.privileges}")
print(f"Пользователь - {user2.name}, Уровень доступа - {user2.privileges}")

user1.read_user_list()