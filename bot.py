import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8595343013:AAFedo4JKC_GP17bsjFVRFqUCgvfvLqy-t8"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 🎤\n"
        "Хит в дар на связи!\n\n"
        "Бот полностью запущен и готов к работе.\n"
        "Напиши любой текст — отвечу эхом."
    )

@dp.message()
async def echo(message: Message):
    await message.answer(message.text)

async def main():
    print("Бот запущен и работает!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
