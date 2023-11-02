from aiogram import Dispatcher

from .client.main import register_client_handlers
from .other import register_other_handlers
from .admin.main import register_admin_handlers
from bot.filters.main import register_all_filters
from bot.database.models import DataBase as models


def register_all_handlers(dp: Dispatcher, models: models):
    register_all_filters(dp)
    register_admin_handlers(dp, models)
    register_client_handlers(dp, models)
    register_other_handlers(dp)
    





