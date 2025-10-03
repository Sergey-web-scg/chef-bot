import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# токен берём из переменной окружения на Render
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[InlineKeyboardButton("🍲 Рецепт дня", callback_data="recipe")]]
    reply_markup = InlineKeyboardMarkup(kb)
    await update.message.reply_text("👨‍🍳 Привет! Я — твой AI-шеф. Хочешь рецепт?", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "recipe":
        await query.edit_message_text(
            "🥗 Рецепт дня:\n\nОвощное рагу с курицей:\n- курица 300г\n- картофель 2шт\n- морковь 1шт\n- лук 1шт\nТушить всё 30 минут."
        )

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
