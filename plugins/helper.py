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

import asyncio
from pyrogram import Client, filters, emoji
from utils import USERNAME, mp
from config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

msg=Config.msg
CHAT=Config.CHAT
ADMINS=Config.ADMINS
playlist=Config.playlist

HOME_TEXT = "👋🏻 **Hi [{}](tg://user?id={})**,\n\nSaya **RelaxMusicBot** \nSaya Akan Membantumu Memutar Music / Radio  / YouTube Live di Grup & Channel 24 Jam Nonstop. Created By @justthetech"
HELP_TEXT = """
🎧 --**Untuk Info Lengkap**--
(Join @robotprojectx)

--**Common Commands**-- :

\u2022 `/play` - 𝘳𝘦𝘱𝘭𝘺 𝘵𝘰 𝘢𝘯 𝘢𝘶𝘥𝘪𝘰 𝘰𝘳 𝘺𝘰𝘶𝘛𝘶𝘣𝘦 𝘭𝘪𝘯𝘬 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘪𝘵 𝘰𝘳 𝘶𝘴𝘦 /𝘱𝘭𝘢𝘺 [𝘴𝘰𝘯𝘨 𝘯𝘢𝘮𝘦]
\u2022 `/help` - 𝘴𝘩𝘰𝘸𝘴 𝘩𝘦𝘭𝘱 𝘧𝘰𝘳 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴
\u2022 `/song` [𝘴𝘰𝘯𝘨 𝘯𝘢𝘮𝘦] - 𝘥𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘵𝘩𝘦 𝘴𝘰𝘯𝘨 𝘢𝘴 𝘢𝘶𝘥𝘪𝘰 𝘵𝘳𝘢𝘤𝘬
\u2022 `/current` - 𝘴𝘩𝘰𝘸𝘴 𝘱𝘭𝘢𝘺𝘪𝘯𝘨 𝘵𝘪𝘮𝘦 𝘰𝘧 𝘤𝘶𝘳𝘳𝘦𝘯𝘵 𝘵𝘳𝘢𝘤𝘬
\u2022 `/playlist` - 𝘴𝘩𝘰𝘸𝘴 𝘵𝘩𝘦 𝘤𝘶𝘳𝘳𝘦𝘯𝘵 𝘱𝘭𝘢𝘺𝘭𝘪𝘴𝘵 𝘸𝘪𝘵𝘩 𝘤𝘰𝘯𝘵𝘳𝘰𝘭𝘴

--**Admin Commands**-- :

\u2022 `/radio` - 𝘴𝘵𝘢𝘳𝘵 𝘳𝘢𝘥𝘪𝘰 𝘴𝘵𝘳𝘦𝘢𝘮
\u2022 `/stopradio` - 𝘴𝘵𝘰𝘱 𝘳𝘢𝘥𝘪𝘰 𝘴𝘵𝘳𝘦𝘢𝘮
\u2022 `/skip` - 𝘴𝘬𝘪𝘱 𝘤𝘶𝘳𝘳𝘦𝘯𝘵 𝘮𝘶𝘴𝘪𝘤
\u2022 `/join` - 𝘫𝘰𝘪𝘯 𝘵𝘩𝘦 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵
\u2022 `/leave` - 𝘭𝘦𝘢𝘷𝘦 𝘵𝘩𝘦 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵
\u2022 `/stop` - 𝘴𝘵𝘰𝘱 𝘱𝘭𝘢𝘺𝘪𝘯𝘨 𝘮𝘶𝘴𝘪𝘤
\u2022 `/volume` - 𝘤𝘩𝘢𝘯𝘨𝘦 𝘷𝘰𝘭𝘶𝘮𝘦 (0-200)
\u2022 `/replay` - 𝘱𝘭𝘢𝘺 𝘧𝘳𝘰𝘮 𝘵𝘩𝘦 𝘣𝘦𝘨𝘪𝘯𝘯𝘪𝘯𝘨
\u2022 `/clean` - 𝘳𝘦𝘮𝘰𝘷𝘦 𝘶𝘯𝘶𝘴𝘦𝘥 𝘳𝘢𝘸 𝘧𝘪𝘭𝘦𝘴
\u2022 `/pause` - 𝘱𝘢𝘶𝘴𝘦 𝘱𝘭𝘢𝘺𝘪𝘯𝘨 𝘮𝘶𝘴𝘪𝘤
\u2022 `/resume` - 𝘳𝘦𝘴𝘶𝘮𝘦 𝘱𝘭𝘢𝘺𝘪𝘯𝘨 𝘮𝘶𝘴𝘪𝘤
\u2022 `/mute` - 𝘮𝘶𝘵𝘦 𝘵𝘩𝘦 𝘷𝘤 𝘶𝘴𝘦𝘳𝘣𝘰𝘵
\u2022 `/unmute` - 𝘶𝘯𝘮𝘶𝘵𝘦 𝘵𝘩𝘦 𝘷𝘤 𝘶𝘴𝘦𝘳𝘣𝘰𝘵
\u2022 `/restart` - 𝘶𝘱𝘥𝘢𝘵𝘦 & 𝘳𝘦𝘴𝘵𝘢𝘳𝘵 𝘵𝘩𝘦 𝘣𝘰𝘵

© **Created By** : 
**@robotprojectx | @justthetech** 
"""


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.from_user.id not in Config.ADMINS and query.data != "help":
        await query.answer(
            "Kamu Tidak Diizinkan! 🤣",
            show_alert=True
            )
        return
    else:
        await query.answer()
    if query.data == "replay":
        group_call = mp.group_call
        if not playlist:
            return
        group_call.restart_playout()
        if not playlist:
            pl = f"**Tidak Ada Playlist!**"
        else:
            pl = f"🔄 **Daftar Playlist**:\n" + "\n".join([
                f"**{i}**. **{x[1]}**\n  - **Request Dari :** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(
                f"{pl}",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄", callback_data="replay"),
                            InlineKeyboardButton("⏸", callback_data="pause"),
                            InlineKeyboardButton("⏭", callback_data="skip")
                            
                        ],
                    ]
                )
            )

    elif query.data == "pause":
        if not playlist:
            return
        else:
            mp.group_call.pause_playout()
            pl = f"📋 **Daftar Playlist**:\n" + "\n".join([
                f"**{i}**. **{x[1]}**\n  **Request Dari :** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(f"❌ **Music Dihentikan**\n\n{pl}",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄", callback_data="replay"),
                            InlineKeyboardButton("▶️", callback_data="resume"),
                            InlineKeyboardButton("⏭", callback_data="skip")
                            
                        ],
                    ]
                )
            )

    elif query.data == "resume":   
        if not playlist:
            return
        else:
            mp.group_call.resume_playout()
            pl = f"⏩ **Playlist**:\n" + "\n".join([
                f"**{i}**. **{x[1]}**\n  - **Requested By:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(f"⏩ **Resumed !**\n\n",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄", callback_data="replay"),
                            InlineKeyboardButton("⏸", callback_data="pause"),
                            InlineKeyboardButton("⏭", callback_data="skip")
                            
                        ],
                    ]
                )
            )

    elif query.data=="skip":   
        if not playlist:
            return
        else:
            await mp.skip_current_playing()
            pl = f"⏩ **Daftar Playlist**:\n" + "\n".join([
                f"**{i}**. **{x[1]}**\n  - **Requested By:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        try:
            await query.edit_message_text(f"⏩ **Skipped !**\n\n{pl}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔄", callback_data="replay"),
                        InlineKeyboardButton("⏸", callback_data="pause"),
                        InlineKeyboardButton("⏭", callback_data="skip")
                            
                    ],
                ]
            )
        )
        except:
            pass
    elif query.data=="help":
        buttons = [
                [   InlineKeyboardButton(
                    "⁉️ ᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ɢʀᴜʙ ⁉️", url=f"https://t.me/robotxmusic_bot?startgroup=true")
                ],
                [   InlineKeyboardButton(
                    "☕ ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/robotprojectx"), 
                    InlineKeyboardButton(
                    "ᴏᴡɴᴇʀ ☕", url=f"https://t.me/justthetech")
                ],
                [   InlineKeyboardButton(
                        "✍️ ᴅᴀꜰᴛᴀʀ ᴘᴇʀɪɴᴛᴀʜ ✍️", url="https://telegra.ph/ROBOT-04-23-2")
                ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_text(
            HELP_TEXT,
            reply_markup=reply_markup

        )

    elif query.data=="close":
        await query.message.delete()


@Client.on_message(filters.command(["start", f"start@{USERNAME}"]))
async def start(client, message):
    buttons = [
                [   InlineKeyboardButton(
                    "⁉️ ᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ɢʀᴜʙ ⁉️", url=f"https://t.me/robotxmusic_bot?startgroup=true")
                ],
                [   InlineKeyboardButton(
                    "☕ ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/robotprojectx"), 
                    InlineKeyboardButton(
                    "ᴏᴡɴᴇʀ ☕", url=f"https://t.me/justthetech")
                ],
                [   InlineKeyboardButton(
                        "✍️ ᴅᴀꜰᴛᴀʀ ᴘᴇʀɪɴᴛᴀʜ ✍️", url="https://telegra.ph/ROBOT-04-23-2")
                ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    m=await message.reply_photo(photo="https://telegra.ph/file/4e839766d45935998e9c6.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await mp.delete(m)
    await mp.delete(message)



@Client.on_message(filters.command(["help", f"help@{USERNAME}"]))
async def help(client, message):
    buttons = [
                [   InlineKeyboardButton(
                    "⁉️ ᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ɢʀᴜʙ ⁉️", url=f"https://t.me/robotxmusic_bot?startgroup=true")
                ],
                [   InlineKeyboardButton(
                    "☕ ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/robotprojectx"), 
                    InlineKeyboardButton(
                    "ᴏᴡɴᴇʀ ☕", url=f"https://t.me/justthetech")
                ],
                [   InlineKeyboardButton(
                        "✍️ ᴅᴀꜰᴛᴀʀ ᴘᴇʀɪɴᴛᴀʜ ✍️", url="https://telegra.ph/ROBOT-04-23-2")
                ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if msg.get('help') is not None:
        await msg['help'].delete()
    msg['help'] = await message.reply_photo(photo="https://telegra.ph/file/4e839766d45935998e9c6.jpg", caption=HELP_TEXT, reply_markup=reply_markup)
    await mp.delete(message)

