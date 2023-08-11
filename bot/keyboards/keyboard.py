from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('🧨Начать🧨')

main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('🛒Корзина🛒').add('🎲Ассортимент🎲').add('🔧Поддержка🔧')
main_menu_admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('🛒Корзина🛒').add('🎲Ассортимент🎲').add('🔧Поддержка🔧').add('Администрирование')

admin_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add('Добавить товар').add('Редактировать товар').add('Удалить товар').add('Назад в меню')

assortment_inlain_button = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='🎲Ассортимент🎲', callback_data='assortment'))
                
assortment_inlain_keyboard = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='NEIGHBORHOOD x Adidas ADIMATIC', callback_data='adimatic'),
                                                                   InlineKeyboardButton(text='Nike SB Dunk Low Strangelove', callback_data='strangelove'),
                                                                   InlineKeyboardButton(text='New Balance 530', callback_data='530'))

product_inlain_menu = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Добавить в корзину', callback_data='add_to_cart'),
                                                        InlineKeyboardButton(text='Назад к ассортименту', callback_data='back_to_assorment'))