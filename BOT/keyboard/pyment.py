from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

pyment = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='При получении'),
        KeyboardButton(text="Картой")

    ]
], resize_keyboard=True)