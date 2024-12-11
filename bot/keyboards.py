import aiohttp
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import requests
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()
API_URL = "http://api:8000"


# Команда /start
@router.message(CommandStart())
async def start_and_auth(message: Message):
    data = {
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'tg_id': int(message.from_user.id)
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{API_URL}/auth", json=data) as response:
            if response.status == 200:
                result = await response.json()
                await message.reply("Вы успешно зарегистрированы.")
            else:
                await message.reply("Ошибка регистрации")
    # await message.reply("Привет! Нажми на кнопку ниже:", reply_markup=get_inline_keyboard())
    await message.reply("Привет! Нажми на кнопку ниже:", reply_markup=main)


# Команда /auth для авторизации
@router.message(Command('auth'))
async def auth_user(message: Message):
    try:
        _, first_name, last_name, tg_id = message.text.split()
    except ValueError:
        await message.reply("Please send /auth <firstName> <lastName> <tgId>")
        return
    data = {
        "firstName": first_name,
        "lastName": last_name,
        "id": int(tg_id)
    }
    response = requests.post(f"{API_URL}/auth", json=data)
    if response.status_code == 200:
        user_data = response.json()
        await message.reply(
            f"Authorized successfully! Your TON Wallet: {user_data['tonWallet']['address']} with balance: {user_data['tonWallet']['balance']}")
    else:
        await message.reply("Authorization failed")


# Команда /wallet для подключения кошелька
@router.message(Command('wallet'))
async def connect_wallet(message: Message):
    try:
        _, address = message.text.split()
    except ValueError:
        await message.reply("Please send /wallet <address>")
        return

    data = {
        "address": address
    }

    response = requests.post(f"{API_URL}/wallet", json=data)
    if response.status_code == 200:
        await message.reply("Wallet connected successfully!")
    else:
        await message.reply("Failed to connect wallet")


# Команда /deal для открытия/закрытия сделки
@router.message(Command('deal'))
async def manage_deal(message: Message):
    try:
        _, deal_id, deal_type, currency, deal_sum, stop_loss, take_profit, cross = message.text.split()
    except ValueError:
        await message.reply("Please send /deal <id> <type> <currency> <sum> <stopLoss> <takeProfit> <cross>")
        return

    data = {
        "id": deal_id,
        "type": deal_type,
        "currency": currency,
        "sum": float(deal_sum),
        "stopLoss": float(stop_loss),
        "takeProfit": float(take_profit),
        "cross": cross.lower() in ["true", "1", "yes"]
    }

    response = requests.post(f"{API_URL}/deal", json=data)
    if response.status_code == 200:
        await message.reply("Deal processed successfully!")
    else:
        await message.reply("Failed to process deal")


# Команда /transfer для перевода средств
@router.message(Command('transfer'))
async def transfer_funds(message: Message):
    try:
        _, wallet_address, network, amount = message.text.split()
    except ValueError:
        await message.reply("Please send /transfer <walletAddress> <network> <amount>")
        return

    data = {
        "walletAddress": wallet_address,
        "network": network,
        "amount": float(amount)
    }

    response = requests.post(f"{API_URL}/transfer", json=data)
    if response.status_code == 200:
        await message.reply("Transfer successful!")
    else:
        await message.reply("Failed to transfer funds")




@router.callback_query(lambda c: c.data in ['players_list', 'friends_list'])
async def process_callback(callback_query: CallbackQuery):
    code = callback_query.data
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}/user-tg-id", params={'tg_id': callback_query.from_user.id}) as response:
            if response.status == 200:
                user = await response.json()

                endpoint = "players" if code == "players_list" else "friends"
                async with session.get(f"{API_URL}/players",
                                       params={"type": endpoint, 'user_id': user['id']}) as response:
                    if response.status == 200:
                        result = await response.json()
                        message = f"Список {endpoint}:\n"
                        for item in result:
                            message += (f"Имя: {item['full_name']}\n"
                                        f"Лига: {item['league']}\n"
                                        f"Монеты: {item['coins']}\n"
                                        f"Друзья: {'Да' if item['is_friend'] else 'Нет'}\n"
                                        "----\n")
                        await callback_query.message.answer(message)
                    else:
                        await callback_query.message.answer(f"Ошибка при получении списка {endpoint}")
            else:
                await callback_query.message.answer("Ошибка при получении данных пользователя")




main = InlineKeyboardMarkup(inline_keyboard=[
    # [InlineKeyboardButton(text='Получить список игроков', callback_data='catalog')],
    [
        InlineKeyboardButton(text='Получить список игроков', callback_data='players_list'),
        InlineKeyboardButton(text='Получить список друзей', callback_data='friends_list'),
        # InlineKeyboardButton(text='Контакты', callback_data='contacts')
    ]
])