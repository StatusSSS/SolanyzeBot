import os

from fastapi import Request, FastAPI
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes



TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


bot = Bot(token=TELEGRAM_BOT_TOKEN)
telegram_app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Send Solana wallet address")



telegram_app.add_handler(CommandHandler("start", start_command))

fast_api = FastAPI()

@fast_api.get("/")
async def root(request: Request):
    return {"message": "Hello World"}


@fast_api.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, bot)

    if not bot._initialized:
        await bot.initialize()

    if not telegram_app.running:
        await telegram_app.initialize()

    await telegram_app.process_update(update)

    return {"ok": True}