from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_menu = {
    "Button-1":'button_1',
    "Button-2":'buton_2',
    "📞 Biz bilan bog'lanish":'support'
}

async def main_menubtns():
    main_menu_btns = InlineKeyboardMarkup(row_width=2)
    for key_, value_ in main_menu.items():
        main_menu_btns.insert(
            InlineKeyboardButton(text=key_, callback_data=value_)
        )
    return main_menu_btns



















