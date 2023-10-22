from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types.reply_keyboard import ReplyKeyboardRemove

from db import add_invoice
from keyboard.invoice import send_mode
from keyboard.pyment import pyment
from keyboard.yes_no import yes_no
from loader import dp, bot
from states.states import Menus


@dp.message_handler(state=Menus.send_mode)
async def process_send_mode(message: types.Message, state: FSMContext):
    send_mode = message.text

    # Сохраняем в состояние
    await state.update_data(send_mode=send_mode)

    # Переходим к следующему полю - количество мест
    await message.answer("Введите количество мест:", reply_markup=ReplyKeyboardRemove())
    await Menus.count.set()


@dp.message_handler(state=Menus.count)
async def process_count(message: types.Message, state: FSMContext):
    count = message.text
    await state.update_data(count=count)

    await message.answer("Введите описание вложений:")
    await Menus.desc.set()


@dp.message_handler(state=Menus.desc)
async def process_desc(message: types.Message, state: FSMContext):
    desc = message.text
    await state.update_data(desc=desc)

    await message.answer("Введите габариты каждого вложения в см (дл-шр-выс):")
    await Menus.dimensions.set()


@dp.message_handler(state=Menus.dimensions)
async def process_dimensions(message: types.Message, state: FSMContext):
    dimensions = message.text
    await state.update_data(dimensions=dimensions)

    await message.answer("Введите вес каждого места в кг:")
    await Menus.weight.set()


@dp.message_handler(state=Menus.weight)
async def process_weight(message: types.Message, state: FSMContext):
    weight = message.text
    await state.update_data(weight=weight)

    await message.answer("Введите стоимость вложения (общая/по местам):")
    await Menus.price.set()


@dp.message_handler(state=Menus.price)
async def process_price(message: types.Message, state: FSMContext):
    price = message.text
    await state.update_data(price=price)

    await message.answer("Введите точный адрес доставки и отправки:")
    await Menus.address.set()


@dp.message_handler(state=Menus.address)
async def process_address(message: types.Message, state: FSMContext):
    address = message.text
    await state.update_data(address=address)

    # Предлагаем выбрать ПВЗ или указать адрес
    await message.answer("Выберите ПВЗ или укажите адрес:",
                         reply_markup=types.ReplyKeyboardMarkup(
                             resize_keyboard=True,
                             one_time_keyboard=True,
                             keyboard=[
                                 [types.KeyboardButton("Выбрать ПВЗ"), types.KeyboardButton("Указать адрес")]
                             ]
                         ))

    await Menus.pvz.set()

@dp.message_handler(state=Menus.pvz)
async def process_payment(message: types.Message, state: FSMContext):
    pvz = message.text
    await state.update_data(pvz=pvz)
    await message.answer("Выберите способ оплаты", reply_markup= pyment)
    await Menus.payment.set()




@dp.message_handler(state=Menus.payment)
async def process_payment(message: types.Message, state: FSMContext):
    payment = message.text
    await state.update_data(payment=payment)

    # Получаем все данные из состояния
    data = await state.get_data()

    # Отправляем итоговую информацию пользователю
    await message.answer("Спасибо! Вот ваша информация. Отправить?\n\n"
                         f"Режим отправки: {data['send_mode']}\n"
                         f"Количество мест: {data['count']}\n"
                         f"Описание вложений: {data['desc']}\n"
                         f"Габариты вложений: {data['dimensions']}\n"
                         f"Вес каждого места: {data['weight']}\n"
                         f"Стоимость вложения: {data['price']}\n"
                         f"Точный адрес доставки и отправки: {data['address']}\n"
                         f"Способ оплаты: {data['payment']}", reply_markup=yes_no)

    # Завершаем сбор информации
    await Menus.confirm.set()


@dp.message_handler(state=Menus.confirm)
async def process_confirm(message: types.Message, state: FSMContext):
    confirm = message.text.lower()
    data = await state.get_data()
    telegram_id=message.chat.id
    if confirm == 'да':
        content = (
            f"Режим отправки: {data['send_mode']}\n"
            f"Количество мест: {data['count']}\n"
            f"Описание вложений: {data['desc']}\n"
            f"Габариты вложений: {data['dimensions']}\n"
            f"Вес каждого места: {data['weight']}\n"
            f"Стоимость вложения: {data['price']}\n"
            f"Точный адрес доставки и отправки: {data['address']}\n"
            f"Способ оплаты: {data['payment']}"
        )
        await message.answer("Спасибо! Ваш заказ принят.", reply_markup=ReplyKeyboardRemove())
        add_invoice(telegram_id, content)
        await state.finish()

    elif confirm == 'нет':
        await message.answer("Хорошо, начнем заново.Как отправить?", reply_markup=send_mode)
        await state.reset_state(with_data=True)
        await Menus.send_mode.set()
    else:
        await message.answer("Пожалуйста, введите 'да' или 'нет'.")
    await state.finish()