import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = "8960819152:AAFM81loiEQhlbfc20tUwLdJE-Z65nq-qTM"
ADMIN_ID = 52504489

async def start(update: Update, context):
    user = update.effective_user
    welcome_text = f"أهلاً بك يا {user.first_name} في البوت!"
    await update.message.reply_text(welcome_text)
    
    admin_notice = f"🔔 دخول جديد للبوت!\nالاسم: {user.first_name}\nالايدي: {user.id}"
    try:
        await context.bot.send_message(chat_id=ADMIN_ID, text=admin_notice)
    except Exception as e:
        print(e)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
