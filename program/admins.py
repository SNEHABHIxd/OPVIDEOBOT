from cache.admins import admins
from driver.snehabhi import call_py
from pyrogram import Client, filters
from driver.decorators import authorized_users_only
from driver.filters import command, other_filters
from driver.queues import QUEUE, clear_queue
from driver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(command(["reload", f"reload@SNEHABHI_BOT"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
  global admins
  new_admins = []
  new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
  for u in new_ads:
    new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
      "✅ 𝚂𝙽𝙴𝙷𝙰𝙱𝙷𝙸 𝚅𝙸𝙳𝙴𝙾 𝙿𝙻𝙰𝚈𝙴𝚁 **𝚁𝙴𝙻𝙾𝙰𝙳𝙴𝙳 𝙲𝙾𝚁𝚁𝙴𝙲𝚃𝙻𝚈 !**\n✅ **𝙰𝙳𝙼𝙸𝙽 𝙻𝙸𝚂𝚃** 𝙷𝙰𝚂 𝙱𝙴𝙴𝙽 **𝚄𝙿𝙳𝙰𝚃𝙴S 𝙱𝚈 @SNEHABHI_UPDATES !**"
    )
    

@Client.on_message(command(["skip", f"skip@SNEHABHI_VIDEOBOT", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):
  
  keyboard = InlineKeyboardMarkup(
    [
      [
        InlineKeyboardButton(
            text="✨ ɢʀᴏᴜᴘ", url=f"https://t.me/SNEHABHI_SERVER"
            ),
        InlineKeyboardButton(
            text="🌻 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/SNEHABHI_UPDATES"
            )
          ]
        ]
      )
      
    chat_id = m.chat.id
    if len(m.command) < 2:
    op = await skip_current_song(chat_id)
    if op == 0:
    await m.reply("❌ 𝙽𝙾𝚃𝙷𝙸𝙽𝙶 𝙸𝚂 𝙲𝚄𝚁𝚁𝙴𝙽𝚃𝙻𝚈 𝙿𝙻𝙰𝚈𝙸𝙽𝙶")
      
