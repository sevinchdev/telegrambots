from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart(deep_link='jonibekdevv'))
async def bot_start(message: types.Message):
    args=message.get_args()
    text=f"Salom, {message.from_user.full_name}!"
    text+=f"Sizni {args} tavsiya qildi."
    await message.answer(text)
