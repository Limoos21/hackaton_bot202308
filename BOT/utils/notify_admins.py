import logging                                                  # Импорт для вывода инфы в консоль

from aiogram import Dispatcher                                  # Импорт КЛАССА диспатчера

ADMINS = ["676040650", "454741689", "782014821"]                                 # Импорт списка админов из конфига


async def on_startup_notify(dp: Dispatcher):                    # Уведомление о запуске
    for admin in ADMINS:                                        # Перебор админов
        try:                                                    # Попытка отправить сообщение
            await dp.bot.send_message(admin, "Пошел на... я работаю")     # Отправка сообщения

        except Exception as err:                                # Обработка ошибки
            logging.exception(err)                              # Вывод ошибки, если не получилось отправить сообщение


async def on_shutdown_notify(dp: Dispatcher):                   # Уведомление об отключении
    for admin in ADMINS:                                        # Перебор админов
        try:                                                    # Попытка отправить сообщение
            await dp.bot.send_message(admin, "Все, я упал")  # Отправка сообщения

        except Exception as err:                                # Обработка ошибки
            logging.exception(err)