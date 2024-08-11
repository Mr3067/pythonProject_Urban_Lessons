"""
версия aiogram 3.11.0

https://t.me/module_13_4_bot

"""

from Data_Bot import api_module_13_4 as api
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

import asyncio

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await bot.send_message(message.chat.id,
                           text='Привет! Я бот помогающий твоему здоровью.\n'
                                'Для подсчета нормы колорий введи /Calories')


@dp.message(Command('Calories'))
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
    await bot.send_message(message.chat.id,
                           text=f'Для мужчины норма калорий {summery_m}\n'
                                f'Для женщины норма калорий {summery_w}')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
