from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from loader import dp
from keyboard.outline.choose_command import rem_ans, markup
from states.States import Interview
from is_message import from_message
import asyncio
from loader import bot
from aiogram.utils.exceptions import BotBlocked, ChatNotFound
from date_filter import date_filter
from keyboard.inline.inline import choice
from database import DBCommand

db = DBCommand()


@dp.message_handler(Text('Отмена'), state='*')
async def res_state(message: Message, state: FSMContext):
    await message.answer(text='Действие отменено', reply_markup=markup)
    await state.reset_state()


@dp.message_handler(commands=['start'])
async def start_mess(message: Message):
    await message.answer(
        text='Приветствую тебя, Тайный Санта! 💔 Для участия, первым делом нужно зарегестрироваться.\n'
             'Для этого нажми кнопку принять участие и следуй инструкции!\n'
             'Если у тебя есть вопросы, то нажми /help',
        reply_markup=markup)


@dp.message_handler(Text('Принять участие'))
async def participate(message: Message):
    await message.answer(
        text='Мы рады, что ты теперь с нами! Теперь заполни форму, '
             'чтобы твой Тайный Санта смог отправить тебе подарок 😋 '
             'При заполнении каждый пункт пиши с новой строки, чтобы бот мог корректно записать тебя на участие\n\n'
             'Вот какие данные нужно оставить:\n'
             'ФИО, email, город(село, деревня), почтовый индекс, '
             'улица(с указанием дома и номера квартиры), свои интересы\n\n'
             'Вот пример, как нужно указать свои данные:\n'
             'Иванов Иван Иванович\n'
             'ivanov@example.com\n'
             'Город Москва\n'
             '123456\n'
             'Улица Пушкина, дом Колотушкина\n'
             'Увлекаюсь игрой на гитаре\n\n'
             'Если ты передумал отправлять заявку, то нажми "Отмена".',
        reply_markup=rem_ans)
    await Interview.Q1.set()


@dp.message_handler(state=Interview.Q1)
async def req_on_form(message: Message, state: FSMContext):
    try:
        name, email, index, city, street, interests = await from_message(message.text)
        user_id = message.from_user.id
        msg = await db.add_new_user(name=name, email=email, index=index, user_id=user_id, city=city,
                                    street=street, interests=interests)
        await message.answer(text=msg, reply_markup=markup)
    except IndexError:
        await message.answer(text='Ты некорректно заполнил форму 😟\n Пожалуйста, попробуй еще раз',
                             reply_markup=markup)

    await state.reset_state()


@dp.message_handler(Text('Удалить заявку'))
async def del_sab(message: Message):
    user_id = message.from_user.id
    msg = await db.remove_user(user_id=user_id)
    await message.answer(text=msg)


async def time(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        end_date, now_date = date_filter()
        if now_date == end_date:
            subs = await db.get_all_users()
            send_subs = list(reversed(subs))
            if len(subs) % 2:
                pass
            else:
                send_subs[0], send_subs[len(subs) // 2] = send_subs[len(subs) // 2], send_subs[0]
            for i in range(len(subs)):
                try:
                    await bot.send_message(chat_id=subs[i][3], text=f'Вот твой подопечный:\n\n{send_subs[i][0]}\n'
                                                                    f'{send_subs[i][1]}\n{send_subs[i][2]}\n'
                                                                    f'{send_subs[i][4]}\n'
                                                                    f'{send_subs[i][5]}\n{send_subs[i][6]}\n\n'
                                                                    f'Теперь в боте доступны 2 новые команды /get '
                                                                    f'и /sent. Отправь боту /get как только ты получишь'
                                                                    f' подарок и /sent, когда ты отправишь свой',
                                           disable_notification=True)
                    await asyncio.sleep(0.3)
                except BotBlocked:
                    pass
                except ChatNotFound:
                    pass


@dp.message_handler(commands=['help'])
async def helper(message: Message):
    await message.answer(text='По вопросам работы бота пиши Мише. По организационным вопросам - Маше.\n'
                              'С радостью поможем и ответим на все вопросы 😉', reply_markup=choice)


@dp.message_handler(commands=['sent'])
async def sent(message: Message):
    user_id = message.from_user.id
    msg = await db.update_send(user_id)
    await message.answer(text=msg, reply_markup=markup)


@dp.message_handler(commands=['get'])
async def sent(message: Message):
    user_id = message.from_user.id
    msg = await db.update_get(user_id)
    await message.answer(text=msg, reply_markup=markup)
