import asyncio

from loader import dp, db, bot
from aiogram.dispatcher import FSMContext
from aiogram import types

from keyboards.inline.admin_announce import *
from keyboards.inline.admin_menu import *
from data.config import ADMINS
from states.state import Admin_announce


############### ADMIN ANNOUNCE #############


@dp.callback_query_handler(text= "announce" ,user_id = ADMINS)
async def admin(call: types.CallbackQuery):
    await call.message.answer("E'lon rasmini yuboring: ", reply_markup=types.ReplyKeyboardRemove())
    await call.message.delete()
    await Admin_announce.announce_photo_id.set()
    


@dp.message_handler(content_types='photo',state=Admin_announce.announce_photo_id)
async def admin(message: types.Message, state: FSMContext):
    await state.update_data(announce_photo_id=message.photo[-1].file_id)
    text = """E'lon tekstini yuboring: """
    await message.answer(text)
    await Admin_announce.announce_text.set()

@dp.message_handler(state=Admin_announce.announce_text)
async def admin(message: types.Message, state:FSMContext):
    await state.update_data(announce_text=message.text)
    await message.answer("Knopkani tanlang: ", reply_markup=await generate_admin_menu_announce())
    await Admin_announce.announce_check_state.set()
    

@dp.callback_query_handler(state=Admin_announce.announce_check_state)
async def admin(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if call.data == "no_btn":
        await call.message.answer_photo(photo=data.get('announce_photo_id'), caption=data.get('announce_text'))
        await call.message.delete()
        await call.message.answer("E'lonni tekshiring!!!!", reply_markup=await generate_yes_not_btns2())
        await call.answer()
        await Admin_announce.announce_check2.set()
    elif call.data == "url_btn":
        await call.message.answer('Knopka tekstini yuboring: ')
        await call.message.delete()
        await Admin_announce.announce_btn_text.set()
        


@dp.callback_query_handler(state=Admin_announce.announce_check2)
async def admin(call: types.CallbackQuery, state:FSMContext):
    data = await state.get_data()
    users = db.give_all_users()
    await state.finish()
    if call.data =="yes":
        await call.message.delete()
        await call.message.answer("Yuborilmoqda!!!", reply_markup=types.ReplyKeyboardRemove())
        spam_info = 0
        not_spam_info = 0
        for user in users:
            try:
                await bot.send_photo(chat_id=user[0],photo=data.get('announce_photo_id'), caption=data.get('announce_text'))
                not_spam_info +=1
                await asyncio.sleep(0.6)
            except:
                spam_info+=1
        for admin in ADMINS:
    
            await bot.send_message(chat_id=admin, text=f"Xabar yetib bormaganlar(spam): {spam_info}\nXabar yetib borganlar soni: {not_spam_info}")
            await bot.send_message(admin ,"Admin menu:", reply_markup= await main_menu_admin_btns())
        
        await state.reset_state()
    elif call.data=="no":
        for admin in ADMINS:
            await bot.send_message(chat_id=admin, text=f"Xabar o'chirildi🗑", reply_markup=await main_menu_admin_btns())
        await state.reset_state()
        await call.message.delete()





@dp.message_handler(state=Admin_announce.announce_btn_text)
async def admin(message: types.Message, state:FSMContext):
    await state.update_data(announce_btn_text=message.text)
    await message.answer('Knopka URLni yuboring: ')
    await Admin_announce.announce_url.set()

@dp.message_handler(state=Admin_announce.announce_url)
async def admin(message: types.Message, state:FSMContext):
    await state.update_data(announce_url=message.text)
    data = await state.get_data()
    await message.answer_photo(photo=data.get('announce_photo_id'), caption=data.get('announce_text'), reply_markup= await generate_url_inline_btn(data.get('announce_btn_text'), data.get('announce_url')))
    await message.answer("E'lonni tekshiring!!!!", reply_markup=await generate_yes_not_btns2())
    await Admin_announce.announce_check3.set()


@dp.callback_query_handler(state=Admin_announce.announce_check3)
async def admin(call: types.CallbackQuery, state:FSMContext):
    data = await state.get_data()
    users = db.give_all_users()
    await state.finish()
    if call.data =="yes":
        await call.message.delete()
        await call.message.answer("Yuborilmoqda!!!", reply_markup=types.ReplyKeyboardRemove())
        spam_info = 0
        not_spam_info = 0
        for user in users:
            try:
                await bot.send_photo(chat_id=user[0],photo=data.get('announce_photo_id'), caption=data.get('announce_text'), reply_markup= await generate_url_inline_btn(data.get('announce_btn_text'), data.get('announce_url')))
                not_spam_info +=1
                await asyncio.sleep(0.6)
            except:
                spam_info+=1
        for admin in ADMINS:
            await bot.send_message(chat_id=admin, text=f"Xabar yetib bormaganlar(spam): {spam_info}\nXabar yetib borganlar soni: {not_spam_info}")
            await bot.send_message(chat_id=admin, text="Admin menu:" , reply_markup= await main_menu_admin_btns())
        
        await state.reset_state()
    elif call.data=="no":
        for admin in ADMINS:
            await bot.send_message(chat_id=admin, text=f"Xabar o'chirildi🗑", reply_markup=await main_menu_admin_btns())
        await state.reset_state()
        await call.message.delete()
