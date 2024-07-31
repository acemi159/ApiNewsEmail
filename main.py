import os
import requests
from dotenv import load_dotenv
from send_email import send_email

try:
    load_dotenv(override=True)
except:
    print("No '.env' file exists")
    exit()
    
news_api_key = os.getenv("NEWS_API_KEY")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
receiver = os.getenv("EMAIL")

if not (news_api_key and email and password and receiver):
    raise KeyError("Missing Environment variables!")


url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-06-30&sortBy=publishedAt&apiKey={news_api_key}"


request = requests.get(url)
content = request.json()
email_body = ""

for article in content["articles"]:
    if article["title"] and article["url"] and article["description"]:
        current_news = ""
        current_news += article["title"] + "\n"
        current_news += article["url"] + "\n"
        current_news += " ".join([word for word in article["description"].split(" ") if word]) + "\n\n"
        
        email_body += current_news
    
email_message = f"""\
Subject: Today's news


{email_body}
"""

send_email(email_message=email_message.encode("utf-8"), email=email, password=password, receiver=receiver)