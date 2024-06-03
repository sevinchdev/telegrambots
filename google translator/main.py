from googletrans import Translator
from aiogram import executor, types, Bot, Dispatcher
import logging

API_TOKEN="7240197747:AAGYdqNItVgtezP4yGmwjGwDDCdumDWNCNQ"

logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)
translator=Translator()


@dp.message_handler(commands=['start','help'])
async def help(message:types.Message):
    await message.answer("Assalomu aleykum botimizga xush kelibsiz! \n Matningizni yuboring")

@dp.message_handler()
async def get_data(message:types.Message):
    translation=translator.translate(message.text,dest="korean")
    translated_text=translation.text
    await message.reply(translated_text)

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)