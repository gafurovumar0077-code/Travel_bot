from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
from states import router as state_router
from callbacks import router as callback_router
from connection import create_table
from service import get_user_by_id, check_admin, create_user
from keyboards import admin_key, users_key
import asyncio
import os


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_bot(message: Message):
    user = await get_user_by_id(message.from_user.id)
    if not user:
        await create_user(username=message.from_user.username, full_name=message.from_user.full_name, telegram_id=message.from_user.id
        )
        
    is_admin = await check_admin(message.from_user.id)
    if is_admin:
        await message.answer(
            f"""
👋 Wellcome, Admin @{message.from_user.username}!
🛠 You can control places and categories
            """, reply_markup=admin_key)
    else:
        await message.answer(
            f"""
🌟 Hello, @{message.from_user.username}!
🌍 Explore beautiful places and add them to your favorites!
            """, reply_markup=users_key)



@dp.message(F.text == "❓ Help")
@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        """
        📋 Commands Guide:
/places — View places by category
/my_places — View your saved places
        """)
    
    
async def main():
    await create_table()
    print("Bot started...")
    dp.include_router(state_router)
    dp.include_router(callback_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

