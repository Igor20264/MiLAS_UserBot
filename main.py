from datetime import datetime

from telethon.sync import TelegramClient
from telethon import functions, types

api_id = 24601404
api_hash = "88ace8e679ea4dc71bf5ddeeaca0f47e"

with TelegramClient('Asus-CustomClient', api_id, api_hash) as client:
    result = client(functions.messages.SearchGlobalRequest(
        q='впн',
        offset_rate=0,
        offset_peer=types.InputPeerEmpty(),
        offset_id=0,
        limit=100,
        filter=types.InputMessagesFilterEmpty(),
        min_date=datetime(2022, 1, 1),
        max_date=datetime.now(),
    ))
    for message in result.messages:
        print(message,end="\n---===---\n")