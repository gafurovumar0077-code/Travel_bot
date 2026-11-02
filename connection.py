import os
import asyncpg
from dotenv import load_dotenv

load_dotenv()
pasw = os.getenv("PASSWORD_DB")

async def connection_db():
    try:
        conn = await asyncpg.connect(
            host="localhost",
            port=5432,
            user="postgres",
            database="travel_bd",
            password=pasw
        )
        return conn
    except Exception as Error:
        print(f"Connection Error: {Error}")
        return None

async def create_table():
    conn = await connection_db()
    try:
        await conn.execute("""
        create table if not exists users(
            user_id serial primary key,
            full_name varchar(100),
            username varchar(100),
            telegram_id text unique,
            is_admin boolean default false,
            created_at timestamp default now(),
            is_active boolean default true
        );
               
        create table if not exists category(
            category_id serial primary key,
            category_name varchar(100) unique,
            created_at timestamp default now(),
            is_active boolean default true
        );
                           
        create table if not exists places(
            places_id serial primary key,
            title varchar(255),
            category_id int references category(category_id) on delete cascade,
            city varchar(100),
            description text,
            file_id text
        );
        
        create table if not exists saved_places(
            id serial primary key,
            user_id bigint references users(user_id) on delete cascade,
            places_id int references places(places_id) on delete cascade,
            saved_at timestamp default now()
        );
        """)
        print("Tables created succesfully!")
    except Exception as Error:
        print(f"Create Error: {Error}")
    finally:
        await conn.close()

