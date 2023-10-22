import io
import os
from aiogram import types
from aiogram.dispatcher import FSMContext  # Импорт машины состояний для переключения между стейтами
from aiogram.types import InputFile

from db import get_active_orders_by_telegram_id
from loader import dp, bot
from states.states import Menus
from utils.create_orderpdf import create_pdf


@dp.message_handler(state=Menus.active_orders)
async def process_login(message: types.Message, state: FSMContext):
    user_id = message.chat.id
    login = message.text
    order = get_active_orders_by_telegram_id(user_id)
    pdf_filename = f"{user_id}_orders.pdf"  # Имя файла PDF

    # Создаем PDF-файл
    create_pdf(order, pdf_filename)

    # Отправляем файл пользователю
    with open(pdf_filename, 'rb') as pdf_file:
        await message.answer_document(InputFile(pdf_file, filename=pdf_filename))

    # Удаляем временный PDF-файл
    os.remove(pdf_filename)

    await state.update_data(order=order)
    await Menus.next()