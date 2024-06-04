from aiogram import types
from loader import dp

@dp.message_handler(hashtags='homework')
@dp.message_handler(cashtags=['eur','usd'])
async def hashtags(message:types.Message):
    await message.answer("Siz hashtag yubordingiz.")