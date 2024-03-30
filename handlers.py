from aiogram import types
from aiogram import Bot
from aiogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
import time
from config import Admin, TOKEN

add_group = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Guruhga qo'shish", url="http://t.me/PDPYordamchi_bot?startgroup=start")]
])


async def start_up(bot: Bot) -> None:
    await bot.send_message(Admin, "Bot ishga tushdi ✅")


async def on_shutdown(bot: Bot) -> None:
    await bot.send_message(Admin, "Bot ishdan to'xtadi ❌")


async def cmd_start(message: types.Message, bot: Bot):
    bot_user = await bot.get_chat_member(message.chat.id, TOKEN.split(":")[0])

    await message.answer(f"""<b>
Assalomu Alaykum {message.from_user.mention_html()} ❗️
        
👮🏻‍♂️ Men guruhingizga qo'shilgan odamlar bilan salomlashaman va guruhni boshqarishda yordam beraman ✅

❗️Guruhingizda muammosiz ishlashim uchun adminlik xuquqini bering!

🤖 {bot_user.user.mention_html()}
</b>""", reply_markup=add_group)


async def new_chat_member_answer(message: types.Message, bot: Bot):
    await message.delete()
    for new_chat_member in message.new_chat_members:
        mes = await message.answer_photo(
            "https://thumbor.forbes.com/thumbor/fit-in/900x510/https://www.forbes.com/advisor/wp-content/uploads/2023/07/computer-coding.jpg",
            f"<b>Assalomu Aleykum, {new_chat_member.mention_html()}\nGuruhimizga Xush kelibsiz 🎉</b>")

        time.sleep(20)
        await bot.delete_message(chat_id=message.chat.id, message_id=mes.message_id)


async def left_chat_member_answer(message: types.Message, bot: Bot):
    await message.delete()
    mes = await message.answer_photo(
        "https://image.shutterstock.com/image-vector/3d-isometric-flat-vector-conceptual-260nw-2373700103.jpg",
        f"<b>Xayir, {message.left_chat_member.mention_html()}</b>")

    time.sleep(20)
    await bot.delete_message(chat_id=message.chat.id, message_id=mes.message_id)


async def mute_member_answer(message: types.Message, bot: Bot):
    try:
        user_status = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        if user_status.status == "creator" or user_status.status == "administrator":
            user_id = message.reply_to_message.from_user.id
            permissions = ChatPermissions(can_send_messages=False)
            await message.chat.restrict(user_id, permissions)
            mes1 = await message.answer_photo(
                "https://businesswired.files.wordpress.com/2014/05/twitter-mute-lo-res.jpg",
                f"<b>{message.reply_to_message.from_user.mention_html()} yozishdan maxrum qilindi ❗️</b>")

            time.sleep(20)
            await bot.delete_message(chat_id=message.chat.id, message_id=mes1.message_id)
        else:
            mes2 = await message.answer("<b>You're not Admin ❌</b>")
            await bot.delete_message(chat_id=message.chat.id, message_id=mes2.message_id)
    except:
        await message.answer("<b>Siz Adminni mute qila olmaysiz ❌</b>")


async def unmute_member_answer(message: types.Message, bot: Bot):
    user_status = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    if user_status.status == "creator" or user_status.status == "administrator":
        user_id = message.reply_to_message.from_user.id
        permissions = ChatPermissions(can_send_messages=True)
        await message.chat.restrict(user_id, permissions)
        mes1 = await message.answer_photo(
            "https://img.freepik.com/free-photo/young-bearded-man-with-striped-shirt_273609-5677.jpg",
            f"<b>✅{message.reply_to_message.from_user.mention_html()} endi yoza olasiz ❗️️</b>")

        time.sleep(20)
        await bot.delete_message(chat_id=message.chat.id, message_id=mes1.message_id)
    else:
        mes2 = await message.answer("<b>You're not Admin ❌</b>")
        await bot.delete_message(chat_id=message.chat.id, message_id=mes2.message_id)


async def deleted_messages(message: types.Message, bot: Bot):
    user_status = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    if user_status.status == "creator" or user_status.status == "administrator":
        mes = message.reply_to_message.message_id
        await bot.delete_message(chat_id=message.chat.id, message_id=mes, request_timeout=15)
        await message.delete()
    else:
        mes = await message.answer("<b>You're not Admin ❌</b>")
        await bot.delete_message(chat_id=message.chat.id, message_id=mes.message_id)


async def get_channel_id(message: types.Message):
    await message.answer(f"<b>This chat's ID is: </b><code>{message.chat.id}</code>")


async def ban_member_answer(message: types.Message, bot: Bot):
    try:
        user_status = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        if user_status.status == "creator" or user_status.status == "administrator":
            user_id = message.reply_to_message.from_user.id
            await message.chat.ban_sender_chat(user_id)
            mes = await message.answer(
                f"<b>{message.reply_to_message.from_user.mention_html()} guruhdan chetlashtirildi ❗️</b>")
            time.sleep(20)
            await bot.delete_message(chat_id=message.chat.id, message_id=mes.message_id)

        else:
            mes2 = await message.answer("You're not Admin ❌")
            await bot.delete_message(chat_id=message.chat.id, message_id=mes2.message_id)

    except:
        await message.answer("<b>Siz adminga ban bera olmaysiz ❌</b>")


async def unban_member_answer(message: types.Message, bot: Bot):
    user_status = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    if user_status.status == "creator" or user_status.status == "administrator":
        user_id = message.reply_to_message.from_user.id
        await message.chat.unban_sender_chat(user_id)
        mes = await message.answer(
            f"<b>{message.reply_to_message.from_user.mention_html()} guruhga qayta qo'shilish uchun ruxsat berildi ❗️</b>")

        time.sleep(20)
        await bot.delete_message(chat_id=message.chat.id, message_id=mes.message_id)

    else:
        mes2 = await message.answer("You're not Admin ❌")
        await bot.delete_message(chat_id=message.chat_id, message_id=mes2.message_id)
