import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Берём токен из переменной окружения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [
        [InlineKeyboardButton("🍲 Рецепт дня", callback_data="recipe")]
    ]
    reply_markup = InlineKeyboardMarkup(kb)
    await update.message.reply_text(
        "👨‍🍳 Привет! Я шеф-повар бот. Нажми кнопку ниже, чтобы получить рецепт дня:",
        reply_markup=reply_markup
    )

# Обработчик кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "recipe":
        await query.edit_message_text("🥗 Рецепт дня:\n\nОвощной салат с оливковым маслом 🥒🍅")

# Запуск бота
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()

if __name__ == "__main__":
    main()
