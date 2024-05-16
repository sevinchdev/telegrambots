import wikipedia
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6418745914:AAHvFUnw6XmGECQYdOuF0bpeWeWvd2IVPcQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
wikipedia.set_lang('uz')


@dp.message_handler(commands=['start', 'help'])
async def hello(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu aleykum \nWikipedia botimizga xush kelibsiz.")



@dp.message_handler()
async def get_data(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    try:
        matn=message.text
        await message.answer(wikipedia.summary(matn))
    except:
        await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)