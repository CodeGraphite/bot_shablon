from aiogram.dispatcher.filters.state import State, StatesGroup



class Admin_announce(StatesGroup):

    announce_photo_id = State()
    announce_text = State()

    announce_check_state = State()
    announce_check1 = State()
    announce_check2 = State()
    announce_check3 = State()


    announce_url = State()
    announce_btn_text = State()