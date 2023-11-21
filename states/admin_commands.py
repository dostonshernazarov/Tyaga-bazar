from aiogram.dispatcher.filters.state import State, StatesGroup


class AddPhoto(StatesGroup):
    services = State()
    get_photo_deraza = State()
    get_photo_eshik = State()
    get_photo_darvoza = State()
    get_photo_patalok = State()
    get_photo_ustun = State()
    get_photo_tashqi = State()


class Reklama(StatesGroup):
    reklama = State()
    photo_reklama_photo = State()
    photo_reklama_text = State()
    video_reklama_video = State()
    video_reklama_text = State()
    video_config = State()
    photo_config = State()
    config = State()