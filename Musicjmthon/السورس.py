import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("الأحد", 60 * 60 * 24 * 7),
    ("يوم", 60 * 60 * 24),
    ("الساعة", 60 * 60),
    ("الدقيقة", 60),
    ("الثانيه", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["بنك"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>⇜ بنك/b> `{delta_ping * 1000:.3f} بالثانيه` \n<b>⇜ شغال</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["اعادة تشغيل"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    jmthon = await m.reply("1")
    await jmthon.edit("2")
    await jmthon.edit("3")
    await jmthon.edit("4")
    await jmthon.edit("5")
    await jmthon.edit("6")
    await jmthon.edit("7")
    await jmthon.edit("8")
    await jmthon.edit("9")
    await jmthon.edit("**تم اعادة تشغيل ريناد بنجاح ✓**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["الاوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HEPZ = f"""
- مـرحبا {m.from_user.mention}!

⇜ هُنا اوامر ريناد

- اوامر الاعضاء : 
⇜ {HNDLR}بحث [عنوان المطقع | رابط يوتيوب | الرد على ملف مقطع صوتي] ⇜ لتشغيل مقطع صوتي في المكالمه

⇜ {HNDLR}فيديو [عنوان الفيديو | رابط يوتيوب | الرد على الفيديو] ⇜ لتشغيل فيديو في المكالمة
⇜ {HNDLR}القائمة  ⇜ لعرض قائمة التشغيل الحالية

⇜ {HNDLR}بنك ⇜ لعرض سرعه النت للبوت

⇜ {HNDLR}الاوامر ⇜ لعرض اوامر ريناد

- اوامر المشرفين : 
⇜ {HNDLR}استئناف ⇜ لتكملة الصوت او المقطع الموقف

⇜ {HNDLR}ايقاف ⇜ لايقاف تشغيل الصوت او المقطع موقتا

⇜ {HNDLR}تخطي ⇜ تتخطى الصوت او المقطع وتشغل اللي بعدو

⇜ {HNDLR}انهاء ⇜ لانهاء التشغيل
"""
    await m.reply(HEPZ)


@Client.on_message(filters.command(["السورس"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPZ = f"""
<b>⇜ مرحبا {m.from_user.mention}!

⇜ هذا هو سورس فواز ميوزك

⇜ اختصاص هذا البوت لتشغيل مقاطع صوتية او مقاطع الفيديو في المكالمات الصوتية

⇜ لعرض اوامر السورس ارسل  {HNDLR}الاوامر

⇜ قناه السورس : @kkznk
⇜ قناه البوتات @kkznk</b>
"""
    await m.reply(REPZ, disable_web_page_preview=True)
