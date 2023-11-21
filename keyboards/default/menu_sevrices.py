from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_services_uz = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="🪟 Deraza uchun lepkalar"),
            KeyboardButton(text="🚪 Eshik uchun lepkalar"),
        ],
        [
            KeyboardButton(text="⛩ Darvoza uchun lepkalar"),
            KeyboardButton(text="🌠 Patalok uchun lepkalar"),
        ],
        [
            KeyboardButton(text="🗽 Ustunlar"),
            KeyboardButton(text="🏠 Tashqi dizayn"),
        ],
        [
            KeyboardButton(text="↩️ Bosh menu"),
        ]

    ], resize_keyboard=True
)

menu_services_eng = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="🪟 Moldings for window"),
            KeyboardButton(text="🚪 Moldings for door"),
        ],
        [
            KeyboardButton(text="⛩ Moldings for gate"),
            KeyboardButton(text="🌠 Moldings for top"),
        ],
        [
            KeyboardButton(text="🗽 Columns"),
            KeyboardButton(text="🏠 Exterior design"),
        ],
        [
            KeyboardButton(text="↩️ Mani menu"),
        ]

    ], resize_keyboard=True
)

menu_services_ru = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="🪟 Лепки для окно"),
            KeyboardButton(text="🚪 Лепки для двери"),
        ],
        [
            KeyboardButton(text="⛩ Лепки для ворота"),
            KeyboardButton(text="🌠 Лепки для паталок"),
        ],
        [
            KeyboardButton(text="🗽 Колонны"),
            KeyboardButton(text="🏠 Внешний дизайн"),
        ],
        [
            KeyboardButton(text="↩️ Главное меню"),
        ]

    ], resize_keyboard=True
)