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







@router.callback_query(F.data.startswith('category_order_'))
async def show_menu_places(callback: CallbackQuery):
    cat_id = callback.data.split("_")[-1]
    await callback.message.answer("Choose a place:", reply_markup=await get_places_order_button(cat_id))
    await callback.answer()
    

    
    
@router.callback_query(F.data.startswith('place_show_'))
async def show_place(callback: CallbackQuery):
    place_id = callback.data.split("_")[-1]
    data = await get_places_id(place_id)
    if not data:
        await callback.answer("Can't find any places..", show_alert=True)
        return
    caption_text = f"""
📍   {data['title']}  
🏙   Country:   {data['city']}
📁   Category:   {data['category_name']}
📝   Caption:  {data['description']}
"""
    await callback.message.answer_photo(photo=data['file_id'], caption=caption_text)
    await callback.answer()
