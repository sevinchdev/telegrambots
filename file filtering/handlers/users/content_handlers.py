from loader import dp, bot
from aiogram.types import ContentType, Message
from pathlib import Path


download_path=Path().joinpath("downloads","categories")
download_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler()
async def text_handler(message:Message):
    await message.reply("Siz matn yubordingiz!")

# @dp.message_handler(content_types='document')
@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handler(message:Message):
    await message.document.download(destination=download_path)
    doc_id=message.document.file_id
    await message.reply(f"Siz hujjat yubordingiz.\nfile_id={doc_id}")

@dp.message_handler(content_types='video')
# @dp.message_handler(content_types=ContentType.VIDEO)
async def video_handler(message:Message):
    await message.video.download(destination=download_path)
    await message.reply(f"Siz video yubordingiz.\nfile_id={message.video.file_id}")

# @dp.message_handler(content_types='photo')
@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_handler(message:Message):
    await message.photo[-1].download(destination=download_path)
    await message.reply(f"Siz rasm yubordingiz.\nfile_id={message.photo[1].file_id}")


@dp.message_handler(content_types=ContentType.ANY)
async def any_handler(message:Message):
    await message.reply(f"{message.content_type} qabul qilindi.")


@dp.message_handler(content_types=ContentType.LOCATION)
async def location_handler(message:Message):
    await message.reply(f"{message.location} qabul qilindi")

@dp.message_handler(content_types=ContentType.CONTACT)
async def contact_handler(message:Message):
    await message.reply(f"{message.contact} qabul qilindi.")