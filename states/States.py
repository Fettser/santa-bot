from aiogram.dispatcher.filters.state import StatesGroup, State


class Interview(StatesGroup):
    Q1 = State()


class Admin(StatesGroup):
    A1 = State()
