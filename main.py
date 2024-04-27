import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router

async def main():
    bot = Bot(token='7040762365:AAGe1cHBecsaUIysk6K2WhMDEL2V2a-Gous')
    dp = Dispatcher()
    dp.include_router((router))
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")