# ApiNewsEmail
This app accesses news about a particular topic and sends them by email.

This application requires to have below information in a ```.env``` file in the work dir.
- news_api_key
- email
- password (gmail access api key)

In ```main.py``` you can change;
- ```TOPIC``` to your desired topic of news to get the email about.
- ```LANGUAGE``` to limit the language of the news to your preference. Options are: 'ar', 'de', 'en', 'es', 'fr', 'he', 'it', 'nl', 'no', 'pt', 'ru', 'sv', 'ud', 'zh'.


### Deploy the automation
- go to pythonanywhere.com
- create an account
- upload the repository files to the server.
- copy the main script's path.
- go to tasks on the pythonanywhere.com
- create a scheduled task for the main script path to run periodically.