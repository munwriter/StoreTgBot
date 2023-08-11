from aiogram import Dispatcher, types
from bot import keyboards as kb
import aiogram.utils.markdown as fmt


def register_other_handlers(dp: Dispatcher):

    @dp.message_handler(text='🧨Начать🧨')
    async def main_menu(message: types.Message):
        await message.answer_sticker('CAACAgQAAxkBAAEJ951k057Igh_S_q3xF3aJhjQwYvWeYgACUQADg2rQEPS6m0vsIMEvMAQ')
        if message.from_user.id == 644920251:
            await message.answer(fmt.text('Вы вошли в главное меню\n', fmt.hbold('Administrator mode on')), parse_mode='HTML', reply_markup=kb.main_menu_admin_keyboard)
        else:
            await message.answer('Вы вошли в главное меню', reply_markup=kb.main_menu_keyboard)

    @dp.message_handler()
    async def invalid_requests(message: types.Message):
        await message.reply('Я не понимаю о чем вы :(')
