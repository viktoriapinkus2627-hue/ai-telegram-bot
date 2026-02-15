import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
PDF_FILE = "AI_Guide.pdf"

# Главное меню
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

# Обработка кнопок
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "guide":
        chat_id = query.message.chat.id
        await context.bot.send_document(chat_id=chat_id, document=open(PDF_FILE, "rb"))
    elif query.data == "faq":
        await query.edit_message_text(
            "FAQ:\n\n"
            "Что это?\nAI инструменты для заработка\n\n"
            "Сколько стоит?\nБесплатно\n\n"
            "Можно с телефона?\nДа"
        )
    elif query.data == "social":
        await query.edit_message_text(
            "Instagram:\nhttps://www.instagram.com/viktoria.ai.life\n\n"
            "Telegram:\nhttps://t.me/ai_freelance_startgo\n\n"
            "YouTube:\nhttps://youtube.com/@фриланс-АИ\n\n"
            "VK:\nhttps://vk.com/frilans0101"
        )
    elif query.data == "contact":
        await query.edit_message_text(
            "Email:\nSverdlova19901612@mail.ru"
        )

# Асинхронный запуск бота
async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
