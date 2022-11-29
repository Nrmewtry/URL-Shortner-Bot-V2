import os
from pyrogram import Client

bot_token = "5426747682:AAEzeVmKTKtlSJjfbZqcQh2vJFDoXqFScHY"
api_id = "1669750"
api_hash = "0f53ee8c576281995d621194aec588d8"
plugins = dict(
    root="plugins"
)

Bot = Client(
    "URL-Shortner-Bot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins=plugins,
    workers=50,
    sleep_threshold=10
)

Bot.run()
