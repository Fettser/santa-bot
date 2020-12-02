if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    from handlers.users.messages import time
    from loader import loop

    dp.loop.create_task(time(60))
    executor.start_polling(dp, loop=loop, skip_updates=True)
