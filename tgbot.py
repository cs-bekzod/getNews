import telebot
import requests

BOT_TOKEN = '7501703426:AAFb7GRNIAoMHalspE0_SPGs3lIVQDV8BJQ'
API_URL = 'http://127.0.0.1:8000/api/news/'  

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "GetNews botiga xush kelibsiz!\n"
        "Ushbu bot yordamida azimjon.com saytidagi eng yangi postlarni o`qishingiz mumkin. Eng oxirgi postni olish uchun /latest ni bosing."
    )
    bot.send_message(message.chat.id, welcome_text)
    
@bot.message_handler(commands=['latest'])
def send_latest_news(message):
    
    response = requests.get(API_URL, params={'ordering': '-published_at'})
    
    if response.status_code == 200:
        news_articles = response.json()
        if news_articles:
            latest_news = news_articles[0] 
            title = latest_news.get('title')
            content = latest_news.get('content')
            link = latest_news.get('link')
            published_at = latest_news.get('published_at')

            
            message_text = (
                f"*Latest News:*\n"
                f"*Title: * {title}\n"
                f"*Published Date: * {published_at}\n"
                f"*Link: * {link}\n"
                f"*Description: * {content[:100]}...\n"
            )
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

# Start the bot
if __name__ == '__main__':
    bot.polling(none_stop=True)