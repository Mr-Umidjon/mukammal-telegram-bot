from aiogram import types
from aiogram.types import LabeledPrice

from ..utils.misc.product import Product

ds_praktikum = Product(
    title="Data Science va Sun'iy intellekt",
    description="Kursga to'lov qilish uchun quyidagi tugmani bosing.",
    currency='UZS',
    prices=[
        LabeledPrice(
            label='Praktikum',
            amount=15000,  # 15.00$
        ),
        LabeledPrice(
            label='Chegirma',
            amount=-1000,
        )
    ],
    start_parameter='create_invoice_ds_praktikum',
    photo_url='https://i.imgur.com/vRN7PBT.jpg',
    photo_width=1280,
    photo_height=564,
    need_email=True,
    need_name=True,
    need_phone_number=True,
)

python_book = Product(
    title="Pythonda Dasturlash Asoslari",
    description="Kitobga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Kitob",
            amount=5000,
        ),
        LabeledPrice(
            label='Yetkazib berish (7 kun)',
            amount=100,
        ),
    ],
    start_parameter="create_invoice_python_book",
    photo_url='https://i.imgur.com/0IvPPun.jpg',
    photo_width=851,
    photo_height=1280,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True,
)
