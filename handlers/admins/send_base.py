from data.config import ADMINS
from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp

@dp.message_handler(commands=['give_all_user'], state='*', user_id = ADMINS)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer_document(open('data/data_base.db', 'rb'))
    await state.finish()
    await state.reset_data()