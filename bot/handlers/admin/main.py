from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram import types
from dotenv import load_dotenv
import os
from bot import keyboards as kb
from bot.templates import descriptions as dc




def register_admin_handlers(dp: Dispatcher):
    load_dotenv()

    @dp.message_handler(text='Администрирование')
    async def admin_start(message: types.Message):
        if str(message.from_user.id) == os.getenv('ADMIN_ID'):
            await message.answer('Вы вошли в панель администрирования', reply_markup=kb.admin_menu_keyboard)
    
    
        
    