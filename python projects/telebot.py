import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from aiogram.fsm.storage.memory import MemoryStorage

# ========== НАСТРОЙКИ ==========
TOKEN = "8401175285:AAE4rWb7kM_c4btSKU7ecQSMfqrarktovpQ"
YOUR_USERNAME = "Ayaz_654"  # Убедись, что это ТВОЙ юзернейм в Telegram!
# ===============================

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# ----- МЕНЮ (клавиатура) -----
def main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🖥️ Портфолио", callback_data="portfolio")],
        [InlineKeyboardButton(text="💰 Услуги и цены", callback_data="services")],
        [InlineKeyboardButton(text="📦 Заказать на Kwork", url="https://kwork.ru/website-development/49072282/sozdam-sovremenniy-sayt-vizitku-lending-na-html-css-js-pod-klyuch")],
        [InlineKeyboardButton(text="💬 Написать мне", url=f"https://t.me/{YOUR_USERNAME}")],
    ])

def back_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад в меню", callback_data="back")]
    ])

def portfolio_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🍔 Бургерная", callback_data="show_burger")],
        [InlineKeyboardButton(text="💪 Фитнес", callback_data="show_fitness")],
        [InlineKeyboardButton(text="🎮 Компьютерный клуб", callback_data="show_cyber")],
        [InlineKeyboardButton(text="📸 Фотостудия", callback_data="show_photo")],
        [InlineKeyboardButton(text="👟 Магазин кроссовок", callback_data="show_kicks")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back")],
    ])

# ----- СТАРТ -----
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Я начинающий веб-разработчик.\n"
        "Я создаю современные сайты на HTML/CSS/JS.\n\n"
        "Выбери, что тебя интересует 👇",
        reply_markup=main_keyboard()
    )

# ----- ПОРТФОЛИО (меню выбора) -----
@dp.callback_query(F.data == "portfolio")
async def portfolio_callback(callback: types.CallbackQuery):
    print("✅ Нажата кнопка ПОРТФОЛИО") # Это для отладки
    await callback.message.edit_text(
        "🖥️ **Мои работы**\n\nВыбери проект, чтобы посмотреть:",
        parse_mode="Markdown",
        reply_markup=portfolio_keyboard()
    )
    await callback.answer()

# ----- ПОКАЗ КАРТИНОК -----
@dp.callback_query(F.data == "show_burger")
async def show_burger(callback: types.CallbackQuery):
    photo = FSInputFile("burger.png")
    await callback.message.answer_photo(
        photo=photo,
        caption="🍔 Бургерная «Bite & Go»\nСтильный лендинг с неоновыми акцентами"
    )
    await callback.answer()

@dp.callback_query(F.data == "show_fitness")
async def show_fitness(callback: types.CallbackQuery):
    photo = FSInputFile("fitness.png")
    await callback.message.answer_photo(
        photo=photo,
        caption="💪 Фитнес-клуб «Titan Fit»\nСовременный сайт для спорта"
    )
    await callback.answer()

@dp.callback_query(F.data == "show_cyber")
async def show_cyber(callback: types.CallbackQuery):
    photo = FSInputFile("cyber.png")
    await callback.message.answer_photo(
        photo=photo,
        caption="🎮 Компьютерный клуб «CYBERSPACE»\nАтмосферный сайт с тёмной темой"
    )
    await callback.answer()

@dp.callback_query(F.data == "show_photo")
async def show_photo(callback: types.CallbackQuery):
    photo = FSInputFile("photo.png")
    await callback.message.answer_photo(
        photo=photo,
        caption="📸 Фотостудия «MOMENT»\nСветлый минималистичный дизайн"
    )
    await callback.answer()

@dp.callback_query(F.data == "show_kicks")
async def show_kicks(callback: types.CallbackQuery):
    photo = FSInputFile("kicks.png")
    await callback.message.answer_photo(
        photo=photo,
        caption="👟 Интернет-магазин «KICKS»\nСтильный e-commerce"
    )
    await callback.answer()

# ----- УСЛУГИ -----
@dp.callback_query(F.data == "services")
async def services_callback(callback: types.CallbackQuery):
    text = (
        "💰 **Услуги и цены**\n\n"
        "▫️ Лендинг / сайт-визитка — **от 1500 ₽**\n"
        "▫️ Многостраничный сайт — **от 3500 ₽**\n"
        "▫️ Интернет-магазин — **от 7000 ₽**\n\n"
        "✅ Что входит:\n"
        "• Адаптивный дизайн\n"
        "• Чистый код HTML/CSS/JavaScript\n"
        "• Современный стиль\n"
        "• Поддержка после сдачи\n\n"
        "⚡️ **Срок:** от 2 до 10 дней"
    )
    await callback.message.edit_text(text, parse_mode="Markdown", reply_markup=back_keyboard())
    await callback.answer()

# ----- НАЗАД -----
@dp.callback_query(F.data == "back")
async def back_callback(callback: types.CallbackQuery):
    print("✅ Нажата кнопка НАЗАД") # Это для отладки
    await callback.message.edit_text(
        "👋 Выбери, что тебя интересует:",
        reply_markup=main_keyboard()
    )
    await callback.answer()

# ----- ЛЮБОЕ СООБЩЕНИЕ -----
@dp.message()
async def any_message(message: types.Message):
    await message.answer(
        "Я понимаю только кнопки 👇",
        reply_markup=main_keyboard()
    )

# ----- ЗАПУСК -----
async def main():
    print("🤖 Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())