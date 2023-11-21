from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, Command

from filters.private_filter import IsPrivate
from keyboards.inline.new_post import config_keyboard, post_callback
from states.admin_commands import AddPhoto, Reklama
from aiogram.dispatcher import FSMContext
import asyncio
from data.config import ADMINS
from filters.admin_filter import AdminFilter
from keyboards.default.menu_sevrices import menu_services_uz
from loader import dp, db, bot


@dp.message_handler(CommandHelp(), chat_id=ADMINS[0])
async def bot_help_admin(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/allusers - Botdagi foydalanuvchilar soni",
            "/reklama - Botdagi foydalanuvchilarga reklama yuborish",
            "/help - Yordam")

    await message.answer("\n".join(text))


@dp.message_handler(IsPrivate(),Command("allusers"), user_id=ADMINS)
async def countUsers(message: types.Message):
    count = db.count_users()[0]
    await message.answer(f"Botdagi foydalanuvchilar soni {count} ta.")


@dp.message_handler(IsPrivate(), text="/reklama", user_id=ADMINS[0])
async def getReklama(message: types.Message):
    await message.answer("Reklama yuboring")
    await Reklama.reklama.set()


# photo reklama uchun
@dp.message_handler(content_types=types.ContentType.PHOTO, state=Reklama.reklama)
async def reklama_photo(message: types.Message, state: FSMContext):
    global PHOTO_ID
    PHOTO_ID = message.photo[-1].file_id
    await message.answer("Rasm osti matnini kiriting!")
    await Reklama.photo_reklama_text.set()


@dp.message_handler(state=Reklama.photo_reklama_text)
async def check_photoReklama(message: types.Message):
    global MESSAGE
    MESSAGE = str(message.text)
    await message.answer_photo(PHOTO_ID, caption=MESSAGE)
    await message.answer("Reklamani foydalanuvchilarga yuborasizmi?", reply_markup=config_keyboard)
    await Reklama.photo_config.set()

# video reklama uchun
@dp.message_handler(content_types=types.ContentType.VIDEO, state=Reklama.reklama)
async def reklama_video(message: types.Message, state: FSMContext):
    global VIDEO_ID
    VIDEO_ID = message.video.file_id
    await message.answer("Video osti matnini kiriting!")
    await Reklama.video_reklama_text.set()


@dp.message_handler(state=Reklama.video_reklama_text)
async def check_videoReklama(message: types.Message):
    global MESSAGE
    MESSAGE = str(message.text)
    await message.answer_video(VIDEO_ID, caption=MESSAGE)
    await message.answer("Reklamani foydalanuvchilarga yuborasizmi?", reply_markup=config_keyboard)
    await Reklama.video_config.set()

# text reklama uchun
@dp.message_handler(content_types=types.ContentType.TEXT, state=Reklama.reklama)
async def reklama_text(message: types.Message, state: FSMContext):
    global MESSAGE_TEXT
    MESSAGE_TEXT = str(message.text)
    await message.answer(MESSAGE_TEXT)
    await message.answer("reklamani foydalanuvchilarga yuboraymi?", reply_markup=config_keyboard)
    await Reklama.config.set()


@dp.callback_query_handler(post_callback.filter(action="post"), state=Reklama.config)
async def configReklama(call: types.CallbackQuery, state: FSMContext):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text=MESSAGE_TEXT)
        await asyncio.sleep(0.05)

    count = db.count_users()[0]
    await bot.send_message(chat_id=ADMINS[0], text=f"Reklama (text) {count} ta foydalanuvchiga yuborildi")
    await state.finish()


@dp.callback_query_handler(post_callback.filter(action="cancel"), state=Reklama.config)
async def configPost(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(chat_id=ADMINS[0], text="Reklama bekor qilindi!")
    await state.finish()


@dp.callback_query_handler(post_callback.filter(action="post"), state=Reklama.photo_config)
async def config_photoReklama(call: types.CallbackQuery, state: FSMContext):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_photo(chat_id=user_id, photo=PHOTO_ID, caption=MESSAGE)
        await asyncio.sleep(0.05)

    count = db.count_users()[0]
    await bot.send_message(chat_id=ADMINS[0], text=f"Reklama (photo) {count} ta foydalanuvchiga yuborildi")
    await state.finish()


@dp.callback_query_handler(post_callback.filter(action="cancel"), state=Reklama.photo_config)
async def config_photoPost(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(chat_id=ADMINS[0], text="Reklama bekor qilindi!")
    await state.finish()


@dp.callback_query_handler(post_callback.filter(action="post"), state=Reklama.video_config)
async def config_videoReklama(call: types.CallbackQuery, state: FSMContext):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_video(chat_id=user_id, video=VIDEO_ID, caption=MESSAGE)
        await asyncio.sleep(0.05)

    count = db.count_users()[0]
    await bot.send_message(chat_id=ADMINS[0], text=f"Reklama (video) {count} ta foydalanuvchiga yuborildi")
    await state.finish()


@dp.callback_query_handler(post_callback.filter(action="cancel"), state=Reklama.video_config)
async def config_videoPost(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(chat_id=ADMINS[0], text="Reklama bekor qilindi!")
    await state.finish()
