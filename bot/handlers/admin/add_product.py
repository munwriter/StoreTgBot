from aiogram import Dispatcher
from aiogram import types
from bot import keyboards as kb
from bot.filters.main import AdminFilter
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMAdminAddProduct(StatesGroup):
    name = State()
    description = State()
    photo = State()
    price = State()

def admin_add_product_handler(dp: Dispatcher):
    @dp.message_handler(AdminFilter(), text='Добавить товар', state=None)
    async def fsm_start(message: types.Message):
        await FSMAdminAddProduct.name.set()
        await message.answer('Пришлите название товара товара', reply_markup=types.ReplyKeyboardRemove())

    @dp.message_handler(AdminFilter(), state=FSMAdminAddProduct.name)
    async def add_product(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdminAddProduct.next()
        await message.answer('Введите описание товара')

    @dp.message_handler(AdminFilter(), state=FSMAdminAddProduct.description)
    async def add_description(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdminAddProduct.next()
        await message.answer('Пришлите фото товара')

    @dp.message_handler(AdminFilter(), content_types=['photo'], state=FSMAdminAddProduct.photo)
    async def add_photo(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdminAddProduct.next()
        await message.answer('Укажите цену товара')

    @dp.message_handler(AdminFilter(), state=FSMAdminAddProduct.price)
    async def add_price(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['price'] = message.text

        async with state.proxy() as data:
            await message.answer(str(data))
        await message.answer('Товар успешно добавлен', reply_markup=kb.admin_menu_keyboard)
        
        await state.finish()