from aiogram import Dispatcher
from bot import keyboards as kb
from bot.templates import descriptions as dc
from aiogram import types


def register_client_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['start'])
    async def cmd_start(message: types.Message):    
        await message.answer_sticker('CAACAgQAAxkBAAEJ9r1k01FoAzo2Gysv8QHETLyTswvirwACRAADg2rQEM7UCtdq5wg8MAQ')
        await message.answer(f'💢 Приветствуем тебя в нашем интрернет сникерссторе, {message.from_user.first_name}!', reply_markup=kb.start_keyboard)

    @dp.message_handler(text='🛒Корзина🛒')
    async def shopping_cart(message: types.Message):
        await message.answer('Ваша корзина пуста :(. \nВремя для нового заказа!', reply_markup=kb.assortment_inlain_button)

    @dp.message_handler(text='🎲Ассортимент🎲')
    async def assortment(message: types.Message):
        await message.answer(dc.ASSORTIMENT_DESCRIPTION, reply_markup=kb.assortment_inlain_keyboard)

    @dp.message_handler(text='🔧Поддержка🔧')
    async def shopping_cart(message: types.Message):
        await message.answer('Связаться с поддержкой - @gleb2999')

    @dp.callback_query_handler()
    async def some_callback_handler(call: types.CallbackQuery):
        if call.data == 'assortment':
            await call.message.answer(dc.ASSORTIMENT_DESCRIPTION, reply_markup=kb.assortment_inlain_keyboard)
            await call.answer()

        elif call.data == 'adimatic':
            photos = types.MediaGroup()
            photos.attach_photo(types.InputFile('bot/templates/media/ipad_neighborhood-x-adidas-adimatic-grey.jpeg'), caption='NEIGHBORHOOD x Adidas ADIMATIC - слияние уличного стиля и передовых технологий. Черные тона и агрессивные линии вдохновлены городским движением, а технология BOOST в подошве обеспечивает комфорт и амортизацию. Эти кроссовки - яркий аксессуар для выражения индивидуальности и стиля.')
            photos.attach_photo(types.InputFile('bot/templates/media/ipad_neighborhood-x-adidas-adimatic-black.jpeg'))
            await call.message.answer_media_group(media=photos)
            await call.message.answer(text='Что думаете?', reply_markup=kb.product_inlain_menu)
            await call.answer()
        
        elif call.data == 'back_to_assorment':
            await call.message.answer(dc.ASSORTIMENT_DESCRIPTION, reply_markup=kb.assortment_inlain_keyboard)
            await call.answer()