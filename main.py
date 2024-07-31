import os
import requests
from dotenv import load_dotenv
from send_email import send_email

TOPIC = "Tesla"
LANGUAGE = "en"
# Get env variables needed for this email automation
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


# Make the API call to get the news
url = f"https://newsapi.org/v2/everything?q={TOPIC.lower()}&sortBy=publishedAt&apiKey={news_api_key}&language={LANGUAGE}"
request = requests.get(url)
content = request.json()
email_body = ""

# Prepare the email message and send it 
for article in content["articles"][:20]:
    if article["title"] and article["url"] and article["description"]:
        email_body += article["title"] + "\n"
        email_body += article["url"] + "\n"
        email_body += (
            " ".join([word for word in article["description"].split(" ") if word])
            + "\n\n"
        )

email_message = f"""\
Subject: Today's news about {TOPIC}


{email_body}
"""

send_email(
    email_message=email_message.encode("utf-8"),
    email=email,
    password=password,
    receiver=receiver,
)
