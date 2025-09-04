from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# توكن البوت من BotFather
TOKEN = "8076498045:AAFMiYGB1p2dCM5H_-WW2Lm3W0ZDJQo5BR4"

# دالة /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 أهلاً! أنا شغال من GitHub.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ البوت شغال...")
    app.run_polling()

if __name__ == "__main__":
    main()
