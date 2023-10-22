from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

yes_no = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='ДА'),
        KeyboardButton(text='НЕТ')
    ]
], resize_keyboard=True)