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



async def get_places_cat_id(category_id):
    try:
        conn = await connection_db()
        places = await conn.fetch("""
        select * from places 
        where category_id = $1
        """, int(category_id))
        return places
    except Exception as Error:
        print(f"Get places by cat_id Error: {Error}")
    finally:
        await conn.close()


async def get_places_id(place_id):
    try:
        conn = await connection_db()
        place = await conn.fetchrow("""
        select p.*, c.category_name from places p 
        join category c on p.category_id = c.category_id 
        where p.places_id = $1
        """, int(place_id))
        return place
    except Exception as Error:
        print(f"Get places by id Error: {Error}")
    finally:
        await conn.close()


async def update_places_db(place_id, title, city, description, file_id):
    try:
        conn = await connection_db()
        await conn.execute("""
        update places 
        set title = $1, city = $2, description = $3, file_id = $4
        where places_id = $5
        """, title, city, description, file_id, int(place_id))
        return True
    except Exception as Error:
        print(f"Update places error: {Error}")
        return False
    finally:
        await conn.close()


async def delete_places_db(places_id):
    try:
        conn = await connection_db()
        await conn.execute("""
        delete from places 
        where places_id = $1
        """, int(places_id))
        return True
    except Exception as Error:
        print(f"Delete places error: {Error}")
        return False
    finally:
        await conn.close()


async def save_place_user(telegram_id, place_id):
    conn = await connection_db()
    try:
        user = await conn.fetchrow("""
select user_id from users 
where telegram_id = $1""", str(telegram_id))
        if user:
            await conn.execute("""
insert into saved_places(user_id, places_id) values 
($1, $2)""", user['user_id'], int(place_id))
    except Exception as Error:
        print(f"Save place error: {Error}")
    finally:
        await conn.close()



async def get_my_places_db(telegram_id):
    conn = await connection_db()
    try:
        user = await conn.fetchrow("""
select user_id from users 
where telegram_id = $1""", str(telegram_id))
        if not user:
            return []
        places = await conn.fetch("""
        select p.places_id, p.title, p.city from saved_places s
        join places p on s.places_id = p.places_id
        where s.user_id = $1
        """, user['user_id'])
        return places
    except Exception as Error:
        print(f"Get my places error: {Error}")
        return []
    finally:
        await conn.close()
        



async def delete_saved_place_db(telegram_id, place_id):
    conn = await connection_db()
    try:
        user = await conn.fetchrow("""
select user_id from users 
where telegram_id = $1""", str(telegram_id))
        if user:
            await conn.execute(
                """
delete from saved_places 
where user_id = $1 and places_id = $2""", user['user_id'], int(place_id)
            )
            return True
        return False
    except Exception as Error:
        print(f"Delete saved place error: {Error}")
        return False
    finally:
        await conn.close()