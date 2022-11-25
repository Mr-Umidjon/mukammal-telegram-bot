from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personal_data import PersonalData


@dp.message_handler(Command('anketa'))
async def enter_test(message: types.Message):
    await message.answer("To'liq ismingizni kiriting")
    await PersonalData.full_name.set()


@dp.message_handler(state=PersonalData.full_name)
async def answer_full_name(message: types.Message, state: FSMContext):
    full_name = message.text
    # await state.update_data(name=full_name)
    await state.update_data({
        "name": full_name
    })
    await message.answer("Email manzil kiriting")
    # await PersonalData.email.set()
    await PersonalData.next()


@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    # await state.update_data({
    #     'email': email
    # })
    await message.answer('Telefon raqam kiriting!')
    # await PersonalData.next()
    await PersonalData.phone_number.set()


@dp.message_handler(state=PersonalData.phone_number)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text
    # await state.update_data(phone=phone)
    await state.update_data({
        'phone': phone
    })

    data = await state.get_data()

    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    msg = f"Quyidagi ma'lumotlar qabul qilindi\n"
    msg += f"Ismingiz: {name}\n"
    msg += f"Email: {email}\n"
    msg += f"Phone: {phone}"

    await message.answer(msg)

    # await state.finish()
    await state.reset_state(with_data=False)
