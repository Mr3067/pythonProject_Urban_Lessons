"""
версия: aiogram 3.11.0

учебный бот: https://t.me/module_13_3_bot

"""
from Data_Bot import api_module_13_3_bot as api
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command('start'))
async def comm_start(message: types.Message):
    await message.reply(text=f'{message.chat.full_name}')
    await bot.send_message(message.chat.id,
                           text=f'Привет! Я бот помогающий твоему здоровью.\n'
                                f'Я реагирую на /start, /d, Привет! и Пока!')

@dp.message(Command('d'))
async def dice(message: types.Message):
    data = await bot.send_dice(message.chat.id, emoji='🎲')
    await asyncio.sleep(2)
    await bot.send_message(message.chat.id,
                           f'{message.chat.full_name}! У тебя выпало число {data.dice.value}!')



@dp.message()
async def msg_all(message:types.Message):
    if message.text in ['Привет!', 'Пока!']:
        await message.reply(text=message.chat.full_name + "! " + (message.text + " ")*3)
    else:
        await message.reply(text=f'{message.chat.full_name}')
        await bot.send_message(message.chat.id,
                               f'Введите команду /start, чтобы начать общение.\nВведите команду /d покидать кубик.')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
