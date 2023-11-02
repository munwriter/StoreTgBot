import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.misc.environment import secret_keys as sk
from bot.handlers import register_all_handlers
from bot.database.models import DataBase as DB


async def __on_start_up(dp: Dispatcher):
    db = DB()
    register_all_handlers(dp, db)

def run():
    bot = Bot(token=sk('TOKEN'))
    dp = Dispatcher(bot, storage=MemoryStorage())
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)