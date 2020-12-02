from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_1 = KeyboardButton('Принять участие')
btn_2 = KeyboardButton('Удалить заявку')
btn_3 = KeyboardButton('Отмена')
btn_admin_1 = KeyboardButton('Не рассказывать')
markup = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_1, btn_2)
rem_ans = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_3)
rem_talk = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_admin_1)

