from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

SUPERUSER=[929847731]
BLACKLIST=[642362195]

@dp.message_handler(chat_id=SUPERUSER,text='secret')
async def id_handler(message:types.Message):
    await message.answer("Xush kelibsiz, SuperUser!")
    