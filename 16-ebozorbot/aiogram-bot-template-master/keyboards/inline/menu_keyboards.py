import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from ...loader import db

menu_cd = CallbackData('show_menu', 'level', 'category', 'subcategory', 'item_id')
buy_item = CallbackData('buy', 'item_id')


def make_callback_data(level, category='0', subcategory='0', item_id='0'):
    return menu_cd.new(level=level, category=category, subcategory=subcategory, item_id=item_id)


