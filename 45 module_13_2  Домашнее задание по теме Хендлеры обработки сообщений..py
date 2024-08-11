"""
версия aiogram 3.11.0

https://t.me/Marshallmarshallbot

"""

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command
import asyncio
from Data_Bot import api_Marshallmarshallbot as Api

bot = Bot(token=Api)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command('start'))
async def comm_start(message: types.Message):
    await bot.send_message(message.chat.id,
                           f'Привет! Я бот помогающий твоему здоровью.')


@dp.message()
async def all_msg(message:types.Message):
    await bot.send_message(message.chat.id,
                           f'Введите команду /start, чтобы начать общение.')

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

