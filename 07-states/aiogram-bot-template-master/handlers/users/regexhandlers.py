from aiogram import types
from aiogram.dispatcher.filters import Regexp

from loader import dp

EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_NUMBER = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
COMMAND_EMAIL_REGEX = r'/email:' + EMAIL_REGEX


@dp.message_handler(Regexp(EMAIL_REGEX))
async def regexp_email(msg: types.Message):
    await msg.answer("Email qabul qilindi")


@dp.message_handler(Regexp(PHONE_NUMBER))
async def regexp_phone(msg: types.Message):
    await msg.answer("Telefone raqami qabul qilindi")


@dp.message_handler(regexp_commands=[COMMAND_EMAIL_REGEX])
async def command_regexp_example(msg: types.Message):
    await msg.answer('Email qabul qilindi')
