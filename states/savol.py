from aiogram.dispatcher.filters.state import State, StatesGroup


class FikrData(StatesGroup):
    fikr_uz = State()
    fikrNum_uz = State()

    fikr_en = State()
    fikrNum_en = State()

    fikr_ru = State()
    fikrNum_ru = State()