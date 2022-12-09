from sqlite import DataBase


def test():
    db = DataBase()
    db.create_table_users()
    db.add_user(1, "one", 'email')
    db.add_user(2, "two", 'email')
    db.add_user(3, "three", 'email')
    db.add_user(4, "four", 'email')
    db.add_user(5, "five", 'email')

    users = db.select_all_users()
    print(f"Barcha foydalanuvchilar: {users}")

    user = db.select_user(Name="five", id=5)
    print(f"Bitta foydalanuvchini ko'rish {user}")


test()
