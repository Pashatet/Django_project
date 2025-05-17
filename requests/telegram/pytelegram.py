import os

from telethon import TelegramClient, events, sync, connection
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterPinned

r_api = 20772742
r_hash = "a37953fd7e60cbf80db19ba61f1acd1c"
group_url = "https://t.me/Parsinger_Telethon_Test"
target_user_id = 6388067367
res = []

with TelegramClient('my', r_api, r_hash, system_version="4.10.5 beta x64") as client:
    client.send_message('@Anthony_Alexander534', 'test')