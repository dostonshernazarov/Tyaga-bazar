from aiogram.types import Message, InputFile
from aiogram import types

from filters import IsPrivate
from loader import dp, db

msguz = ("Qo'shimcha ma'lumot uchun quyidagi raqam orqali ma'lumot olishengiz mumkin👇\n\n"
       "Tel: +998 99 282 77 88\nTelegram: @Of_The_Best_77")
msgeng = ("For more information, you can contact the number below👇\n\n"
          "Tel: +998 99 282 77 88\nTelegram: @Of_The_Best_77")
msgru = ("Для получения дополнительной информации вы можете позвонить по номеру ниже👇\n\n"
         "Tel: +998 99 282 77 88\nTelegram: @Of_The_Best_77")

#Kvartira tozalash
@dp.message_handler(IsPrivate(),text="🪟 Deraza uchun lepkalar")
async def show_deraza_uz(message: Message):
    album = types.MediaGroup()
    photo1 =InputFile(path_or_bytesio="Photos/DERAZA/photo1.jpg")
    photo2 =InputFile(path_or_bytesio="Photos/DERAZA/photo2.jpg")
    photo3 =InputFile(path_or_bytesio="Photos/DERAZA/photo3.jpg")
    photo4 =InputFile(path_or_bytesio="Photos/DERAZA/photo4.jpg")
    photo5 =InputFile(path_or_bytesio="Photos/DERAZA/photo5.jpg")
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)
    album.attach_photo(photo=photo4)

    album.attach_photo(photo=photo5, caption=msguz)

    await message.answer_media_group(media=album)

@dp.message_handler(IsPrivate(), text="🪟 Moldings for window")
async def show_deraza_eng(message: Message):

    album = types.MediaGroup()
    photo1 =InputFile(path_or_bytesio="Photos/DERAZA/photo1.jpg")
    photo2 =InputFile(path_or_bytesio="Photos/DERAZA/photo2.jpg")
    photo3 =InputFile(path_or_bytesio="Photos/DERAZA/photo3.jpg")
    photo4 =InputFile(path_or_bytesio="Photos/DERAZA/photo4.jpg")
    photo5 =InputFile(path_or_bytesio="Photos/DERAZA/photo5.jpg")
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)
    album.attach_photo(photo=photo4)

    album.attach_photo(photo=photo5, caption=msgeng)

    await message.answer_media_group(media=album)

@dp.message_handler(IsPrivate(), text="🪟 Лепки для окно")
async def show_deraza_ru(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/DERAZA/photo1.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/DERAZA/photo2.jpg")
    photo3 = InputFile(path_or_bytesio="Photos/DERAZA/photo3.jpg")
    photo4 = InputFile(path_or_bytesio="Photos/DERAZA/photo4.jpg")
    photo5 = InputFile(path_or_bytesio="Photos/DERAZA/photo5.jpg")
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)
    album.attach_photo(photo=photo4)

    album.attach_photo(photo=photo5, caption=msgru)

    await message.answer_media_group(media=album)


@dp.message_handler(IsPrivate(), text="🚪 Eshik uchun lepkalar")
async def buy_home_uz(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/ESHIK/photo_2023-11-20_10-09-44.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/ESHIK/photo_2023-11-20_10-09-45.jpg")
    photo3 = InputFile(path_or_bytesio="Photos/ESHIK/photo_2023-11-20_10-09-45 (2).jpg")
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3, caption=msguz)

    await message.answer_media_group(media=album)

@dp.message_handler(IsPrivate(), text="🚪 Moldings for door")
async def buy_home_eng(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/ESHIK/photo_2023-11-20_10-09-44.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/ESHIK/photo_2023-11-20_10-09-45.jpg")
    photo3 = InputFile(path_or_bytesio="Photos/ESHIK/photo_2023-11-20_10-09-45 (2).jpg")
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3, caption=msgeng)

    await message.answer_media_group(media=album)

@dp.message_handler(IsPrivate(), text="🚪 Лепки для двери")
async def buy_home_ru(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/ESHIK/photo_2023-11-20_10-09-44.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/ESHIK/photo_2023-11-20_10-09-45.jpg")
    photo3 = InputFile(path_or_bytesio="Photos/ESHIK/photo_2023-11-20_10-09-45 (2).jpg")
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3, caption=msgru)

    await message.answer_media_group(media=album)

