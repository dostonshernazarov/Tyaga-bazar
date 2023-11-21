from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

lan_callback = CallbackData("language", "action")

language_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🇺🇿 UZ", callback_data=lan_callback.new(action="uz")),
        InlineKeyboardButton(text="🇺🇸 ENG", callback_data=lan_callback.new(action="eng")),
        InlineKeyboardButton(text="🇷🇺 RU", callback_data=lan_callback.new(action="ru"))
    ]]
)