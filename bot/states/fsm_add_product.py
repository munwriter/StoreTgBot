from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMAdminAddProduct(StatesGroup):
    name = State()
    description = State()
    photo = State()
    price = State()