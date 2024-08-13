"""
версия: aiogram 3.11.0

учебный бот: https://t.me/module_13_6_bot

"""

from Data_Bot import api_module_13_6 as api
import asyncio

from aiogram import F, Bot, Dispatcher
from aiogram.types import (Message, InlineKeyboardButton, CallbackQuery)
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
    builder_start = InlineKeyboardBuilder()
    builder_start.add(
        InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories"),
        InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
    )
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
        InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
    )
    await callback.message.answer(
        text='Привет! Я бот, помогающий твоему здоровью.',
        reply_markup=builder_start.as_markup()
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
    await state.update_data(weight=message.text)
    data = await state.get_data()
    summery_m = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) + 5
    summery_w = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) - 161
    await bot.send_message(message.chat.id,
                           text=f'Для мужчины норма калорий {summery_m}\n'
                                f'Для женщины норма калорий {summery_w}')


# ____________________________________________________________________
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
