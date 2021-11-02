import asyncio

import re

from config import BOT_USERNAME, GROUP_SUPPORT, IMG_1, IMG_2, UPDATES_CHANNEL

from driver.filters import command, other_filters

from driver.queues import QUEUE, add_to_queue

from driver.snehabhi import call_py

from pyrogram import Client

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from pytgcalls import StreamType

from pytgcalls.types.input_stream import AudioPiped

from youtubesearchpython import VideosSearch

def ytsearch(query):

    try:

        search = VideosSearch(query, limit=1)

        for r in search.result()["result"]:

            ytid = r["id"]

            if len(r["title"]) > 34:

                songname = r["title"][:70]

            else:

                songname = r["title"]

            url = f"https://www.youtube.com/watch?v={ytid}"

        return [songname, url]

    except Exception as e:

        print(e)

        return 0

async def ytdl(link):

    proc = await asyncio.create_subprocess_exec(

        "yt-dlp",

        "-g",

        "-f",

        "bestaudio",

        f"{link}",

        stdout=asyncio.subprocess.PIPE,

        stderr=asyncio.subprocess.PIPE,

    )

    stdout, stderr = await proc.communicate()

    if stdout:

        return 1, stdout.decode().split("\n")[0]

    else:

        return 0, stderr.decode()

@Client.on_message(command(["play", f"play@SNEHABHI_VIDEOBOT"]) & other_filters)

async def play(_, m: Message):

    keyboard = InlineKeyboardMarkup(

        [

            [

                InlineKeyboardButton(

                    text="✨ ɢʀᴏᴜᴘ", url=f"https://t.me/SNEHABHI_SERVER"

                ),

                InlineKeyboardButton(

                    text="🌻 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/SNEHABHI_UPDATES"

                ),

            ]

        ]

    )
    
