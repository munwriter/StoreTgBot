import re

import aiogram.utils.markdown as fmt

from bot.database.models import get_user_data


def cart_parser(message):
    res = '\n'.join(get_user_data(message.from_user.id)[0][1].split(','))
    total_price = [int(re.sub('\D', '', i)) for i in res.split('руб')[:-1]]
    return f'{fmt.text(fmt.hbold(res))}\nИтоговая стоимость: {str(sum(total_price))}руб'
    