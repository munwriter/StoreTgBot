import re

import aiogram.utils.markdown as fmt

from bot.database.models import DataBase as models


def cart_parser(message, models):
    res = '\n'.join(models.get_user_data(message.from_user.id)[0][1].split(','))
    total_price = [int(re.sub('\D', '', i)) for i in res.split('руб')[:-1]]
    return f'{fmt.text(fmt.hbold(res))}\nИтоговая стоимость: {str(sum(total_price))}руб'
    