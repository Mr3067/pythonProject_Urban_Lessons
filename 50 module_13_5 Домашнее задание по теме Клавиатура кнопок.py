"""
версия: aiogram 3.11.0

учебный бот: https://t.me/module_13_3_bot

"""

from Data_Bot import api_module_13_5 as api
import asyncio
from aiogram import F, Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.types.message import Message
from aiogram.types import (KeyboardButton, InlineKeyboardButton,
                           ReplyKeyboardMarkup, InlineKeyboardMarkup)
from aiogram.fsm.context import FSMContext

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()
    begin = State()


def two_butt_kb(name1, name2: str):
    button = [[KeyboardButton(text=f'{name1}'), KeyboardButton(text=f'{name2}')]]
    return ReplyKeyboardMarkup(keyboard=button,
                               resize_keyboard=True,
                               one_time_keyboard=True)


@dp.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.',
                         reply_markup=two_butt_kb("Рассчитать", "Информация."))

@dp.message(F.text == "Рассчитать")
async def msg_Calories(message: Message, state: FSMContext):
    await  bot.send_message(message.chat.id,
                            text=f'Введите свой возраст:')
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
    await state.update_data(weight=message.text)
    data = await state.get_data()
    summery_m = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) + 5
    summery_w = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) - 161
    if data['sex'] == 1:
        await bot.send_message(message.chat.id,
                               text=f'Для мужчины норма калорий {summery_m}')
    elif data['sex'] == 2:
        await bot.send_message(message.chat.id,
                               text=f'Для женщины норма калорий {summery_w}')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
