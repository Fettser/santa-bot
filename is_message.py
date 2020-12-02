async def from_message(message):
    msg = message.split('\n')
    name = msg[0]
    email = msg[1]
    index = msg[3]
    city = msg[2]
    street = msg[4]
    interests = msg[5]
    return name, email, index, city, street, interests
