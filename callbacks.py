from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from service import *
from keyboards import *

router = Router()


@router.message(F.text == "🌍 Places")
@router.message(Command("places"))
async def show_menu(message: Message):
    await message.answer("Choose category:", reply_markup=await get_category_places_button())







@router.callback_query(F.data.startswith('categoris_'))
async def show_menu_places(callback: CallbackQuery):
    cat_id = callback.data.split("_")[-1]
    await callback.message.answer("Choose a place:", reply_markup=await get_places_order_button(cat_id))
    await callback.answer()
    

    
    
@router.callback_query(F.data.startswith('place_show_'))
async def show_place(callback: CallbackQuery):
    place_id = callback.data.split("_")[-1]
    data = await get_places_id(place_id)
    if not data:
        await callback.answer("Can't find any places..")
        return
    caption_text = f"""
📍   {data['title']}  
🏙   Country:   {data['city']}
📁   Category:   {data['category_name']}
📝   Caption:  {data['description']}
"""
    await callback.message.answer_photo(photo=data['file_id'], caption=caption_text, reply_markup=await get_saved_places_button(place_id))
    await callback.answer()

@router.callback_query(F.data.startswith('save_place_'))
async def save_place_handler(callback: CallbackQuery):
    place_id = callback.data.split("_")[-1]
    await save_place_user(callback.from_user.id, place_id)
    await callback.answer("⭐ Place saved in Favorites!")

@router.callback_query(F.data.startswith('del_fav_'))
async def delete_favorite_handler(callback: CallbackQuery):
    place_id = callback.data.split("_")[-1]
    await delete_saved_place_db(callback.from_user.id, place_id)
    await callback.answer("🗑️ Place removed from Favorites!")
    await callback.message.delete()