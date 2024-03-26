from aiogram import types
from config import Admin
from aiogram import Bot
from aiogram.types import ChatPermissions
from datetime import timedelta, datetime


async def start_up(bot: Bot) -> None:
    await bot.send_message(Admin, "Bot ishga tushdi ✅")


async def on_shutdown(bot: Bot) -> None:
    await bot.send_message(Admin, "Bot ishdan to'xtadi ❌")


async def new_chat_member_answer(message: types.Message):
    for new_chat_member in message.new_chat_members:
        await message.answer(f"Assalomu Aleykum, {new_chat_member.mention_html()}")

        await message.delete()


async def left_chat_member_answer(message: types.Message):
    await message.answer(f"Hayir, {message.left_chat_member.mention_html()}")

    await message.delete()


async def mute_member_answer(message: types.Message):
    user_id = message.reply_to_message.from_user.id
    permissions = ChatPermissions(can_send_messages=False)
    await message.chat.restrict(user_id, permissions)
    await message.answer_photo(
        "https://media.istockphoto.com/id/1305893663/vector/silent-sound-off-icon-vector-for-your-web-design-logo-ui-illustration.jpg?s=612x612&w=0&k=20&c=czrINWt2weKC3fLHU3KqI2eZBFdwhOuuCZxS5JNGpSU=",
        f"{message.reply_to_message.from_user.mention_html()} yozishdan maxrum qilindi ❗️")


async def unmute_member_answer(message: types.Message):
    user_id = message.reply_to_message.from_user.id
    permissions = ChatPermissions(can_send_messages=True)
    await message.chat.restrict(user_id, permissions)
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlPQKfIi9UUnwcNasWrtRXuZGvu1pUq1_XRw&usqp=CAU",
                               f"✅{message.reply_to_message.from_user.mention_html()} endi yoza olasiz!")


async def ban_member_answer(message: types.Message):
    user_id = message.reply_to_message.from_user.id
    await message.chat.ban_sender_chat(user_id)
    await message.answer(f"{message.reply_to_message.from_user.mention_html()} siz ban oldingiz!")


async def unban_member_answer(message: types.Message):
    user_id = message.reply_to_message.from_user.id
    await message.chat.unban_sender_chat(user_id)
    await message.answer(f"{message.reply_to_message.from_user.mention_html()} siz bandan olindingiz!")
