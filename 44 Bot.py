"""
https://mastergroosha.github.io/aiogram-3-guide/quickstart/
https://habr.com/ru/companies/amvera/articles/820527/
https://habr.com/ru/articles/819955/

"""

# from handlers.start import start_router
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command
import asyncio
from Data_Bot import api_SmlKonBot as Api

bot = Bot(token=Api)
dp = Dispatcher(storage=MemoryStorage())


# dp['iii'] = 187 #Создается переменная в боте

# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Галя - Солнышко!!")

# @dp.message(Command("start"))
# async def cmd_dice(message: types.Message, bot: Bot, iii:int):
#     print(iii)
#     await bot.send_dice(390029612, emoji="🎲")

# @dp.message(Command("dice"))
# async def cmd_dice(message: types.Message):
#     await message.answer_dice(emoji="🎲")


# @dp.message()
# async def react_text(message):
#     if message.text == 'gg':
#         print('GG')
#     elif message.text == 'kk':
#         print("KK")
#     else:
#         print(f"{message.text}")
# @dp.message(Command("run"))
# async def com_run(message: types.Message):
#     print(message.text)
#     await message.answer('asdsdfdsf')
#     value = await message.answer_dice(emoji='🎲')
#     await message.answer(f'{value.dice.value}')


@dp.message(Command('start'))
async def dice(message: types.Message):
    data = await bot.send_dice(message.chat.id, emoji='🎲')
    await asyncio.sleep(5)
    await bot.send_message(message.chat.id,
                           f'Галочка!! Ты победила! У тебя выпало число {data.dice.value}!')



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
