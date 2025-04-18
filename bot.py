from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

BOT_TOKEN ='7478792333:AAFjhCBd0fIawfpLI4UNGEmseazqMY7bN6w'
CHANNEL_USERNAME = '@Persian_Deaf'  # آی‌دی کانال خودت بدون فاصله

# ویدیوی تست - جایگزین کن با FILE_ID واقعی یا لینک تلگرام
VIDEO_FILE_ID = 'اhttps://t.me/persian_deaf/152'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat_member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user.id)

    if chat_member.status in ['member', 'administrator', 'creator']:
        await update.message.reply_text("عالی! شما عضو کانال هستید.")
        await update.message.reply_video(video=VIDEO_FILE_ID, caption="اینجا ویدیوی درخواستی شماست.")
    else:
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("عضویت در کانال", url=f"https://t.me/{persian_deaf[1:]}")],
             [InlineKeyboardButton("✅ عضویت انجام شد", callback_data="check_membership")]]
        )
        await update.message.reply_text(
            "برای دریافت ویدیو، ابتدا باید در کانال عضو شوید.",
            reply_markup=keyboard
        )

async def check_membership(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user
    chat_member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user.id)

    if chat_member.status in ['member', 'administrator', 'creator']:
        await query.message.reply_text("عضویت تأیید شد! اینم ویدیوی شما:")
        await query.message.reply_video(video=VIDEO_FILE_ID, caption="موفق باشید!")
    else:
        await query.message.reply_text("شما هنوز عضو کانال نشدید. لطفاً ابتدا عضو شوید و دوباره امتحان کنید!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler('start', start))
app.add_handler(CallbackQueryHandler(check_membership, pattern='check_membership'))

if __name__ == '__main__':
    app.run_polling()