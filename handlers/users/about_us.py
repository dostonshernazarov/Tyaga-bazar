from aiogram import types

from filters import IsPrivate
from keyboards.inline.language import language_keyboard

from loader import dp, bot

@dp.message_handler(IsPrivate(),text="ℹ️ Biz haqimizda" )
async def bot_start(message: types.Message):
    # await message.answer(f"Salom, {message.from_user.full_name}!")
    msg = (f"🔔Bizda siz uchun kerak bo'ladigan "
           f"ichki va tashqi devorlar uchun, deraza va eshik uchun va boshqa istalgan turdagi lipkalar mavjud.\n\n "
           f"❗️Malakali ustalar xizmatlari ham mavjud\n\n")

    msg += (f"💯Sifati esa a'lo darajada.\n\n")
    msg += (f"Biz bilan bo'g'lanish: 👇\n\n"
            f"  Tel:+998 99 282 77 88\n"
            f"  Telegram: @Of_The_Best_77")
    await message.answer(msg)

@dp.message_handler(IsPrivate(),text="ℹ️ О нас" )
async def bot_start(message: types.Message):
    msg = (f"🔔У нас есть все виды лепки для внутренних и наружных стен, "
           f"окон и дверей и всего остального, что вам нужно.\n\n"
           f"❗️Также доступны услуги опытных мастеров.\n\n")
    msg += (f"💯Качество отличное.\n\n"
            f"Связаться с нами:👇\n\n"
            f"  Тел:+998 99 282 77 88\n"
            f"  Телеграм: @Of_The_Best_77")
    await message.answer(msg)


@dp.message_handler(IsPrivate(),text="ℹ️ About us")
async def bot_start(message: types.Message):
    msg = (f"🔔We have all kinds of moldings for interior and exterior walls, windows and doors, "
           f"and anything else you need.\n\n"
           f"❗️The services of experienced craftsmen are also available.\n\n")
    msg += (f"💯The quality is excellent.\n\n"
            f"Connect with us:👇\n\n"
            f"  Tel:+998 99 282 77 88\n"
            f"  Telegram: @Of_The_Best_77")
    await message.answer(msg)



