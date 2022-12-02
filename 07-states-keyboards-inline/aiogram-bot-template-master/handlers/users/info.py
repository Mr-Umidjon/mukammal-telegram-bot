from aiogram import types

from loader import dp

from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hstrikethrough, hlink


@dp.message_handler(commands='info')
async def bot_info(message: types.Message):
    text = f"Assalomu alaykum, {message.from_user.full_name}!\n"
    text += "Bu " + hbold('qalin matn.\n')
    text += "Bu " + hitalic('egri matn.\n')
    text += "Bu " + hunderline('ostiga chizilgan matn.\n')
    text += "Bu " + hstrikethrough("o'chirilgan matn.\n")
    text += "Bu " + hlink('mail\n', 'mrumidjon2020@gmail.com')
    text += "Bu " + hcode("print('hello world')")

    await message.answer(text)


@dp.message_handler(commands='info_html')
async def bot_info(message: types.Message):
    text = f"Assalomu alaykum, {message.from_user.full_name}!\n"
    text += "Bu <b> qalin matn. </b>\n"
    text += "Bu <i> egri matn </i>\n"
    text += "Bu <u> ostiga chizilgan matn </u>\n"
    text += "Bu <s> o'chirilgan matn </s>\n"
    text += "Bu <a href='mrumidjon2020@gmail.com'> mail </a>\n"
    text += "Bu <code> print('hello world') </code> kod.\n"

    await message.answer(text)


@dp.message_handler(commands='info_markdown')
async def bot_info(message: types.Message):
    text = f"Assalomu alaykum, {message.from_user.full_name}\!\n"
    text += "Bu * qalin matn\. *\n"
    text += "Bu _ egri matn _\n"
    text += "Bu __ ostiga chizilgan matn __\n"
    text += "Bu ~ o'chirilgan matn ~\n"
    text += "Bu [mail](mrumidjon2020@gmail.com)\n"
    text += "Bu `print('hello world')` kod\.\n"

    await message.answer(text, parse_mode=types.ParseMode.MARKDOWN_V2)
