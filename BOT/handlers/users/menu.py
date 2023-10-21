from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from db import get_manager_telegram_ids, get_user_telegram_ids
from keyboard.invoice import send_mode
from keyboard.orders import order, send
from keyboard.user_main import user_main
from loader import dp
from keyboard.authorization import authoriz
from states.states import Menus

from utils.outfunc import voice_chat, openai

from aiogram.types import Voice
from aiogram.dispatcher.filters import ContentTypeFilter


@dp.message_handler(Command('start'))
async def show_main_men(message: Message):
    if str(message.chat.id) in get_manager_telegram_ids():
        await message.answer(text="Вы успешно авторизовались как Менеджер")

    elif str(message.chat.id) in get_user_telegram_ids():
        await message.answer(text="Вы уже авторизованы", reply_markup=user_main)

    else:
        await message.answer(text="Для продолжения вам нужно авторизоваться", reply_markup=authoriz)


@dp.message_handler(Text("Авторизоваться"))
async def show_main_menu(message: Message):
    await message.answer(text='Введите ваш номер договора',
                         reply_markup=ReplyKeyboardRemove())
    await Menus.login.set()


@dp.message_handler(Text("Мои заказы"))
async def show_main_menu(message: Message):
    await message.answer(text="Заказы", reply_markup=order)


@dp.message_handler(Text("Создание нового заказа"))
async def show_main_menu(message: Message):
    await message.answer(text="Выбор режима отправки", reply_markup=send)



@dp.message_handler(Text("Отправить голосовое сообщение"))
async def show_main_menu(message: Message):
    await message.answer(text="Запиши голосовое")
    await Menus.voice.set()



@dp.message_handler(Text("Заполнить текстовую форму"))
async def show_main_menu(message: Message):
    await message.answer(text="Как отправить?", reply_markup=send_mode)
    await Menus.send_mode.set()

