from aiogram import executor                                            # Импорт экзекутора для начала работы бота

from loader import dp                                                   # Импорт диспатчера
import handlers                                                         # Импорт хендлеров. (Так как у нас всё прописано в __init__.py мы и можем импортировать таким образом) import handlers
from utils.notify_admins import on_startup_notify, on_shutdown_notify   # Импорт функций для оповещения админов
from utils.bot_commands import set_default_commands                 # Импорт функции устанавливающей команды


async def on_startup(dispatcher):           # Функция отвечающая за выполнение действий, которые должны быть выполнены сразу же при запуске бота
    # Устанавливаем дефолтные команды         А именно установка команд
    await set_default_commands(dispatcher)

    # Уведомляет про запуск                   И уведомление о запуске
    await on_startup_notify(dispatcher)


if __name__ == '__main__':  # Конструкция чтобы бота можно было запустить только из этого файла. Делается чтобы избежать больших ошибок
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown_notify)   # Указываются функции выполняемые на запуске и на остановке