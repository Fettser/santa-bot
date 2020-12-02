import asyncpg
from config import PG_PASS, PG_USER, PG_HOST, PG_NAME
import asyncio


async def create_pool():
    return await asyncpg.create_pool(dsn=f'postgres://{PG_USER}:{PG_PASS}@{PG_HOST}:5432/{PG_NAME}')


async def create_db():
    create_db_command = open('create_db.sql', 'r').read()

    conn: asyncpg.Connection = await asyncpg.connect(dsn=f'postgres://{PG_USER}:{PG_PASS}@{PG_HOST}:5432/{PG_NAME}')
    await conn.execute(create_db_command)
    await conn.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
