import logging
import asyncio
from aiogram import Bot, Dispatcher
from keyboards import router

logging.basicConfig(level=logging.INFO)

API_TOKEN = '7429091412:AAGkI-u_td59r4CLrrc4jQf3SY2iBPJ5oOQ'
# API_TOKEN = '7883399772:AAF4ybEwlA6KAkYQbS_G78QDz4OZ3MsLsF0'

async def main():
    # await async_main()
    bot=Bot(token=API_TOKEN)
    dp = Dispatcher() # является основным роутером - его задача обрабатывать входящие обновления
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
