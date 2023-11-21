from aiogram import types

from filters import IsPrivate
from keyboards.inline.language import language_keyboard

from loader import dp, bot

@dp.message_handler(IsPrivate(),text="⚙️ Язык" )
@dp.message_handler(IsPrivate(),text="⚙️ Language" )
@dp.message_handler(IsPrivate(),text="⚙️ Tilni o'zgartirish" )
async def bot_start(message: types.Message):
    # await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer(f"Choose language: ", reply_markup=language_keyboard)