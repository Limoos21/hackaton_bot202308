from aiogram import Bot, Dispatcher, types                              # Импорт КЛАССА бота, КЛАССА диспатчера и типов
from aiogram.contrib.fsm_storage.memory import MemoryStorage            # Импорт класса для работы с памятью, не трогать

                                                # Импорт данных из конфига

bot = Bot(token="6575862659:AAFowh2C62RngDPLutCQWLpwX-EymgEYEeY")      # Создание бота
storage = MemoryStorage()                                               # Создание экземпляра класса памяти
dp = Dispatcher(bot, storage=storage)                                   # Создание диспатчера