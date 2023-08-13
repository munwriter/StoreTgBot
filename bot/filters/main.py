from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from bot.misc.environment import secret_keys


class AdminFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return str(message.from_user.id) == secret_keys('ADMIN_ID')

def register_all_filters(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)