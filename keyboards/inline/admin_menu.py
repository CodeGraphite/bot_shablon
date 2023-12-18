from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton







main_menu_admin = {
    "E'lon berish 🗞":"announce"
}

async def main_menu_admin_btns():
    btns = InlineKeyboardMarkup(row_width=2)
    for key_, value_ in main_menu_admin.items():
        btns.insert(
            InlineKeyboardButton(text=key_, callback_data=value_)
        )
    return btns