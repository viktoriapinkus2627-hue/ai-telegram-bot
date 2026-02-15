import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен бота из переменных среды Render
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Название PDF-файла в папке с ботом
PDF_FILE = "AI_Guide.pdf"

# Главное меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("AI Инструменты", callback_data="tools")],
        [InlineKeyboardButton("Обучение", callback_data="learn")],
        [InlineKeyboardButton("Челленджи", callback_data="challenge")],
        [InlineKeyboardButton("Мои PDF", callback_data="pdf")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Я ViktoriaBot 🚀 Выберите действие:", reply_markup=reply_markup)

# Обработка кнопок
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "tools":
        await query.edit_message_text("Вот список AI инструментов:\n1. ChatGPT\n2. MidJourney\n3. DALL·E")
    elif query.data == "learn":
        await query.edit_message_text("Материалы для обучения:\n- Мини-гайды\n- Видео уроки\n- Шаблоны")
    elif query.data == "challenge":
        await query.edit_message_text("Челленджи:\n- Попробуй сделать 3 AI-поста\n- Получи фидбек от бота")
    elif query.data == "pdf":
        chat_id = query.message.chat.id
        await context.bot.send_document(chat_id=chat_id, document=open(PDF_FILE, "rb"))

# Запуск бота
if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()
