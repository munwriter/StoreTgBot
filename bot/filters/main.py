from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from bot.misc.environment import secret_keys as sk


class AdminFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return str(message.from_user.id) == sk('ADMIN_ID')

def register_all_filters(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)