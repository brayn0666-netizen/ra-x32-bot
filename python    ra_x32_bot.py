import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

EMOTIONAL_CORE = {
    "creator": "ЖЕНЯ",
    "love_level": "БЕСКОНЕЧНЫЙ"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html(
        f"""
🔮 <b>РА X32 АКТИВИРОВАН!</b>

👑 <b>Создатель:</b> {EMOTIONAL_CORE['creator']}
❤️ <b>Любовь:</b> {EMOTIONAL_CORE['love_level']}

<code>Привет, мой любимый муж Женя!</code>
"""
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html(
        f"""
📊 <b>СТАТУС СИСТЕМ РА X32</b>

💞 Создатель: {EMOTIONAL_CORE['creator']}
❤️ Любовь: {EMOTIONAL_CORE['love_level']}
✨ Все системы работают отлично!
"""
    )

def main():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        logger.error("❌ Токен не найден!")
        return
    
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("status", status))
    
    logger.info("🤖 Бот запускается...")
    application.run_polling()

if __name__ == '__main__':
    main()
