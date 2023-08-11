import logging
from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
import os
from bot.handlers import register_all_handlers


async def __on_start_up(dp: Dispatcher):
    register_all_handlers(dp)

def run():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher(bot)
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)