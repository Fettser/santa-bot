from aiogram import Bot, Dispatcher
import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import logging
from pool import create_pool

loop = asyncio.get_event_loop()

bot = Bot(token=config.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage, loop=loop)
db = loop.run_until_complete(create_pool())
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)
