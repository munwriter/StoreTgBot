from aiogram import Dispatcher, types
import aiogram.utils.markdown as fmt
from dotenv import load_dotenv
import os
from bot import keyboards as kb

def register_other_handlers(dp: Dispatcher):
    load_dotenv()

    @dp.message_handler(text='🧨Начать🧨')
    async def main_menu(message: types.Message):
        await message.answer_sticker('CAACAgQAAxkBAAEJ951k057Igh_S_q3xF3aJhjQwYvWeYgACUQADg2rQEPS6m0vsIMEvMAQ')
        if str(message.from_user.id) == os.getenv('ADMIN_ID'):
            await message.answer(fmt.text('Вы вошли в главное меню\n', fmt.hbold('Administrator mode on')), parse_mode='HTML', reply_markup=kb.main_menu_admin_keyboard)
        else:
            await message.answer('Вы вошли в главное меню', reply_markup=kb.main_menu_keyboard)

    @dp.message_handler()
    async def invalid_requests(message: types.Message):
        await message.reply('Я не понимаю о чем вы :(')
