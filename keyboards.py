from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from service import *

users_key = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌍 Places")],
        [KeyboardButton(text="❓ Help"), KeyboardButton(text="❌ Cancel")]
    ],
    resize_keyboard=True
)


admin_key = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Add Place"), KeyboardButton(text="✏️ Update Place")],
        [KeyboardButton(text="🗑️ Delete Place"), KeyboardButton(text="📁 Add Category")],
        [KeyboardButton(text="✏️ Update Category"), KeyboardButton(text="🗑️ Delete Category")],
        [KeyboardButton(text="🌍 Places")],
        [KeyboardButton(text="❓ Help"), KeyboardButton(text="❌ Cancel")]
    ],
    resize_keyboard=True
)

async def get_category_places_button():
    data = await get_category()
    keyboards = []
    for category in data:
        keyboards.append([InlineKeyboardButton(text=f"{category['category_name']}", callback_data=f"category_order_{category['category_id']}")])
    keybor = InlineKeyboardMarkup(inline_keyboard=keyboards)
    return keybor


async def get_places_order_button(cat_id):
    data = await get_places_cat_id(cat_id)
    keyboards = []
    for place in data:
        keyboards.append([InlineKeyboardButton(text=f"📍 {place['title']} ({place['city']})", callback_data=f"place_show_{place['places_id']}")])
    keybor = InlineKeyboardMarkup(inline_keyboard=keyboards)
    return keybor

def get_saved_places_button(place_id):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⭐ Save in favorites", callback_data=f"save_place_{place_id}")]
        ]
    )
    return keyboard

async def get_category_button():
    data = await get_category()
    keyboards = []
    for category in data:
        keyboards.append([InlineKeyboardButton(text=f"📁 {category['category_name']}", callback_data=f"category_{category['category_id']}")])
    keybor = InlineKeyboardMarkup(inline_keyboard=keyboards)
    return keybor

async def get_category_edit_button():
    data = await get_category()
    keyboards = []
    for category in data:
        keyboards.append([InlineKeyboardButton(text=f"✏️ {category['category_name']}", callback_data=f"cat_edit_{category['category_id']}")])
    keybor = InlineKeyboardMarkup(inline_keyboard=keyboards)
    return keybor

async def get_category_delete_button():
    data = await get_category()
    keyboards = []
    for category in data:
        keyboards.append([InlineKeyboardButton(text=f"🗑️ {category['category_name']}", callback_data=f"cat_del_{category['category_id']}")])
    keybor = InlineKeyboardMarkup(inline_keyboard=keyboards)
    return keybor
