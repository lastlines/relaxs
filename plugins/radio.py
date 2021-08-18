"""
RadioPlayerV3, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

from pyrogram import Client, filters, emoji
from pyrogram.types import Message
from utils import mp, RADIO, USERNAME
from config import Config, STREAM

from helpers.filters import command, other_filters

ADMINS=Config.ADMINS

@Client.on_message(command(["radio", f"radio@{USERNAME}"]) & other_filters)
async def radio(client, message: Message):
    if 1 in RADIO:
        k=await message.reply_text(f"⚠️ **Please Stop Existing Live Stream!**")
        await mp.delete(k)
        await message.delete()
        return
    await mp.start_radio()
    k=await message.reply_text(f"🎶 **Live Stream Started :** \n<code>{STREAM}</code>")
    await mp.delete(k)
    await mp.delete(message)

@Client.on_message(command(["stopradio", f"stopradio@{USERNAME}"]) & other_filters)
async def stop(_, message: Message):
    if 0 in RADIO:
        k=await message.reply_text(f"⚠️ **Please Start A Live Stream First!**")
        await mp.delete(k)
        await mp.delete(message)
        return
    await mp.stop_radio()
    k=await message.reply_text(f"{emoji.CROSS_MARK_BUTTON} **Live Stream Ended Successfully!**")
    await mp.delete(k)
    await mp.delete(message)
