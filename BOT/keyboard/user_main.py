from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Техническая поддержка'),
        KeyboardButton(text='Мои заказы')
    ]
], resize_keyboard=True)