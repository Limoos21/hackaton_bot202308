from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

send_mode = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Дверь-Дверь'),
        KeyboardButton(text="Склад-Склад"),
        KeyboardButton(text ="Склад-Дверь"),
        KeyboardButton(text ="Дверь-Склад")
    ]
], resize_keyboard=True)