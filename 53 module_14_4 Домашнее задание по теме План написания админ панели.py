"""
версия: aiogram 3.11.0

учебный бот: https://t.me/module_14_4_bot

"""
from Data_Bot import api_module_14_4 as api
import asyncio, os
import sqlite3

from aiogram import F, Bot, Dispatcher
from aiogram.types import (Message, InlineKeyboardButton, CallbackQuery, FSInputFile)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


class SomeStates(StatesGroup):
    state1 = State()
    state2 = State()
    state3 = State()
    state4 = State()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    initiate_db() #Инициализация и заполнение 4 значениями учебной базы данных
    builder_start = InlineKeyboardBuilder()
    builder_start.add(
        InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories"),
        InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas"),
        InlineKeyboardButton(text="Купить", callback_data="buying_4_products")
    )
    builder_start.adjust(2)
    await message.answer(
        text='Привет! Я бот, помогающий твоему здоровью.',
        reply_markup=builder_start.as_markup()
    )
    await state.set_state(SomeStates.state1)


@dp.callback_query(F.data == "formulas")
async def msg_formulas(callback: CallbackQuery, state: FSMContext):
    builder_back = InlineKeyboardBuilder()
    builder_back.add(
        InlineKeyboardButton(text="Назад в меню", callback_data="main_menu")
    )
    await callback.message.answer(text=f'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n'
                                       f'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161',
                                  reply_markup=builder_back.as_markup()
                                  )


@dp.callback_query(F.data == "main_menu")
async def cmd_start(callback: CallbackQuery):
    builder_start = InlineKeyboardBuilder()
    builder_start.add(
        InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories"),
        InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas"),
        InlineKeyboardButton(text="Купить", callback_data="buying_4_products")
    )
    builder_start.adjust(2)
    await callback.message.answer(
        text='Привет! Я бот, помогающий твоему здоровью.',
        reply_markup=builder_start.as_markup()
    )


@dp.callback_query(F.data == "buying_4_products")
async def buying_4_products(callback: CallbackQuery):
    buyng_4_products = InlineKeyboardBuilder()
    for i in get_all_products():
        buyng_4_products.add(InlineKeyboardButton(text=f'{i[1]}', callback_data='product_buying'))
        photo = FSInputFile(f'{i[4]}')
        await callback.message.answer_photo(
            photo=photo,
            caption=f'||Описание: {i[2]}|| Цена: {i[3]}||'
        )
    buyng_4_products.add(InlineKeyboardButton(text="Назад в меню", callback_data="main_menu"))
    buyng_4_products.adjust(4)
    await callback.message.answer(
        text='Выберите продукт для покупки:',
        reply_markup=buyng_4_products.as_markup()
    )


@dp.callback_query(F.data == 'product_buying')
async def send_confirm_message(callback: CallbackQuery):
    builder_back = InlineKeyboardBuilder()
    builder_back.add(
        InlineKeyboardButton(text="Назад в меню", callback_data="main_menu")
    )
    await callback.message.answer(
        text="Вы успешно приобрели продукт!",
        reply_markup=builder_back.as_markup()
    )


@dp.callback_query(F.data == "calories")
async def msg_Calories(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=f'Введите свой возраст:')
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def msg_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await bot.send_message(message.chat.id,
                           text=f'Введите свой рост:')
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def msg_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await bot.send_message(message.chat.id,
                           text=f'Введите свой вес:')
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def msg_calcul(message: Message, state: FSMContext):
    builder_back = InlineKeyboardBuilder()
    builder_back.add(
        InlineKeyboardButton(text="Назад в меню", callback_data="main_menu")
    )
    await state.update_data(weight=message.text)
    data = await state.get_data()
    summery_m = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) + 5
    summery_w = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) - 161
    await bot.send_message(
        message.chat.id,
        text=f'Для мужчины норма калорий {summery_m}\n'
             f'Для женщины норма калорий {summery_w}',
        reply_markup=builder_back.as_markup()
    )


def initiate_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products
        (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        price INTEGER NOT NULL,
        pic_name TEXT NOT NULL
        )
        ''')
    if cursor.execute('SELECT COUNT(*) FROM Products').fetchone()[0] == 0:
        for i in range(1, 5):
            cursor.execute('INSERT INTO Products (title, description, price,pic_name) VALUES (?,?,?,?)',
                           (f'Product{i}', f'Описание Product{i}', f'{i * 100}', f'Img_module_14_3\\Product{i}.jpg'))

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    result = cursor.execute('SELECT * FROM Products')
    # for i in result:
    #     print(f'id: {i[0]} | title: {i[1]} | description: {i[2]} | price: {i[3]}  | pic_name: {i[4]} ')

    return result
    connection.close()



# ____________________________________________________________________
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    initiate_db()
    asyncio.run(main())
