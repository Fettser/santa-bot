from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import URL_ADMIN, URL_PROM

choice = InlineKeyboardMarkup(row_width=2)

admin = InlineKeyboardButton(text='Миша', url=URL_ADMIN)
prom = InlineKeyboardButton(text='Маша', url=URL_PROM)
choice.insert(admin)
choice.insert(prom)