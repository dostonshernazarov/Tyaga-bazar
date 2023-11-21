from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_uz = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="📙 Xizmatlar"),
        ],
        [
            KeyboardButton(text="ℹ️ Biz haqimizda"),
            KeyboardButton(text="❓ Savol yo'llash"),
        ],
        [
            KeyboardButton(text="⚙️ Tilni o'zgartirish"),
        ]

    ], resize_keyboard=True
)

menu_eng = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="📙 Services"),
        ],
        [
            KeyboardButton(text="ℹ️ About us"),
            KeyboardButton(text="❓ Ask a question"),
        ],
        [
            KeyboardButton(text="⚙️ Language"),
        ]

    ], resize_keyboard=True
)

menu_ru = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="📙 Услуги"),
        ],
        [
            KeyboardButton(text="ℹ️ О нас"),
            KeyboardButton(text="❓ Задайте вопрос"),
        ],
        [
            KeyboardButton(text="⚙️ Язык"),
        ]

    ], resize_keyboard=True
)