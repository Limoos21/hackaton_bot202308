
from loader import dp, bot
from states.states import Menus
from aiogram import types
from aiogram.dispatcher import FSMContext
from utils.outfunc import voice_chat, openai


@dp.message_handler(state=Menus.voice, content_types=types.ContentType.VOICE)
async def process_voice(message: types.Message, state: FSMContext):
    # Сохраняем информацию о голосовом сообщении
    voice_file_id = message.voice.file_id

    # Загружаем аудиофайл с помощью bot.get_file
    file = await bot.get_file(voice_file_id)
    file_path = file.file_path

    # Загружаем содержимое файла в память
    voice_mess_bytes = await bot.download_file(file_path)

    # Задаем путь, куда хотим сохранить файл
    save_path = "voice/voice.ogg"

    # Открываем файл в режиме записи байтов и записываем в него скачанные данные
    with open(save_path, "wb") as file:
        file.write(voice_mess_bytes)
    save_path = "voice/voice.ogg"
    # Теперь можно использовать save_path для обращения к этому файлу
    voice_text = await voice_chat(save_path)
    result = await openai(voice_text)

    await message.answer(text="записал")
    print(result)

    await state.finish()
