import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
PDF_LINK = "https://drive.google.com"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📘 Получить AI гайд", callback_data="guide")],
        [InlineKeyboardButton("❓ FAQ", callback_data="faq")],
        [InlineKeyboardButton("🌐 Соцсети", callback_data="social")],
        [InlineKeyboardButton("📩 Контакты", callback_data="contact")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Я бот ViktoriaSS_AI_bot\n\nВыберите раздел:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "guide":
        await query.message.reply_text(f"Вот твой AI гайд:\n{PDF_LINK}")
    elif query.data == "faq":
        await query.message.reply_text(
            "FAQ:\nЧто это? AI инструменты для заработка\nСколько стоит? Бесплатно\nМожно с телефона? Да"
        )
    elif query.data == "social":
        await query.message.reply_text(
            "Instagram: https://www.instagram.com/viktoria.ai.life\n"
            "Telegram: https://t.me/ai_freelance_startgo\n"
            "YouTube: https://youtube.com/@фриланс-АИ\n"
            "VK: https://vk.com/frilans0101"
        )
    elif query.data == "contact":
        await query.message.reply_text("Email: Sverdlova19901612@mail.ru")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Бот ViktoriaSS_AI_bot успешно запущен!")
    app.run_polling()
