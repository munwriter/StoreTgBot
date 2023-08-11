from aiogram import Dispatcher

from .admin_init import initial_admin_handlers
from .add_product import admin_add_product_handler


def register_admin_handlers(dp: Dispatcher):
    admin_add_product_handler(dp)
    initial_admin_handlers(dp)
    

    
        
    