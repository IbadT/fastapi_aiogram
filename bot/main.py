# import logging
# from aiogram import Bot, Dispatcher
# import os
# # from configs.settings import TG_BOT_TOKEN
# import asyncio
# from dotenv import load_dotenv
# from handlers import router
#
# logging.basicConfig(level=logging.INFO)
#
# load_dotenv()
#
# async def main():
#     dp = Dispatcher()
#     # bot=Bot(token=TG_BOT_TOKEN)
#     bot=Bot(token=os.getenv('TG_BOT_TOKEN'))
#     dp.include_router(router)
#     await dp.start_polling(bot)
#
#
# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO)
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         print("Exit")
#




################################

import logging
import asyncio
from aiogram import Bot, Dispatcher
from keyboards import router
# from api.schemas.database import async_main

logging.basicConfig(level=logging.INFO)

API_TOKEN = '7429091412:AAGkI-u_td59r4CLrrc4jQf3SY2iBPJ5oOQ'

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
