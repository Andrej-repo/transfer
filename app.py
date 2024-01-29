import asyncio
import logging
from aiogram import Bot, Dispatcher
import handlers
from config import config

bot = Bot(token=config.tg_bot_token.get_secret_value())
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

async def main():

    dp.include_router(handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())