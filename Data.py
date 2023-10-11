from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("بـدء استـخراج الجلسـة 🖥️", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="رجـوع 🔙", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "𝗛𝗨𝗡𝗧𝗘𝗥𝗧𝗛𝗢𝗡 - سـورس هانترثـون 🌐", url="https://t.me/HunerThon"
            )
        ],
        [
            InlineKeyboardButton("كيفيـة الاستـخدام   ⍰ ", callback_data="help"),
            InlineKeyboardButton("حـول البـوت ℹ️", callback_data="about"),
        ],
        [InlineKeyboardButton("المطـور 👷", url="https://t.me/Y_H_E")],
    ]

    START = """
**⎆ مـرحبـًا** {}
**⎆ اضغـط عـلى بـدء استخـراج الجلسـة لبـدء الاستـخراج**
**⎆ أنـا بوت استـخراج كـود تيرمكـس وبايروجـرام لـ تنصيـب @HunerThon**
**⎆ هـذا الكـود خـطير جدًا لا تشاركـه لأحد .**
    """

    HELP = """
**أوامـر البـوت ⎙**
━━━━━━━━━━━━━━━━━
/about - لحول البوت ℹ️
/help - لمساعدتك ❓
/start - لبدء البوت ❗
/repo - لعرض معلومـات عـن السـورس 💡
/generate - لاستخراج الجلسات 👷
/cancel - لإلغاء الاستخراج 🥀
/restart - لترسيت البـوت ♻️
"""

    # About Message
    ABOUT = """
**حـول البـوت ⍰**

**هـذا البوت تـم تشـغيله بواسطـة 𝗛𝗨𝗡𝗧𝗘𝗥𝗧𝗛𝗢𝗡 و المـطور @Y_H_E**

قنـاة السـورس 🖥️ : [𝗦𝗼𝘂𝗿𝗰𝗲 𝗛𝗨𝗡𝗧𝗘𝗥𝗧𝗛𝗢𝗡](https://t.me/HunerThon)
لغـة البرمجـة ℹ️ : [بـايروجرام](docs.pyrogram.org)
اللغـة 🌐 : [بايثون](www.python.org)
المـطور 👷 : @Y_H_E
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
**سـورس هانترثـون - 𝗛𝗨𝗡𝗧𝗘𝗥𝗧𝗛𝗢𝗡 **
**لا تنسـى الصـلاة على النبي 🤍 .**
┏━━━━━━━━━━━━━━━━━┓
⎆ سـورس هانترثـون - 𝗛𝗨𝗡𝗧𝗘𝗥𝗧𝗛𝗢𝗡 . [اضـغط هـنا ❗](https://t.me/HunerThon)
⎆ المطـور : [اضـغط هـنا ❗](https://t.me/Y_H_E)
⎆ شـروحـات السـورس ℹ️ [اضـغط هـنا ❗](https://t.me/HunerThon)
┗━━━━━━━━━━━━━━━━━┛ 
**تابـع لـ - 𝗛𝗨𝗡𝗧𝗘𝗥𝗧𝗛𝗢𝗡 🌐**
   """
