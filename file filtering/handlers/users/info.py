from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from aiogram.utils.markdown import hbold, hcode, hitalic,hunderline,hstrikethrough,hlink

from loader import dp

@dp.message_handler(commands='info_html')
async def bot_help(message:types.Message):
    text=f"Assalomu aleykum, {message.from_user.full_name}!\n"
    text+="Bu <b>qalin</b> shrift.\n"
    text += "Bu <b>qalin</b> shrift.\n"
    text += "Bu <i>qalin</i> shrift.\n"
    text += "Bu <u>qalin</u> shrift.\n"
    text += "Bu <s>qalin</s> shrift.\n"
    text += "Bu <a href='https://kun.uz'> Kun Uz sahifasi</a>\n"
    text += "Bu <code> print('Hello World') </code>\n"

    await message.reply(text)

@dp.message_handler(commands='info_markdown')
async def get_mark(message:types.Message):
    text = f"Assalomu aleykum, {message.from_user.full_name}!\n"
    text += "Bu *qalin shrift markdown usulida*.\n"
    text += "~to'lqin~"
    text += f"[Kun uz sahifasi](https://kun.uz)"

    await message.reply(text, parse_mode=types.ParseMode.MARKDOWN_V2)

@dp.message_handler(commands='info_aiogram')
async def get_aio(message:types.Message):
    text=f"Assalomu aleykum, {message.from_user.full_name}!\n"
    text+="Bu"+hbold('qalin \n.')
    text += "Bu" + hbold('qalin \n.')
    text += "Bu" + hitalic('qalin \n.')
    text += "Bu" + hstrikethrough('qalin \n.')
    text += "Bu" + hunderline('qalin \n.')
    text += "Bu" + hcode("@dp.message_handler(commands='info_aiogram')\n")
    # text += "Bu" + hlink('https://kun.uz')
    await message.reply(text)