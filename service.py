from connection import *

async def create_user(username, full_name, telegram_id):
    try:
        conn = await connection_db()
        await conn.execute("""
        insert into users(username, full_name, telegram_id) values
        ($1, $2, $3) 
        """, username, full_name, str(telegram_id))
    except Exception as Error:
        print(f"Create user Error: {Error}")
    finally:
        await conn.close()


async def get_user_by_id(telegram_id):
    try:
        conn = await connection_db()
        user = await conn.fetchrow("""
        select * from users 
        where telegram_id = $1
        """, str(telegram_id))
        return user
    except Exception as Error:
        print(f"Get user by id Error: {Error}")
    finally:
        await conn.close()


async def check_admin(telegram_id):
    try:
        conn = await connection_db()
        users = await conn.fetchrow("""
        select * from users 
        where telegram_id = $1 and is_admin = true
        """, str(telegram_id))
        return users
    except Exception as Error:
        print(f"Get user Error: {Error}")
    finally:
        await conn.close()


async def create_category_db(title):
    try:
        conn = await connection_db()
        await conn.execute("""
        insert into category(category_name) values
        ($1) 
        """, title)
        return True
    except Exception as Error:
        print(f"Create category Error: {Error}")
        return False
    finally:
        await conn.close()


async def get_category():
    try:
        conn = await connection_db()
        categorys = await conn.fetch("""
        select * from category
        """)
        return categorys
    except Exception as Error:
        print(f"Get categorys Error: {Error}")
    finally:
        await conn.close()


async def update_category_db(category_id, new_title):
    try:
        conn = await connection_db()
        await conn.execute("""
        update category 
        set category_name = $1 where category_id = $2
        """, new_title, int(category_id))
        return True
    except Exception as Error:
        print(f"Update category error: {Error}")
        return False
    finally:
        await conn.close()


async def delete_category_db(category_id):
    try:
        conn = await connection_db()
        await conn.execute("""
        delete from category 
        where category_id = $1
        """, int(category_id))
        return True
    except Exception as Error:
        print(f"Delete category error: {Error}")
        return False
    finally:
        await conn.close()


async def create_places_db(category_id, title, city, description, file_id):
    try:
        conn = await connection_db()
        await conn.execute("""
        insert into places(category_id, title, city, description, file_id) values
        ($1, $2, $3, $4, $5) 
        """, int(category_id), title, city, description, file_id)
        return True
    except Exception as Error:
        print(f"Create place Error: {Error}")
        return False
    finally:
        await conn.close()

