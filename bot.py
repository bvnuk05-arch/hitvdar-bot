import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "8595343013:AAFedo4JKC_GP17bsjFVRFqUCgvfvLqy-t8"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Бот ХитВДар запущен на Render!")

@dp.message()
async def echo(message: Message):
    await message.answer(message.text)

async def main():
    print("Бот запущен на Render!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
