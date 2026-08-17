import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "8960819152:AAFM81loiEQhlbfc20tUwLdJE-Z65nq-qTM"

bot_is_active = True

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"أهلاً بك يا {user.first_name} في البوت!\nحالة البوت الآن: مفعل ✅")

async def turn_on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global bot_is_active
    bot_is_active = True
    await update.message.reply_text("تم تفعيل البوت وتشغيله بنجاح! 🟢")

async def turn_off(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global bot_is_active
    bot_is_active = False
    await update.message.reply_text("تم إيقاف البوت مؤقتاً! 🔴")

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global bot_is_active
    if not bot_is_active:
        return  
    
    user_text = update.message.text
    await update.message.reply_text(f"أنت قلت: {user_text}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("on", turn_on))
    app.add_handler(CommandHandler("off", turn_off))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_messages))

    app.run_polling()

if __name__ == "__main__":
    main()
