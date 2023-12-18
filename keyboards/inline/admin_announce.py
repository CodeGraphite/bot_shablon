from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


########## ADMIN announce BTNS ##########


menu_announce_inline = {
    "URL knopka":'url_btn',
    "Knopkasiz":'no_btn'
}
async def generate_admin_menu_announce():
    admin_menu_announce = InlineKeyboardMarkup(row_width=2)
    for key, value in menu_announce_inline.items():
        admin_menu_announce.insert(InlineKeyboardButton(text=key, callback_data=value))

    return admin_menu_announce



menu_yes_not_inline = {
    "✅ Xa":'yes',
    "❌ Yo'q":'no'

}


async def generate_url_inline_btn(btn_text, btn_url):
    btns = InlineKeyboardMarkup(row_width=2)
    btns.add(InlineKeyboardButton(btn_text, url=btn_url))
    return btns


async def generate_yes_not_btns2():
    btns = InlineKeyboardMarkup(row_width=2)
    for key, value in menu_yes_not_inline.items():
        btns.insert(InlineKeyboardButton(text=key, callback_data=value))
    return btns





