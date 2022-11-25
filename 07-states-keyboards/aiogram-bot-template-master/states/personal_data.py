from aiogram.dispatcher.filters.state import State, StatesGroup


class PersonalData(StatesGroup):
    full_name = State()
    email = State()
    phone_number = State()
