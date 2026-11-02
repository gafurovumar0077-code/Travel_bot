from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from service import *
from keyboards import *

router = Router()


class AddCategory(StatesGroup):
    get_title = State()




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