replied = m.reply_to_message

    chat_id = m.chat.id
     else:

            if len(m.command) < 2:

                await m.reply(

                    "» 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰𝙽 **𝙰𝚄𝙳𝙸𝙾 𝙵𝙸𝙻𝙴** 𝙾𝚁 **𝙶𝙸𝚅𝙴 𝚂𝙾𝙼𝙴𝚃𝙷𝙸𝙽𝙶 𝚃𝙾 𝚂𝙴𝙰𝚁𝙲𝙷.**"

                )

            else:

                suhu = await m.reply("🔎 **𝚂𝙴𝙰𝚁𝙲𝙷𝙸𝙽𝙶...**")

                query = m.text.split(None, 1)[1]

                search = ytsearch(query)

                if search == 0:

                    await suhu.edit("❌ **𝙽𝙾 𝚁𝙴𝚂𝚄𝙻𝚃𝚂 𝙵𝙾𝚄𝙽𝙳.**")

                else:

                    songname = search[0]

                    url = search[1]

                    veez, ytlink = await ytdl(url)

                    if veez == 0:

                        await suhu.edit(f"❌ 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙸𝚂𝚂𝚄𝙴 𝙳𝙴𝚃𝙴𝙲𝚃𝙴𝙳\n\n» `{ytlink}`")

                    else:

                        if chat_id in QUEUE:

                            pos = add_to_queue(

                                chat_id, songname, ytlink, url, "Audio", 0

                            )

                            await suhu.delete()

                            await m.reply_photo(

                                photo=f"{IMG_1}",

                                caption=f"💡 **𝚃𝚁𝙰𝙲𝙺 𝙰𝙳𝙳𝙴𝙳 𝚃𝙾 𝚀𝚄𝙴𝚄𝙴**\n\n🏷 **𝙽𝙰𝙼𝙴:** [{songname}]({url})\n💭 **𝙲𝙷𝙰𝚃:** `{chat_id}`\n🎧 **𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙱𝚈:** {m.from_user.mention()}\n🔢 **𝙰𝚃 𝙿𝙾𝚂𝙸𝚃𝙸𝙾𝙽 »** `{pos}`",

                                reply_markup=keyboard,

                            )

                        else:

                            try:

                                await call_py.join_group_call(

                                    chat_id,

                                    AudioPiped(

                                        ytlink,

                                    ),

                                    stream_type=StreamType().pulse_stream,

                                )

                                add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)

                                await suhu.delete()

                                await m.reply_photo(

                                    photo=f"{IMG_2}",

                                    caption=f"💡 **𝙼𝚄𝚂𝙸𝙲 𝚂𝚃𝚁𝙴𝙰𝙼 𝚂𝚃𝙰𝚁𝚃𝙴𝙳.**\n\n🏷 **𝙽𝙰𝙼𝙴:** [{songname}]({url})\n💭 **𝙲𝙷𝙰𝚃:** `{chat_id}`\n💡 **𝚂𝚃𝙰𝚃𝚄𝚂:** `𝙿𝙻𝙰𝚈𝙸𝙽𝙶`\n🎧 **𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙱𝚈:** {m.from_user.mention()}",

                                    reply_markup=keyboard,

                                )

                            except Exception as ep:

                                await m.reply_text(f"🚫 𝙴𝚁𝚁𝙾𝚁: `{ep}`")
                            else:
                              suhu = await m.reply("🔎 **𝚂𝙴𝙰𝚁𝙲𝙷𝙸𝙽𝙶...**")

                query = m.text.split(None, 1)[1]

                search = ytsearch(query)

                if search == 0:

                    await suhu.edit("❌ **𝙽𝙾 𝚁𝙴𝚂𝚄𝙻𝚃𝚂 𝙵𝙾𝚄𝙽𝙳.**")

                else:

                    songname = search[0]

                    url = search[1]

                    veez, ytlink = await ytdl(url)

                    if veez == 0:

                        await suhu.edit(f"❌ 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙸𝚂𝚂𝚄𝙴 𝙳𝙴𝚃𝙴𝙲𝚃𝙴𝙳\n\n» `{ytlink}`")

                    else:

                        if chat_id in QUEUE:

                            pos = add_to_queue(

                                chat_id, songname, ytlink, url, "Audio", 0

                            )

                            await suhu.delete()

                            await m.reply_photo(

                                photo=f"{IMG_1}",

                                caption=f"💡 **𝚃𝚁𝙰𝙲𝙺 𝙰𝙳𝙳𝙴𝙳 𝚃𝙾 𝚀𝚄𝙴𝚄𝙴**\n\n🏷 **𝙽𝙰𝙼𝙴:** [{songname}]({url})\n💭 **𝙲𝙷𝙰𝚃:** `{chat_id}`\n🎧 **𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙱𝚈:** {m.from_user.mention()}\n🔢 **𝙰𝚃 𝙿𝙾𝚂𝙸𝚃𝙸𝙾𝙽 »** `{pos}`",

                                reply_markup=keyboard,

                            )

                        else:

                            try:

                                await call_py.join_group_call(

                                    chat_id,

                                    AudioPiped(

                                        ytlink,

                                    ),

                                    stream_type=StreamType().pulse_stream,

                                )

                                add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)

                                await suhu.delete()

                                await m.reply_photo(

                                    photo=f"{IMG_2}",

                                    caption=f"💡 **𝙼𝚄𝚂𝙸𝙲 𝚂𝚃𝚁𝙴𝙰𝙼 𝚂𝚃𝙰𝚁𝚃𝙴𝙳.**\n\n🏷 **𝙽𝙰𝙼𝙴:** [{songname}]({url})\n💭 **𝙲𝙷𝙰𝚃:** `{chat_id}`\n💡 **𝚂𝚃𝙰𝚃𝚄𝚂:** `𝙿𝙻𝙰𝚈𝙸𝙽𝙶`\n🎧 **𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙱𝚈:** {m.from_user.mention()}",

                                    reply_markup=keyboard,

                                )

                            except Exception as ep:

                                await m.reply_text(f"🚫 𝙴𝚁𝚁𝙾𝚁: `{ep}`")
                                
                                else:

            suhu = await m.reply("🔎 **𝚂𝙴𝙰𝚁𝙲𝙷𝙸𝙽𝙶...**")

            query = m.text.split(None, 1)[1]

            search = ytsearch(query)

            if search == 0:

                await suhu.edit("❌ **𝙽𝙾 𝚁𝙴𝚂𝚄𝙻𝚃𝚂 𝙵𝙾𝚄𝙽𝙳.**")

            else:

                songname = search[0]

                url = search[1]

                veez, ytlink = await ytdl(url)

                if veez == 0:

                    await suhu.edit(f"❌ 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙸𝚂𝚂𝚄𝙴 𝙳𝙴𝚃𝙴𝙲𝚃𝙴𝙳\n\n» `{ytlink}`")

                else:

                    if chat_id in QUEUE:

                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)

                        await suhu.delete()

                        await m.reply_photo(

                            photo=f"{IMG_1}",

                            caption=f"💡 **𝚃𝚁𝙰𝙲𝙺 𝙰𝙳𝙳𝙴𝙳 𝚃𝙾 𝚃𝙷𝙴 𝚀𝚄𝙴𝚄𝙴**\n\n🏷 **𝙽𝙰𝙼𝙴:** [{songname}]({url})\n💭 **𝙲𝙷𝙰𝚃:** `{chat_id}`\n🎧 **𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙱𝚈:** {m.from_user.mention()}\n🔢 **𝙰𝚃 𝙿𝙾𝚂𝙸𝚃𝙸𝙾𝙽 »** `{pos}`",

                            reply_markup=keyboard,

                        )

                    else:

                        try:

                            await call_py.join_group_call(

                                chat_id,

                                AudioPiped(

                                    ytlink,

                                ),

                                stream_type=StreamType().pulse_stream,

                            )

                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)

                            await suhu.delete()

                            await m.reply_photo(

                                photo=f"{IMG_2}",

                                caption=f"💡 **𝙼𝚄𝚂𝙸𝙲 𝚂𝚃𝚁𝙴𝙰𝙼 𝚂𝚃𝙰𝚁𝚃𝙴𝙳.**\n\n🏷 **Name:** [{songname}]({url})\n💭 **𝙲𝙷𝙰𝚃:** `{chat_id}`\n💡 **𝚂𝚃𝙰𝚃𝚄𝚂:** `𝙿𝙻𝙰𝚈𝙸𝙽𝙶`\n🎧 **𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙱𝚈:** {m.from_user.mention()}",

                                reply_markup=keyboard,

                            )

                        except Exception as ep:

                            await m.reply_text(f"🚫 𝙴𝚁𝚁𝙾𝚁: `{ep}`")
                                
