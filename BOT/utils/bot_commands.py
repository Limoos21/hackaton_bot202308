from aiogram import types                                   # Импорт всех типов из aiogram


async def set_default_commands(dp):                         # Определение функции для установки команд
    await dp.bot.set_my_commands(                           # Выполнение установки команд
        [
            types.BotCommand("start", "Запустить бота")   # Передача команд и их описания
            # types.BotCommand("menu", "выбрать функцию"),
            # types.BotCommand("stop", "остановить бота")
        ]
    )