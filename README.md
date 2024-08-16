# News Scraper API

This project is a Django-based web scraper that fetches news articles from a [azimjon.com](azimjon.com), stores them in a database, and exposes a RESTful API for managing and accessing the articles. Additionally, it includes a Telegram bot that interacts with the API to provide users with the latest news articles.

## Features

- Scrape news articles from a [azimjon.com](azimjon.com).
- RESTful API to manage and retrieve news articles.
- Telegram bot integration to provide users with the latest news.

## Requirements

- Python 3.8+
- Django 3.0+
- Django REST framework

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/cs-bekzod/getNews.git
```
### 2. Set Up a Virtual Environment
```bash
# On macOS and Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Create a superuser for access admin panel
```bash
python manage.py createsuperuser
access -> http://127.0.0.1:8000/admin
```
### 5. Run the server
```bash
python manage.py runserver
if you did all steps correct, API should now be running at http://127.0.0.1:8000/

to run telegram bot, python tgbot.py
```
### 5. Telegram bot address is [@getnewstestbot](https://t.me/getnewstestbot)
```bash
/start -> greetings
/latest -> get latest article
```

### API Endpoints

All API endpoints are powered by Django REST Framework:

- **Get All News Articles**: 
  ```bash
  GET /api/news/
  ```
- **Get Specific News by ID**:
  ```bash
  GET /api/news/<id>/
  ```
