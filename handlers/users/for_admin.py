from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, IDFilter
from loader import dp
from config import ADMIN_ID
from keyboard.outline.choose_command import rem_talk, markup
from states.States import Admin
from aiogram.utils.exceptions import BotBlocked
from loader import bot
from asyncio import sleep
from database import DBCommand

db = DBCommand()


@dp.message_handler(Text('Не рассказывать'), IDFilter(ADMIN_ID), state='*')
async def res_state(message: Message, state: FSMContext):
    await message.answer(text='Отменено', reply_markup=markup)
    await state.reset_state()


@dp.message_handler(Text('Рассказать всем'), IDFilter(ADMIN_ID))
async def talk_all(message: Message):
    await message.answer(text='Введи свой текст', reply_markup=rem_talk)
    await Admin.A1.set()


@dp.message_handler(state=Admin.A1)
async def send_all(message: Message, state: FSMContext):
    subs = await db.get_all_users()
    await message.answer(text='Рассылка сделана', reply_markup=markup)
    for s in subs:
        try:
            await bot.send_message(chat_id=s[0], text=message.text, disable_notification=True)
            await sleep(0.3)
        except BotBlocked:
            pass
    await state.reset_state()
