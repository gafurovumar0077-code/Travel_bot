from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from service import *
from keyboards import *

router = Router()

class AddPlace(StatesGroup):
    get_catgory_id = State()
    get_name = State()
    get_city = State()      
    get_caption = State() 
    get_photo_id = State()
    
class AddCategory(StatesGroup):
    get_title = State()

class UpdateCategory(StatesGroup):
    get_category_id = State()
    get_new_title = State()

class UpdatePlace(StatesGroup):
    get_category_id = State()
    get_place_id = State()
    get_name = State()
    get_city = State()
    get_caption = State()
    get_photo_id = State()




@router.message(F.text == "❌ Cancel")
@router.message(Command("cancel"))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("❌ Command canceled.")







@router.message(F.text == "📁 Add Category")
@router.message(Command("add_category"))
async def add_category(message: Message, state: FSMContext):
    if await check_admin(message.from_user.id):
        await message.answer("Enter name of category:")
        await state.set_state(AddCategory.get_title)
    else:
        await message.answer("Only admin can Add category!")
        await state.clear()

@router.message(AddCategory.get_title)
async def add_category_title(message: Message, state: FSMContext):
    title = message.text.strip()
    status = await create_category_db(title)
    if status:
        await message.answer(f"✅ Category «{title}» added!")
    else:
        await message.answer("Error while adding category!")
    await state.clear()







@router.message(F.text == "✏️ Update Category")
async def update_category_start(message: Message, state: FSMContext):
    if await check_admin(message.from_user.id):
        await message.answer("Choose category name for update:", reply_markup=await get_category_edit_button())
        await state.set_state(UpdateCategory.get_category_id)

@router.callback_query(UpdateCategory.get_category_id, F.data.startswith("cat_edit_"))
async def update_category_select(callback: CallbackQuery, state: FSMContext):
    cat_id = callback.data.split("_")[-1]
    await state.update_data(category_id=cat_id)
    await callback.message.answer("Enter a new name of category:")
    await state.set_state(UpdateCategory.get_new_title)
    await callback.answer()

@router.message(UpdateCategory.get_new_title)
async def update_category_finish(message: Message, state: FSMContext):
    data = await state.get_data()
    status = await update_category_db(data['category_id'], message.text.strip())
    if status:
        await message.answer("✅ Category updated succesfuly!")
    else:
        await message.answer("Error while updating category!")
    await state.clear()








@router.message(F.text == "🗑️ Delete Category")
async def del_category_start(message: Message):
    if await check_admin(message.from_user.id):
        button = await get_category_delete_button()
        await message.answer("Choose category for deleteing:", reply_markup=button)

@router.callback_query(F.data.startswith("cat_del_"))
async def del_category_finish(callback: CallbackQuery):
    cat_id = callback.data.split("_")[-1]
    await delete_category_db(cat_id)
    await callback.message.answer("🗑️ Category deleted!")
    await callback.answer()





