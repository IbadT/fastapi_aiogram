from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import keyboards as kb
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.fsm.context import FSMContext
# from app.middlewares import TestMiddleware
# import app.database.requests as rq
from aiogram.types import Message
from keyboards import main

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    # await rq.set_user(message.from_user.id)
    await message.answer("Привет я телеграм-бот")
    await message.answer('Добро пожаловать', reply_markup=main)
    # await message.answer('Добро пожаловать', reply_markup=kb.main)