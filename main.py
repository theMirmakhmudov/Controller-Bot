import asyncio
import logging
from aiogram import Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, and_f
from config import TOKEN
import handlers
from aiogram import Bot

dp = Dispatcher()


async def main() -> None:
    dp.startup.register(handlers.start_up)
    dp.shutdown.register(handlers.on_shutdown)
    dp.message.register(handlers.cmd_start, Command("start"))
    dp.message.register(handlers.new_chat_member_answer,
                        and_f(F.chat.type == "group" or F.chat.type == "supergroup", F.new_chat_members))
    dp.message.register(handlers.left_chat_member_answer,
                        and_f(F.chat.type == "group" or F.chat.type == "supergroup", F.left_chat_member))
    dp.message.register(handlers.mute_member_answer,
                        and_f(F.chat.type == "supergroup", and_f(F.text == "/mute", F.reply_to_message)))
    dp.message.register(handlers.unmute_member_answer,
                        and_f(F.chat.type == "supergroup", and_f(F.text == "/unmute", F.reply_to_message)))
    dp.message.register(handlers.ban_member_answer,
                        and_f(F.chat.type == "supergroup", and_f(F.text == "/ban", F.reply_to_message)))
    dp.message.register(handlers.unban_member_answer,
                        and_f(F.chat.type == "supergroup", and_f(F.text == "/unban", F.reply_to_message)))
    dp.message.register(handlers.deleted_messages,
                        and_f(F.chat.type == "supergroup", and_f(F.text == "/delete", F.reply_to_message)))
    dp.message.register(handlers.get_channel_id, and_f(F.text == "/id"))

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
