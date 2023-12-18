from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.menu import *
from loader import dp, db, bot

from data.config import ADMINS

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = db.add_user(message)
    if text:
        for admin in ADMINS:
            await bot.send_message(admin, text)
    await message.answer("Menu:", reply_markup= await main_menubtns())


