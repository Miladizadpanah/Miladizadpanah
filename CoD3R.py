import time
from telegram.ext import Updater, CommandHandler

# توکن ربات خود را اینجا وارد کنید
TOKEN = '6091544216:AAF_Eg59uNY29gAKv8H27_MXZXlvCDBmIBA'

def start(update, context):
    update.message.reply_text('ربات آماده است!')

def set_timer(update, context):
    context.user_data['start_time'] = time.time()
    context.user_data['remaining_time'] = 40
    update.message.reply_text(' فقط ۵ ثانیه زمان باقی مانده است ')

def check_timer(update, context):
    if 'start_time' in context.user_data:
        elapsed_time = time.time() - context.user_data['start_time']
        remaining_time = 40 - int(elapsed_time)
        
        if remaining_time <= 0:
            update.message.reply_text('زمان تمام شد!')
            context.user_data.clear()
        elif remaining_time == 5:
            update.message.reply_text('فقط ۵ ثانیه باقی مانده!')
        elif remaining_time % 10 == 0:
            update.message.reply_text(f'{remaining_time} ثانیه باقی مانده.')

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('45s', set_timer))
    dispatcher.add_handler(CommandHandler('check', check_timer))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
