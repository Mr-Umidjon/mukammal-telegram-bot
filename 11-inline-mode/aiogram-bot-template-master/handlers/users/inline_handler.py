from aiogram import types
from loader import dp


@dp.inline_handler()
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="kurs001",
                title='Dasturlash asoslari. Python',
                input_message_content=types.InputTextMessageContent(
                    message_text='Dars link: https://mohirdev.uz/courses/python/',
                ),
                url='https://mohirdev.uz/courses/python/',
                thumb_url='https://yt3.googleusercontent.com/ytc/AMLnZu_rEY9N8jGS2eV7EEKCEMRbpKtJZ7Wa1GVjNIq_=s176-c-k-c0x00ffffff-no-rj',
                description="Darsimizning asl maqsadi tinglovchilarga dasturlash asoslarini va eng muhimi turli muammolarga yechim bo’luvchi dasturlar yozishni o’rgatish."
            ),
            types.InlineQueryResultArticle(
                id="kurs002",
                title='Mukammal Telegram Bot',
                input_message_content=types.InputTextMessageContent(
                    message_text='Dars uchun link: https://mohirdev.uz/courses/telegram',
                ),
                url="https://mohirdev.uz/courses/telegram",
                thumb_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Anvar-aka-python.png",
                description="Python dasturlash tilida Mukammal telegram bot yozishni o'rganamiz",
            ),
            types.InlineQueryResultArticle(
                id="kurs003",
                title="Ma'lumotlar Tuzilmasi va Algoritmlar",
                input_message_content=types.InputTextMessageContent(
                    message_text="Dars uchun link: https://mohirdev.uz/courses/algoritmlar",
                ),
                url="https://mohirdev.uz/courses/algoritmlar",
                thumb_url="https://i0.wp.com/mohirdev.uz/wp-content/uploads/ALGORITMLAR.png",
                description="Har bir dasturchi bilishi muhim bo'lgan eng dolzarb kurs.",
            ),
            types.InlineQueryResultArticle(
                id="kurs004",
                title="Python Django Web dasturlash",
                input_message_content=types.InputTextMessageContent(
                    message_text="Dars uchun link: https://mohirdev.uz/courses/django",
                ),
                url="https://mohirdev.uz/courses/django",
                thumb_url="https://i0.wp.com/mohirdev.uz/wp-content/uploads/photo1627374915.jpeg",
                description="Django frameworkida Web dasturlar yaratishni o'rganamiz",
            ),

        ]
    )
