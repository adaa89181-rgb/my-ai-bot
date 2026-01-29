import telebot
import requests

# আপনার টেলিগ্রাম টোকেন ও জেমিনি কি
BOT_TOKEN = "8597077623:AAEuo4OwWMUjKpoTeEUq4772Rq4Wf5APDck"
GEMINI_KEY = "AIzaSyCAmJTr1vYPxf9otLjT1_q2foIxsK2TpCI"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda m: True)
def chat(message):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
    payload = {"contents": [{"parts": [{"text": message.text}]}]}
    try:
        r = requests.post(url, json=payload)
        response_data = r.json()
        bot.reply_to(message, response_data['candidates'][0]['content']['parts'][0]['text'])
    except Exception as e:
        bot.reply_to(message, "সার্ভার এখন ব্যস্ত ভাই!")

bot.infinity_polling()
