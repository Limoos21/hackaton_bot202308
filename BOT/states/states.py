from aiogram.dispatcher.filters.state import StatesGroup, State


class Menus(StatesGroup):
    login = State()
    password = State()
    send_mode = State()
    count = State()
    desc = State()
    dimensions = State()
    weight = State()
    price = State()
    choose_pvz = State()
    address = State()
    pvz = State()
    payment = State()

    voice = State()
    active_orders = State()
    confirm = State()