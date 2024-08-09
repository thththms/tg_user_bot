from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import os
from time import sleep
import datetime
api_id = 22072179
api_hash = "9d4bae939777e3bce3e4eef6556ed88e"
client = Client("my_account", api_id=api_id, api_hash=api_hash)

chat_id = -1002169671885
PUBLIC_CHANNEL1 = "@SLIVY_PRIVATKI_5OPKA"
CHANNEL_ID1 = -1002169671885
count = 0
list = []
with client:

    for message in client.get_chat_history(chat_id):
        if message.date > datetime.datetime(year=2024, month=8, day=8, hour=15, minute=53, second=59):
            list.append(message)
    for message in reversed(list):
        if message.text:
            print("new text messange")
            client.send_message(PUBLIC_CHANNEL1, f"{message.text}", schedule_date=message.date + datetime.timedelta(days=1))
        if message.poll:
            pass
        elif message.media:
            print("new media messange")
            file_path = message.download()
            try:
                if message.photo:
                    if message.caption:
                        client.send_photo(PUBLIC_CHANNEL1, photo=file_path, caption=f"{message.caption}", schedule_date=message.date + datetime.timedelta(days=1))
                    else:
                        client.send_photo(PUBLIC_CHANNEL1, photo=file_path, schedule_date=message.date + datetime.timedelta(days=1))
                elif message.video:
                    if message.caption:
                        client.send_video(PUBLIC_CHANNEL1, video=file_path, caption=f"{message.caption}", schedule_date=message.date + datetime.timedelta(days=1))
                    else:
                        client.send_video(PUBLIC_CHANNEL1, video=file_path, schedule_date=message.date + datetime.timedelta(days=1))
                elif message.document:
                    client.send_document(PUBLIC_CHANNEL1, document=file_path, caption=f"{message.caption}", schedule_date=message.date + datetime.timedelta(days=1))
                elif message.voice:
                    if message.caption:
                        client.send_voice(PUBLIC_CHANNEL1, voice=file_path, caption=f"{message.caption}", schedule_date=message.date + datetime.timedelta(days=1))
                    else:
                        client.send_voice(PUBLIC_CHANNEL1, voice=file_path, schedule_date=message.date + datetime.timedelta(days=1))
                elif message.audio:
                    if message.caption:
                        client.send_audio(PUBLIC_CHANNEL1, audio=file_path, caption=f"{message.caption}", schedule_date=message.date + datetime.timedelta(days=1))
                    else:
                        client.send_audio(PUBLIC_CHANNEL1, audio=file_path, schedule_date=message.date + datetime.timedelta(days=1))
                elif message.video_note:
                    client.send_video_note(PUBLIC_CHANNEL1, video_note=file_path, schedule_date=message.date + datetime.timedelta(days=1))
            finally:
                if file_path and os.path.exists(file_path):
                    os.remove(file_path)

client.run()
