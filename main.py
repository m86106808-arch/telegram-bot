import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = "8960819152:AAFM81loiEQhlbfc20tUwLdJE-Z65nq-qTM"
ADMIN_ID = 52504489

async def start(update: Update, context):
    user = update.effective_user
    await update.message.reply_text(f"أهلاً بك يا {user.first_name}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
