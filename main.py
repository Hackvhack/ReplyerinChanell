from telethon.sync import TelegramClient, events
# Апи айди и хэш можно получить с сайта https://my.telegram.org/
api_id = 'Ваш Апи Айди'
api_hash = 'Ваш Апи Хэш '
phone_number = 'Ваш номер телефона'

source_channel_username = 'Канал где будет браться триггер сообщение'

target_channel_username = 'Канал где будет писаться сообещние'

client = TelegramClient('session_name', api_id, api_hash)

async def send_message_to_target_channel(message):
    await client.send_message(target_channel_username, message)

@client.on(events.NewMessage(chats=source_channel_username))
async def Trigger(event):
    if 'Триггер' in event.message.message:
        await send_message_to_target_channel("Ответ")

# Элемент с Триггером и ответом можно копировать до бесконечности, только нужно менять слова после async def

client.start(phone_number)

client.run_until_disconnected()