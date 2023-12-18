from loader import dp, db, bot
from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS, CHANNEL_USERNAME
from keyboards.inline.admin_menu import *
from keyboards.inline.menu import *




@dp.message_handler(commands=['admin'], state='*', user_id = ADMINS)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer("Admin menu:", reply_markup= await main_menu_admin_btns())
    await state.finish()
    await state.reset_data()