# Office tozalash
@dp.message_handler(IsPrivate(), text="⛩ Darvoza uchun lepkalar")
async def but_office_uz(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/DARVOZA/photo1.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/DARVOZA/photo2.jpg")
    album.attach_photo(photo=photo1)

    album.attach_photo(photo=photo2, caption=msguz)

    await message.answer_media_group(media=album)

@dp.message_handler(IsPrivate(), text="⛩ Moldings for gate")
async def but_office_eng(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/DARVOZA/photo1.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/DARVOZA/photo2.jpg")
    album.attach_photo(photo=photo1)

    album.attach_photo(photo=photo2, caption=msgeng)

    await message.answer_media_group(media=album)

@dp.message_handler(IsPrivate(), text="⛩ Лепки для ворота")
async def but_office_ru(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/DARVOZA/photo1.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/DARVOZA/photo2.jpg")
    album.attach_photo(photo=photo1)

    album.attach_photo(photo=photo2, caption=msgru)

    await message.answer_media_group(media=album)



@dp.message_handler(IsPrivate(),text="🌠 Patalok uchun lepkalar")
async def buy_garden_uz(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/PATALOK/photo1.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/PATALOK/photo2.jpg")
    photo3 = InputFile(path_or_bytesio="Photos/PATALOK/photo3.jpg")


    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)

    album.attach_photo(photo=photo3, caption=msguz)

    await message.answer_media_group(media=album)

@dp.message_handler(IsPrivate(), text="🌠 Moldings for top")
async def buy_garden_eng(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/PATALOK/photo1.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/PATALOK/photo2.jpg")
    photo3 = InputFile(path_or_bytesio="Photos/PATALOK/photo3.jpg")

    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)

    album.attach_photo(photo=photo3, caption=msgeng)

    await message.answer_media_group(media=album)

@dp.message_handler(IsPrivate(), text="🌠 Лепки для паталок")
async def buy_garden_ru(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/PATALOK/photo1.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/PATALOK/photo2.jpg")
    photo3 = InputFile(path_or_bytesio="Photos/PATALOK/photo3.jpg")

    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)

    album.attach_photo(photo=photo3, caption=msgru)

    await message.answer_media_group(media=album)



@dp.message_handler(IsPrivate(), text="🗽 Ustunlar")
async def buy_green_uz(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/USTUN/photo1.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/USTUN/photo2.jpg")
    photo3 = InputFile(path_or_bytesio="Photos/USTUN/photo3.jpg")
    photo4 = InputFile(path_or_bytesio="Photos/USTUN/photo4.jpg")
    photo5 = InputFile(path_or_bytesio="Photos/USTUN/photo5.jpg")
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)
    album.attach_photo(photo=photo4)

    album.attach_photo(photo=photo5, caption=msguz)

    await message.answer_media_group(media=album)

@dp.message_handler(IsPrivate(), text="🗽 Columns")
async def buy_green_eng(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/USTUN/photo1.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/USTUN/photo2.jpg")
    photo3 = InputFile(path_or_bytesio="Photos/USTUN/photo3.jpg")
    photo4 = InputFile(path_or_bytesio="Photos/USTUN/photo4.jpg")
    photo5 = InputFile(path_or_bytesio="Photos/USTUN/photo5.jpg")
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)
    album.attach_photo(photo=photo4)

    album.attach_photo(photo=photo5, caption=msgeng)

    await message.answer_media_group(media=album)

@dp.message_handler(IsPrivate(), text="🗽 Колонны")
async def buy_green_ru(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/USTUN/photo1.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/USTUN/photo2.jpg")
    photo3 = InputFile(path_or_bytesio="Photos/USTUN/photo3.jpg")
    photo4 = InputFile(path_or_bytesio="Photos/USTUN/photo4.jpg")
    photo5 = InputFile(path_or_bytesio="Photos/USTUN/photo5.jpg")
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)
    album.attach_photo(photo=photo4)

    album.attach_photo(photo=photo5, caption=msgru)

    await message.answer_media_group(media=album)



@dp.message_handler(IsPrivate(), text="🏠 Tashqi dizayn")
async def buy_qurilish_uz(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/TASHQI/photo1.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/TASHQI/photo2.jpg")
    photo3 = InputFile(path_or_bytesio="Photos/TASHQI/photo3.jpg")
    photo4 = InputFile(path_or_bytesio="Photos/TASHQI/photo4.jpg")
    photo5 = InputFile(path_or_bytesio="Photos/TASHQI/photo5.jpg")
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)
    album.attach_photo(photo=photo4)

    album.attach_photo(photo=photo5, caption=msguz)

    await message.answer_media_group(media=album)

@dp.message_handler(IsPrivate(), text="🏠 Exterior design")
async def buy_qurilish_eng(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/TASHQI/photo1.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/TASHQI/photo2.jpg")
    photo3 = InputFile(path_or_bytesio="Photos/TASHQI/photo3.jpg")
    photo4 = InputFile(path_or_bytesio="Photos/TASHQI/photo4.jpg")
    photo5 = InputFile(path_or_bytesio="Photos/TASHQI/photo5.jpg")
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)
    album.attach_photo(photo=photo4)

    album.attach_photo(photo=photo5, caption=msgeng)

    await message.answer_media_group(media=album)

@dp.message_handler(IsPrivate(), text="🏠 Внешний дизайн")
async def buy_qurilish_ru(message: Message):
    album = types.MediaGroup()
    photo1 = InputFile(path_or_bytesio="Photos/TASHQI/photo1.jpg")
    photo2 = InputFile(path_or_bytesio="Photos/TASHQI/photo2.jpg")
    photo3 = InputFile(path_or_bytesio="Photos/TASHQI/photo3.jpg")
    photo4 = InputFile(path_or_bytesio="Photos/TASHQI/photo4.jpg")
    photo5 = InputFile(path_or_bytesio="Photos/TASHQI/photo5.jpg")
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)
    album.attach_photo(photo=photo4)

    album.attach_photo(photo=photo5, caption=msgru)

    await message.answer_media_group(media=album)

