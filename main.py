import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from config import *
from aiogram.enums.parse_mode import ParseMode
from buttons import keyboard
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.types import FSInputFile
from pay import pre_checkout_query, successful_payment, order1


bot = Bot(token=Token, parse_mode=ParseMode.HTML)

dp = Dispatcher()


async def on_startup(bot: Bot):
    await bot.send_message(Admins, "Bot ishga tushdi!")


async def on_shutdown(bot: Bot):
    await bot.send_message(Admins, "Bot ishdan to'xtadi!")


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer_photo("https://frankfurt.apollo.olxcdn.com/v1/files/7w6ymhm2lvxu3-UZ/image",
                               caption=f"Assalomu Aleykum. Xurmatli {message.from_user.full_name}! \n<b>UZUM MARKET</b> botimizga xush kelibsiz 👋",
                               reply_markup=keyboard)


@dp.message(F.text == "Telefonlar")
async def cmd_phones(message: types.Message):
    album_builder = MediaGroupBuilder(
        caption="<b>Nomi: Infinix Hot 30 Play 📱\nXotira: 16/128 GB 💾\nNarxi: 1,679,000 UZS</b> 💸")
    album_builder.add(
        type="photo",
        media=FSInputFile("images/photo1.jpg"))
    album_builder.add(
        type="photo",
        media=FSInputFile("images/photo2.jpg"))
    album_builder.add(
        type="photo",
        media=FSInputFile("images/photo3.jpg"))
    album_builder.add(
        type="photo",
        media=FSInputFile("images/photo4.jpg"))

    await message.answer_media_group(media=album_builder.build())
    await message.answer_poll("Olasizmi", ["ha", "yo'q", "bilmadim"],reply_markup=keyboard)


dp.callback_query.register(order1, F.data == "Infinix")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


async def main():
    await dp.start_polling(bot)
    dp.startup.register(on_startup)
    dp.message.register(cmd_start)
    dp.shutdown.register(on_shutdown)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
