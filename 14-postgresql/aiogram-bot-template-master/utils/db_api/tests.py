from postgresql import DataBase

import asyncio


async def test():
    db = DataBase()
    await db.create()

    await db.create_table_users()

    await db.add_user('Umidjon', 'hope', 123456)
    await db.add_user('Odiljon', 'sariqdev', 123457)
    await db.add_user('Ali', 'sqriqdev', 123458)
    await db.add_user('Vali', 'sqriqdev', 123459)
    await db.add_user('Sobir', 'sobir', 123450)

    users = db.select_all_users()
    print(f"Barcha foydalanuvchilar {users}")

    user = db.select_user(id=5)
    print(f"Foydalanuvchi {user}")


asyncio.run(test())
