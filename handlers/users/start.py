import sqlite3
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from data.config import ADMINS
from filters.private_filter import IsPrivate
from keyboards.default.menu import menu_uz, menu_eng, menu_ru
from keyboards.inline.language import language_keyboard, lan_callback
from loader import dp, bot, db



@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        pass

    await message.answer("Choose language: ", reply_markup=language_keyboard)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)


@dp.callback_query_handler(lan_callback.filter(action="eng"))
async def select_lan(call: CallbackQuery, state: FSMContext):
    await call.answer("eng")
    await bot.send_message(call.from_user.id,text = "Select the desired button!",reply_markup=menu_eng)


    # await Language.Eng.set()


@dp.callback_query_handler(lan_callback.filter(action="uz"))
async def select_lan(call: CallbackQuery, state: FSMContext):
    await call.answer("uz")
    await bot.send_message(call.from_user.id,text = "Kerakli tugmani tanlang!",reply_markup=menu_uz)
    # await Language.Uz.set()

@dp.callback_query_handler(lan_callback.filter(action="ru"))
async def select_lan(call: CallbackQuery, state: FSMContext):
    await call.answer("ru")
    await bot.send_message(call.from_user.id,text = "Выберите нужную кнопку!",reply_markup=menu_ru)
    # await Language.Ru.set()


