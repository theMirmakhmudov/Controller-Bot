import asyncio
import logging
from aiogram import Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, and_f
from aiogram.types import Message
from config import TOKEN, Channel
import handlers
from aiogram import Bot

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Salom !")


async def main() -> None:
    dp.startup.register(handlers.start_up)
    dp.shutdown.register(handlers.on_shutdown)
    dp.message.register(handlers.new_chat_member_answer, and_f(F.chat.id == Channel, F.new_chat_members))
    dp.message.register(handlers.left_chat_member_answer, and_f(F.chat.id == Channel, F.left_chat_member))
    dp.message.register(handlers.mute_member_answer, and_f(F.chat.type == "supergroup", and_f(F.text == "/mute", F.reply_to_message)))
    dp.message.register(handlers.unmute_member_answer, and_f(F.chat.type == "supergroup", and_f(F.text == "/unmute", F.reply_to_message)))
    dp.message.register(handlers.ban_member_answer, and_f(F.chat.type == "supergroup", and_f(F.text == "/ban", F.reply_to_message)))
    dp.message.register(handlers.unban_member_answer, and_f(F.chat.type == "supergroup", and_f(F.text == "/unban", F.reply_to_message)))

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

    if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
