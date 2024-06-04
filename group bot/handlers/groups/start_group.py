from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from filters.group_chat import IsGroup


@dp.message_handler(IsGroup(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! Guruhimizga xush kelibsiz!")
