# DON'T CHANGE THIS FILE 
import asyncio

from driver.snehabhi import bot, call_py

from pytgcalls import idle

async def mulai_bot():

    print("[INFO]: ππ½π΄π·π°π±π·πΈ π±πΎπ πππ°πππΈπ½πΆ")

    await bot.start()

    print("[INFO]: ππ½π΄π·π°π±π·πΈ πΏπΎππ΄ππ΄π³ π±πΎπ πππ°πππΈπ½πΆ")

    await call_py.start()

    await idle()

    print("[INFO]: ππ½π΄π·π°π±π·πΈ πππΎπΏπΏπΈπ½πΆ π±πΎπ")

    await bot.stop()

loop = asyncio.get_event_loop()

loop.run_until_complete(mulai_bot())

print("ππ½π΄π·π°π±π·πΈ ππΈπ³π΄πΎ πΏπ»π°ππ΄π π±πΎπ πΈπ πππ°πππ΄π³")

print("Β―\_(γ)_/Β― π½π΄π΄π³ π·π΄π»πΏ πΉπΎπΈπ½ @SNEHABHI_UPDATES")


