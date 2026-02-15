import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

PDF_LINK = "https://drive.google.com"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📘 Получить AI гайд", callback_data="guide")],
        [InlineKeyboardButton("❓ FAQ", callback_data="faq")],
        [InlineKeyboardButton("🌐 Соцсети", callback_data="social")],
        [InlineKeyboardButton("📩 Контакты", callback_data="contact")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет! Я бот ViktoriaSS_AI_bot\n\nВыберите нужный раздел:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "guide":
        await query.message.reply_text(
            "Вот твой AI гайд:\n" + PDF_LINK
        )

    elif query.data == "faq":
        await query.message.reply_text(
            "FAQ:\n\n"
            "Что это?\nAI инструменты для заработка\n\n"
            "Сколько стоит?\nБесплатно\n\n"
            "Можно с телефона?\nДа"
        )

    elif query.data == "social":
        await query.message.reply_text(
            "Instagram:\n"
            "https://www.instagram.com/viktoria.ai.life\n\n"
            "Telegram:\n"
            "https://t.me/ai_freelance_startgo\n\n"
            "YouTube:\n"
            "https://youtube.com/@фриланс-АИ\n\n"
            "VK:\n"
            "https://vk.com/frilans0101"
        )

    elif query.data == "contact":
        await query.message.reply_text(
            "Email:\n"
            "Sverdlova19901612@mail.ru"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Бот ViktoriaSS_AI_bot успешно запущен!")

app.run_polling()
