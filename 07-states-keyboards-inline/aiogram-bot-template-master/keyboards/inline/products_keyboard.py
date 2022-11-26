from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import course_callback, book_callback

category_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='💻 Kurslar', callback_data="courses"),
            InlineKeyboardButton(text='📚 Kitoblar', callback_data="books"),
        ],
        [
            InlineKeyboardButton(text='🔗 Mohirdev sahifasiga o\'tish', url="https://mohirdev.uz/courses/telegram"),
        ],
        [
            InlineKeyboardButton(text='🔍 Qidirish', switch_inline_query_current_chat='')
        ],
        [
            InlineKeyboardButton(text='✉️Ulashish', switch_inline_query='Zo\'r bot ekan')
        ],
    ],
)

# Kurslar uchun keyboard

courses_menu = InlineKeyboardMarkup(row_width=1)

python = InlineKeyboardButton(text='🐍 Python Dasturlash Asoslari',
                              callback_data=course_callback.new(item_name="python"))
courses_menu.insert(python)

django = InlineKeyboardButton(text='🌐 Django Web Dasturlash', callback_data=course_callback.new(item_name='django'))
courses_menu.insert(django)

telegram = InlineKeyboardButton(text='🤖 Mukammal Telegram bot', callback_data="course:telegram")
courses_menu.insert(telegram)

algorithm = InlineKeyboardButton(text='📈 Ma\'lumotlar Tuzilmasi va Algoritmlar', callback_data='course:algorithm')
courses_menu.insert(algorithm)

back_button = InlineKeyboardButton(text='🔙 Ortga', callback_data='cancel')
courses_menu.insert(back_button)

# 3 - usul

books = {
    "Python. Dasturlash asoslari": "python_book",
    "C++. Dasturlash tili": "cpp_book",
    "Mukammal Dasturlash. JavaScript": "js_book",
}

books_menu = InlineKeyboardMarkup(row_width=1)

for key, value in books.items():
    books_menu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
books_menu.insert(back_button)

# Har bir kurs uchun tugma
telegram_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Xarid qilish", url="https://mohirdev.uz/courses/telegram/")
    ]
])

algorithm_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ko'rish", url="https://mohirdev.uz/courses/algoritmlar/")
    ]
])
