import types

from aiogram.types import Message

from filters import IsPrivate
from keyboards.default.menu_sevrices import menu_services_eng, menu_services_ru,menu_services_uz
from loader import dp


@dp.message_handler(IsPrivate(), text="📙 Services")
async def services_info(message: Message):
    await message.answer(text = "All services",reply_markup=menu_services_eng)

@dp.message_handler(IsPrivate(), text="📙 Xizmatlar")
async def services_info(message: Message):
    await message.answer(text="Barcha xizmatlar",reply_markup=menu_services_uz)

@dp.message_handler(IsPrivate(), text="📙 Услуги")
async def services_info(message: Message):
    await message.answer(text="Все услуги",reply_markup=menu_services_ru)


