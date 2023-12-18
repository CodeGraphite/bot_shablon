from loader import dp, db, bot
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import types

from keyboards.inline.menu import *
from keyboards.inline.admin_menu import *


from data.config import ADMINS




@dp.callback_query_handler(text = 'button_1')
async def send_welcome(call: types.CallbackQuery, state:FSMContext):
    await call.message.answer("Button-1 bosildi")
    await call.message.delete()

@dp.callback_query_handler(text = 'button_2')
async def send_welcome(call: types.CallbackQuery, state:FSMContext):
    await call.message.answer("Button-2 bosildi")
    await call.message.delete()