from aiogram import Dispatcher
from aiogram import types
import aiogram.utils.markdown as fmt

from bot import keyboards as kb
from bot.filters.main import AdminFilter
from bot.database.models import DataBase as models
from bot.misc.environment import secret_keys


def admin_delete_product_handler(dp: Dispatcher, models: models):
    @dp.message_handler(AdminFilter(), text='Удалить товар')
    async def delete_product(message: types.Message):
        await message.answer_sticker('CAACAgQAAxkBAAEKAwdk2R8-loEM3z_WFBCaAAH_DLEuu9UAAksAA4Nq0BBKm97pMDCqWDAE', reply_markup=types.ReplyKeyboardRemove())
        await message.answer('Выберите товар', reply_markup=kb.dinamic_delete_assortmen_keyboard())

    @dp.callback_query_handler(text_startswith="!")
    async def admin_callback_handler(call: types.CallbackQuery):
        admim_product_callbacks = ['!' + i  for i in models.get_products_details()['name']]
        if call.data in admim_product_callbacks:
            index = admim_product_callbacks.index(call.data)
            await models.delete_product(models.get_products_details()['name'][index])
            await call.message.answer(text='Товар успешно удален', reply_markup=kb.admin_menu_keyboard)
            await call.answer()
        elif call.data == '!back_to_admin_menu':
            await call.message.answer(text='Вы вошли в меню администратора', reply_markup=kb.admin_menu_keyboard)
            await call.answer(text='В данный момент список товаров пуст', show_alert=True)

        
