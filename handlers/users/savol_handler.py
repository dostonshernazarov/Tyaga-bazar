from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from filters.private_filter import IsPrivate
from loader import dp, bot
from states.savol import FikrData


# global fikr
# global number

@dp.message_handler(IsPrivate(), text="❓ Savol yo'llash")
async def savol_uz(message: Message):
    await message.answer("Savol yoki shikoyatingizni yozing", )
    await FikrData.fikr_uz.set()


@dp.message_handler(state=FikrData.fikr_uz)
async def fikr_uz(message: Message):
    global fikrUz
    fikrUz = str(message.text)
    await message.answer("Telefon raqamingizni yuboring: (91-321-44-55)", protect_content=True)
    await FikrData.fikrNum_uz.set()


@dp.message_handler(state=FikrData.fikrNum_uz)
async def fikrNum_uz(message: Message, state: FSMContext):
    global numberUz
    numberUz = str(message.text)
    await message.answer("Rahmat. Savolingiz adminga yetkazildi tez orada sizga aloqaga chiqishadi")
    await state.finish()
    try:
        await bot.send_message(ADMINS[0],
                               f"<b>Savol</b>\nText:{fikrUz}\n\nTel: {numberUz}\nFullname: {message.from_user.full_name}\nUsername: @{message.from_user.username}")
    except:
        await bot.send_message(ADMINS[0],
                               f"<b>Savol</b>\nText:{fikrUz}\n\nTel: {numberUZ}\nFullname: {message.from_user.full_name}")

@dp.message_handler(IsPrivate(), text="❓ Ask a question")
async def savol_en(message: Message):
    await message.answer("Write your question or complaint", )
    await FikrData.fikr_en.set()


@dp.message_handler(state=FikrData.fikr_en)
async def fikr_en(message: Message):
    global fikrEn
    fikrEn = str(message.text)
    await message.answer("Send your phone number: (91-321-44-55)", protect_content=True)
    await FikrData.fikrNum_en.set()


@dp.message_handler(state=FikrData.fikrNum_en)
async def fikrNum_en(message: Message, state: FSMContext):
    global numberEn
    numberEn = str(message.text)
    await message.answer("Thank you. Your question has been forwarded to an admin who will contact you shortly")
    await state.finish()
    try:
        await bot.send_message(ADMINS[0],
                               f"<b>Savol</b>\nText:{fikrEn}\n\nTel: {numberEn}\nFullname: {message.from_user.full_name}\nUsername: @{message.from_user.username}")
    except:
        await bot.send_message(ADMINS[0],
                               f"<b>Savol</b>\nText:{fikrEn}\n\nTel: {numberEn}\nFullname: {message.from_user.full_name}")


@dp.message_handler(IsPrivate(), text="❓ Задайте вопрос")
async def savol_ru(message: Message):
    await message.answer("Напишите свой вопрос или жалобу", )
    await FikrData.fikr_ru.set()


@dp.message_handler(state=FikrData.fikr_ru)
async def fikr_ru(message: Message):
    global fikrRu
    fikrRu = str(message.text)
    await message.answer("Отправьте свой номер телефона: (91-321-44-55)", protect_content=True)
    await FikrData.fikrNum_ru.set()


@dp.message_handler(state=FikrData.fikrNum_ru)
async def fikrNum_ru(message: Message, state: FSMContext):
    global numberRu
    numberRu = str(message.text)
    await message.answer("Спасибо. Ваш вопрос передан администратору, который свяжется с вами в ближайшее время.")
    await state.finish()
    try:
        await bot.send_message(ADMINS[0],
                               f"<b>Savol</b>\nText:{fikrRu}\n\nTel: {numberRu}\nFullname: {message.from_user.full_name}\nUsername: @{message.from_user.username}")
    except:
        await bot.send_message(ADMINS[0],
                               f"<b>Savol</b>\nText:{fikrRu}\n\nTel: {numberRu}\nFullname: {message.from_user.full_name}")

