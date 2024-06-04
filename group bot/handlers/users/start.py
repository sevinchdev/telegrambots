from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from filters.private_chat import IsPrivate
from filters.admins import AdminFilter


@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! Sahifamizga xush kelibsiz!")


@dp.message_handler(AdminFilter(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, admin: {message.from_user.full_name}! Sahifamizga xush kelibsan!")
