from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           ReplyKeyboardMarkup)

from bot.database.models import DataBase as models


models = models()

'''===============================================CLIENT KEYBOARDS==============================================='''
#just start button
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('🧨Начать🧨')

#2 various if main menu keyboard(admim/client)
main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('🛒Корзина🛒').add('🎲Ассортимент🎲').add('🔧Поддержка🔧')
main_menu_admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('🛒Корзина🛒').add('🎲Ассортимент🎲').add('🔧Поддержка🔧').add('Администрирование')

#back assortment inlain keyboard(if your cart is empty)
back_to_assortment_inlain_keyboard = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='🎲Ассортимент🎲', callback_data='assortment'))   

#back assortment inlain keyboard(if your cart is empty)
cart_inlain_keyboard = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Назад в меню', callback_data='back_to_menu'),
                                                             InlineKeyboardButton(text='Очистить корзину', callback_data='clear_cart')) 

#assortment inlain keyboard
def dinamic_assortmen_keyboard():
    if len(models.get_products())!= 0:
        assortment_inlain_keyboard = InlineKeyboardMarkup(row_width=1)
        for i in range(len(models.get_products())):
            assortment_inlain_keyboard.add(InlineKeyboardButton(text=models.get_products()[i][0], callback_data=models.get_products()[i][0]))
        return assortment_inlain_keyboard.add(InlineKeyboardButton(text='Назад в меню', callback_data='back_to_menu'))                                                                    
    else:
        return InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Назад в меню', callback_data='back_to_menu'),)
    
def dinamic_delete_assortmen_keyboard():
    if len(models.get_products())!= 0:
        assortment_inlain_keyboard = InlineKeyboardMarkup(row_width=1)
        for i in range(len(models.get_products())):
            assortment_inlain_keyboard.add(InlineKeyboardButton(text=models.get_products()[i][0], callback_data=f'!{models.get_products()[i][0]}'))
        return assortment_inlain_keyboard                                                                    
    else:
        return InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Назад в меню администрирования', callback_data='!back_to_admin_menu'))

#product inlain keyboard(add/back)
def dinamic_product_inlain_keyboard(product_name):
    product_inlain_keyboard = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Добавить в корзину', callback_data=f'+{product_name}'),
                                                                    InlineKeyboardButton(text='Назад к ассортименту', callback_data='assortment'))
    return product_inlain_keyboard

'''===============================================ADMIN KEYBOARDS==============================================='''
#admin main menu keyboard
admin_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Добавить товар').add('Удалить товар').add('Назад в меню')


            




