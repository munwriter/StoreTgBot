from aiogram import Dispatcher

from .client.main import register_client_handlers
from .other import register_other_handlers
from .admin.main import register_admin_handlers
from bot.filters.main import register_all_filters


def register_all_handlers(dp: Dispatcher):
    register_all_filters(dp)
    register_admin_handlers(dp)
    register_client_handlers(dp)
    register_other_handlers(dp)
    





