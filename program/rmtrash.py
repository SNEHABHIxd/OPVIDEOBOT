import os

from pyrogram import Client, filters

from pyrogram.types import Message

from driver.filters import command, other_filters

from driver.decorators import sudo_users_only, errors

downloads = os.path.realpath("program/downloads")

raw = os.path.realpath(".")

@Client.on_message(command(["rmd", "clear"]) & ~filters.edited)

@errors

@sudo_users_only

async def clear_downloads(_, message: Message):

    ls_dir = os.listdir(downloads)

    if ls_dir:

        for file in os.listdir(downloads):

            os.remove(os.path.join(downloads, file))

        await message.reply_text("β **π³π΄π»π΄ππ΄π³ π°π»π» π³πΎππ½π»πΎπ°π³π΄π³ π΅πΈπ»π΄π**")

    else:

        await message.reply_text("β **π½πΎ π΅πΈπ»π΄ π³πΎππ½π»πΎπ°π³π΄π³**")

        

@Client.on_message(command(["rmw", "clean"]) & ~filters.edited)

@errors

@sudo_users_only

async def clear_raw(_, message: Message):

    ls_dir = os.listdir(raw)

    if ls_dir:

        for file in os.listdir(raw):

            if file.endswith('.raw'):

                os.remove(os.path.join(raw, file))

        await message.reply_text("β **π³π΄π»π΄ππ΄π³ π°π»π» ππ°π π΅πΈπ»π΄π**")

    else:

        await message.reply_text("β **π½πΎ ππ°π π΅πΈπ»π΄π**")

@Client.on_message(command(["cleanup"]) & ~filters.edited)

@errors

@sudo_users_only

async def cleanup(_, message: Message):

    pth = os.path.realpath(".")

    ls_dir = os.listdir(pth)

    if ls_dir:

        for dta in os.listdir(pth):

            os.system("rm -rf *.raw *.jpg")

        await message.reply_text("β **π²π»π΄π°π½π΄π³**")

    else:

        await message.reply_text("β **π°π»ππ΄π°π³π π²π»π΄π°π½π΄π³**")
