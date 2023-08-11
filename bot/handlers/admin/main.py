from aiogram import Dispatcher
from bot import keyboards as kb
from bot.templates import descriptions as dc
from aiogram import types


def register_admin_handlers(dp: Dispatcher):
    @dp.message_handler(text='Администрирование')
    async def admin_start(message: types.Message):
        if message.from_user.id == 644920251:
            await message.answer('Вы вошли в панель администрирования', reply_markup=kb.admin_menu_keyboard)
        else:
            await message.answer('Вы не являетесь администратором')
    