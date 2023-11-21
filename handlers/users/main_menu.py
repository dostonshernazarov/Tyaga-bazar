from aiogram.types import Message

from filters.private_filter import IsPrivate
from keyboards.default.menu import menu_uz, menu_ru, menu_eng
from loader import dp

@dp.message_handler(IsPrivate(), text="↩️ Bosh menu")
async def set_main_menu(message: Message):
    await message.answer("Bosh menu", reply_markup=menu_uz)

@dp.message_handler(IsPrivate(), text="↩️ Mani menu")
async def set_main_menu(message: Message):
    await message.answer("Mani menu", reply_markup=menu_eng)


@dp.message_handler(IsPrivate(), text="↩️ Главное меню")
async def set_main_menu(message: Message):
    await message.answer("Главное меню", reply_markup=menu_ru)
