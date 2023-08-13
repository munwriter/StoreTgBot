from aiogram import Dispatcher

from .admin_panel import initial_admin_handlers
from .add_product import admin_add_product_handler
from .delete_product import admin_delete_product_handler


def register_admin_handlers(dp: Dispatcher):
    initial_admin_handlers(dp)
    admin_add_product_handler(dp)
    admin_delete_product_handler(dp)
    
    

    
        
    