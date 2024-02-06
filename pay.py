from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.types import LabeledPrice, PreCheckoutQuery, CallbackQuery
from config import Payment_Token

dp = Dispatcher()
data = []
users_ids = []


# -------------------------------------------- Start order1 ---------------------------------------------#
async def order1(call: CallbackQuery, bot: Bot):
    await bot.send_invoice(
        chat_id=call.from_user.id,
        title="Uzum Market To'lov Tizimi",
        description="Infinix Hot 30 Play",
        payload="Infinix Hot 30 Play",
        provider_token=Payment_Token,
        currency="uzs",
        prices=[
            LabeledPrice(label="Narxi", amount=160_000_00),
            LabeledPrice(label="QQS", amount=19_200_00),
            LabeledPrice(label="Skidka", amount=-30_200_00)
        ],
        max_tip_amount=10_000_00,
        suggested_tip_amounts=[],
        start_parameter="Infinix_Hot_30_Play",
        provider_data=None,
        photo_url="https://images.uzum.uz/cm1ac11uf2i84h4p9vi0/original.jpg",
        photo_size=100,
        photo_width=1000,
        photo_height=800,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=True,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        request_timeout=15

    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: types.Message, bot: Bot):
    msg = f"""
To'lov muvaffaqiyatli amalga oshirildi ✅
Maxsulot nomi : {message.successful_payment.invoice_payload}
Summa: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
Menejerimiz so'rovingizni oldi va allaqachon sizga termoqda 💻
"""

    await message.answer(msg)
