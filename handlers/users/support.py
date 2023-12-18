from loader import dp
from aiogram import types



@dp.callback_query_handler(text = 'support')
async def send_welcome(call: types.CallbackQuery, state:FSMContext):
    await call.message.answer("Qo'shimcha savol va takliflar uchun: @the_dast")
    await call.message.delete()


