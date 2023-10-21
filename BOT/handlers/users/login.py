from aiogram import types
from aiogram.dispatcher import FSMContext  # Импорт машины состояний для переключения между стейтами
from aiogram.dispatcher.filters import Text  # Импорт фильтра - Текст
from aiogram.types import Message  # Импорт типа - Сообщение

from db import check_manager_credentials, check_user_credentials, update_user_telegram_id, update_manager_telegram_id
from keyboard.user_main import user_main
from loader import dp, bot
from states.states import Menus


@dp.message_handler(state=Menus.login)
async def process_login(message: types.Message, state: FSMContext):
    user_id = message.chat.id
    login = message.text

    # Сохраняем логин в состояние
    await state.update_data(login=login)

    # Отправляем запрос на ввод пароля
    await message.answer("Введите пароль:")
    await Menus.next()  # Переходим к следующему состоянию


@dp.message_handler(state=Menus.password)
async def process_password(message: types.Message, state: FSMContext):
    password = message.text

    # Получаем логин из состояния
    data = await state.get_data()
    login = data.get("login")

    if update_manager_telegram_id(login, password, telegram_id=message.chat.id):
        await message.answer("Вы успешно авторизировались как менеджер")

    elif update_user_telegram_id(login, password, telegram_id=message.chat.id):
        await message.answer("Вы успешно авторизировались", reply_markup=user_main)

    else:
        await message.answer("Авторизация не удалась!")

    # Закрываем состояние
    await state.finish()

