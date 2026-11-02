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

