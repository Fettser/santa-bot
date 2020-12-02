from loader import db
from asyncpg import Connection


class DBCommand:
    pool: Connection = db
    ADD_NEW_USER = "INSERT INTO members(name, index, email, user_id, city, street, interests)" \
                   " VALUES ($1, $2, $3, $4, $5, $6, $7)"
    REMOVE_USER = "DELETE FROM members WHERE user_id=$1"
    GET_ALL_USER = "SELECT * FROM members"
    GET_USER = "SELECT * FROM members WHERE user_id=$1"
    UPDATE_SEND = "UPDATE members SET send=true WHERE user_id=$1"
    UPDATE_GET = "UPDATE members SET get=true WHERE user_id=$1"

    async def add_new_user(self, name, index, email, user_id, city, street, interests):
        args = name, index, email, user_id, city, street, interests
        command = self.ADD_NEW_USER
        resp = await self.pool.fetchval(self.GET_USER, user_id)
        if resp is None:
            msg = 'Твоя заявка принята!\n\n' \
                  'В скором времени начнется все самое интересное, ' \
                  'а пока следи за рассылкой в боте, чтобы не пропустить важную информацию 🥰\n\n' \
                  'Если ты неверно указал(а) свои данные, нажми кнопку "Удалить заявку" ' \
                  'и заполни форму повторно.'
            await self.pool.fetchval(command, *args)
            return msg
        else:
            msg = 'Такой пользователь уже есть. Если ты хочешь заново отправить заявку на участие, ' \
                  'нажми "Удалить заявку" ' \
                  'и заполни форму повторно.'
            return msg

    async def remove_user(self, user_id):
        resp = await self.pool.fetchval(self.GET_USER, user_id)
        if resp is None:
            msg = 'Чтобы удалить заявку, для начала отправь ее!'
            return msg
        else:
            await self.pool.fetchval(self.REMOVE_USER, user_id)
            msg = 'Ты успешно удален из базы'
            return msg

    async def get_all_users(self):
        subs = await self.pool.fetch(self.GET_ALL_USER)
        new_subs = []
        for s in subs:
            new_subs.append(tuple(s))
        return new_subs

    async def update_send(self, user_id):
        command = self.UPDATE_SEND
        resp = await self.pool.fetchval(self.GET_USER, user_id)
        if resp is None:
            msg = 'Для начала нужно зарегистрироваться!'
            return msg
        else:
            await self.pool.fetchval(command, user_id)
            msg = 'Действие подтверждено!'
            return msg

    async def update_get(self, user_id):
        command = self.UPDATE_GET
        resp = await self.pool.fetchval(self.GET_USER, user_id)
        if resp is None:
            msg = 'Для начала нужно зарегистрироваться!'
            return msg
        else:
            await self.pool.fetchval(command, user_id)
            msg = 'Действие подтверждено!'
            return msg
