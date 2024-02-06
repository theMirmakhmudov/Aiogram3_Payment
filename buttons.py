from aiogram import types

btn = [
    [types.KeyboardButton(text="Telefonlar"), types.KeyboardButton(text="Aksusuarlar")]
]

keyboard = types.ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True, input_field_placeholder="Tanlang:")
