from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

order = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Архив заказов'),
        KeyboardButton(text="Создание нового заказа"),
        KeyboardButton(text ="Активные заказы")
    ]
], resize_keyboard=True)

send = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Отправить голосовое сообщение'),
        KeyboardButton(text="Заполнить текстовую форму")
    ]
], resize_keyboard=True)


pvz = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Выбор ПВЗ'),
        KeyboardButton(text="Укажу адресс")
    ]
], resize_keyboard=True)

