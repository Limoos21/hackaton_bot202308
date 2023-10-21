from keyboard.user_main import user_main
from loader import dp, bot
from states.states import Menus
from aiogram import types
from aiogram.dispatcher import FSMContext  # Импорт машины состояний для переключения между стейтами
from aiogram.dispatcher.filters import Text  # Импорт фильтра - Текст
from aiogram.types import Message  # Импорт типа - Сообщение



@dp.message_handler(state=Menus.voice)
async def process_voice(message: types.Message, state: FSMContext):

    API_TOKEN = '6575862659:AAFowh2C62RngDPLutCQWLpwX-EymgEYEeY'


    voice = message.voice
    file_id = voice.file_id

    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path

    voice_url = f'https://api.telegram.org/file/bot{API_TOKEN}/{file_path}'

    # Сохраняем логин в состояние
    await state.update_data(voice=voice)
    await message.answer(text='Записал')
    # await message.answer(voice_url)
    await state.finish()

