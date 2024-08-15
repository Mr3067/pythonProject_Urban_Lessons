"""
версия: aiogram 3.11.0

учебный бот: https://t.me/module_14_4_bot

"""
from Data_Bot import api_module_14_4 as api
import asyncio, os
import sqlite3
from random import randrange

from aiogram import F, Bot, Dispatcher, Router
from aiogram.types import (Message, InlineKeyboardButton, CallbackQuery, FSInputFile)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

#_______________________________________________________
def initiate_db_products():
    connection_products = sqlite3.connect('database.db')
    cursor_products = connection_products.cursor()
    cursor_products.execute('''
        CREATE TABLE IF NOT EXISTS Products
        (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        price INTEGER NOT NULL,
        pic_name TEXT NOT NULL
        )
        ''')

    if cursor_products.execute('SELECT COUNT(*) FROM Products').fetchone()[0] == 0:
        for i in range(1, 5):
            cursor_products.execute('INSERT INTO Products (title, description, price,pic_name) VALUES (?,?,?,?)',
                                (f'Product{i}', f'Описание Product{i}', f'{i * 100}',
                                 f'Img_module_14_3\\Product{i}.jpg'))

    connection_products.commit()
    connection_products.close()

    connection_users = sqlite3.connect('users.db')
    cursor_users = connection_users.cursor()
    cursor_users.execute('''
        CREATE TABLE IF NOT EXISTS Users
        (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age  INTEGER NOT NULL,
        balance INTEGER NOT NULL,
        block INTEGER NOT NULL
        )
        ''')
    if cursor_users.execute('SELECT COUNT(*) FROM Users').fetchone()[0] == 0:
        for i in range(1, 11):
            cursor_users.execute('INSERT INTO Users (username, email, age, balance, block ) VALUES (?,?,?,?,?)',
                                (f'User{i}', f'User{i}@fb.com', f'{randrange(50)}', 1000, 0))

    connection_users.commit()
    connection_users.close()


def get_all_products():
    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        result = cursor.execute('SELECT * FROM Products')
        return result


def is_included(username):
    with sqlite3.connect('users.db') as connection:
        cursor = connection.cursor()
        result = cursor.execute('SELECT username FROM Users WHERE username == ?', (username,))
        if result.fetchone() != None:
            return True
        else:
            return False

def add_user(username, email, age):
    with sqlite3.connect('users.db') as connection:
        connection= sqlite3.connect('users.db')
        cursor = connection.cursor()
        if is_included(username):
            print('ok')
        else:
            cursor.execute('INSERT INTO Users (username, email, age, balance, block ) VALUES (?,?,?,?,?)',
                           (username, email, age, 1000, 0))
            print('add')
        connection.commit()




#_____________________________________________________________
@dp.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    initiate_db_products()  # Инициализация и заполнение 4 значениями учебной базы данных
    builder_start = InlineKeyboardBuilder()
    builder_start.add(
        InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories"),
        InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas"),
        InlineKeyboardButton(text="Купить", callback_data="buying_4_products"),
        InlineKeyboardButton(text="Регистрация", callback_data="registration")
    )
    builder_start.adjust(2)
    await message.answer(
        text='Привет! Я бот, помогающий твоему здоровью.',
        reply_markup=builder_start.as_markup()
    )


@dp.callback_query(F.data == "main_menu")
async def cmd_start(callback: CallbackQuery):
    builder_start = InlineKeyboardBuilder()
    builder_start.add(
        InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories"),
        InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas"),
        InlineKeyboardButton(text="Купить", callback_data="buying_4_products"),
        InlineKeyboardButton(text="Регистрация", callback_data="registration")
    )
    builder_start.adjust(2)
    await callback.message.answer(
        text='Привет! Я бот, помогающий твоему здоровью.',
        reply_markup=builder_start.as_markup()
    )

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


@dp.callback_query(F.data == "registration")
async def msg_username(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=f'Введите имя пользователя (только латинский алфавит):')
    await state.set_state(RegistrationState.username)

@dp.message(RegistrationState.username)
async def msg_email(message: Message, state: FSMContext):
    if is_included(message.text):
        builder_registration = InlineKeyboardBuilder()
        builder_registration.add(
            InlineKeyboardButton(text="Регистрация", callback_data="registration"),
            InlineKeyboardButton(text="Назад в меню", callback_data="main_menu")
        )
        await message.answer(
            text='Пользователь существует, введите другое имя',
            reply_markup=builder_registration.as_markup()
        )
    else:
        await state.update_data(username=message.text)
        await bot.send_message(message.chat.id,
                               text=f'Введите свой email:')
        await state.set_state(RegistrationState.email)


@dp.message(RegistrationState.email)
async def msg_age(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await bot.send_message(message.chat.id,
                           text=f'Введите свой возраст:')
    await state.set_state(RegistrationState.age)


@dp.message(RegistrationState.age)
async def msg_add_users(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    builder_back = InlineKeyboardBuilder()
    builder_back.add(
        InlineKeyboardButton(text="Назад в меню", callback_data="main_menu")
    )
    await message.answer(
        text='Пользователь добавлен',
        reply_markup=builder_back.as_markup()
    )

# ____________________________________________________________________
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
