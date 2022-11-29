from aiogram import types

from loader import dp

import wikipedia

wikipedia.set_lang('uz')


# Echo bot
@dp.message_handler(state=None)
async def send_wiki(message: types.Message):
    print(message.chat.id)
    try:
        response = wikipedia.summary(message.text)
        if len(response) > 4095:
            for x in range(0, len(response), 4095):
                await message.answer(response[x:x + 4095])
        else:
            await message.answer(response)
    except:
        await message.answer("Bu mavzuga oid maqola yo'q")
