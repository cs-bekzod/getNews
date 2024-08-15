import requests
from .models import NewsArticle
from datetime import datetime
from bs4 import BeautifulSoup

def get_news():
    
    url = 'https://azimjon.com/blog/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = []

    for detail in soup.find_all('ul', class_='list-wrapper')[:10]:
        title = detail.find('div', class_='title').text
        link = 'https://azimjon.com' + detail.find('a', class_='list-item')['href']
        published_at = detail.find('div', class_='date').text 
        datetime_format = datetime.strptime(published_at, "%d %B %Y")
        
        
        article_response = requests.get(link)
        article_soup = BeautifulSoup(article_response.content, 'html.parser')
        content = article_soup.find('article', class_='content').text

        NewsArticle.objects.update_or_create(
            link=link,
            defaults={
                'title': title,
                'content': content,
                'published_at': published_at,
                'datetime_format':datetime_format,
            }
        )

    return articles