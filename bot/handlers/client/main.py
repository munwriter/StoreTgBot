import aiogram.utils.markdown as fmt
from aiogram import Dispatcher, types

from bot import keyboards as kb
from bot.database import models
from bot.misc.environment import secret_keys
from bot.templates import descriptions as dc
from .utils.cart_parser import cart_parser


def register_client_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        if not models.get_user_data(message.from_user.id):
            await models.add_user(message.from_user.id)
        await message.answer_sticker('CAACAgQAAxkBAAEJ9r1k01FoAzo2Gysv8QHETLyTswvirwACRAADg2rQEM7UCtdq5wg8MAQ')
        await message.answer(f'💢 Приветствуем тебя в нашем интрернет сникерссторе, {message.from_user.first_name}!', reply_markup=kb.start_keyboard)

    @dp.message_handler(text='🛒Корзина🛒')
    async def shopping_cart(message: types.Message):
        if models.get_user_data(message.from_user.id)[0][1]!= None:
            await message.answer_sticker('CAACAgQAAxkBAAEKH-pk6MTMUVbUoZpl8A6vOSKz4P9nBgACUgADg2rQEAnSAbE-A3P-MAQ', reply_markup=types.ReplyKeyboardRemove())
            await message.answer(f'Товары в вашей корзине:\n\n{cart_parser(message)}', parse_mode='HTML', reply_markup=kb.cart_inlain_keyboard)
        else:
            await message.answer('Ваша корзина пуста :(. \nВремя для нового заказа!', reply_markup=kb.back_to_assortment_inlain_keyboard)

    @dp.message_handler(text='🎲Ассортимент🎲')
    async def assortment(message: types.Message):
        await message.answer_sticker('CAACAgQAAxkBAAEKAAJk19dVR9rwHlml2HOglfF0KHHysQACTAADg2rQENhMNgNvS0EOMAQ', reply_markup=types.ReplyKeyboardRemove())
        await message.answer(dc.ASSORTIMENT_DESCRIPTION, reply_markup=kb.dinamic_assortmen_keyboard())

    @dp.message_handler(text='🔧Поддержка🔧')
    async def support(message: types.Message):
        await message.answer('Связаться с поддержкой - @gleb2999')

    @dp.callback_query_handler()
    async def callback_handlers(call: types.CallbackQuery):
        if call.data == 'assortment':
            await call.message.answer_sticker('CAACAgQAAxkBAAEKAAJk19dVR9rwHlml2HOglfF0KHHysQACTAADg2rQENhMNgNvS0EOMAQ', reply_markup=types.ReplyKeyboardRemove())
            await call.message.answer(dc.ASSORTIMENT_DESCRIPTION, reply_markup=kb.dinamic_assortmen_keyboard())
            await call.answer()        
        elif call.data in models.get()['name']:
            index = models.get()['name'].index(call.data)
            await call.bot.send_photo(call.from_user.id, models.get()['photo'][index], f"Название: {models.get()['name'][index]}\nОписание: {models.get()['description'][index]}\nЦена товара: {models.get()['price'][index]}руб", reply_markup=types.ReplyKeyboardRemove())
            await call.message.answer(text='Что думаете?', reply_markup=kb.dinamic_product_inlain_keyboard(f"{models.get()['name'][index]} - {models.get()['price'][index]}руб"))
            await call.answer()       
        elif call.data == 'back_to_menu':
            if str(call.from_user.id) == secret_keys('ADMIN_ID'):
                await call.message.answer(fmt.text('Вы вошли в главное меню', fmt.hbold('Administrator mode on'), sep='\n'), parse_mode='HTML', reply_markup=kb.main_menu_admin_keyboard)
                await call.answer()
            else:
                await call.message.answer('Вы вошли в главное меню',reply_markup=kb.main_menu_keyboard)
                await call.answer()   
        elif call.data == 'clear_cart':
            await models.clear_cart(call.from_user.id)  
            await call.answer('Корзина успешно очищена', show_alert=True)
        elif call.data[0] == '+':
            await models.add_product_to_cart(id=call.from_user.id, product_name=call.data[1:])
            await call.answer('Товар успешно добавлен в корзину', show_alert=True)
