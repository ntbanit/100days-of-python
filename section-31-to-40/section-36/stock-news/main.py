import os
import requests
import smtplib
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
MY_ALPHA_VANTAGE_API_KEY = os.environ.get('MY_ALPHA_VANTAGE_API_KEY')
ALPHA_VANTAGE_API_URL = 'https://www.alphavantage.co/query'
ALPHA_VANTAGE_API_PARAMS = {
    'function': 'GLOBAL_QUOTE',
    'symbol': STOCK,
    'apikey': MY_ALPHA_VANTAGE_API_KEY
}
requests.packages.urllib3.disable_warnings()
response = requests.get(ALPHA_VANTAGE_API_URL, params=ALPHA_VANTAGE_API_PARAMS, verify=False)
response.raise_for_status()
data = response.json() 
percent_changed = float(data['Global Quote']['10. change percent'].replace('%', ''))

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
MY_NEWS_API_KEY = os.environ.get('MY_NEWS_API_KEY')
NEWS_API_URL = 'https://newsapi.org/v2/everything'
NEWS_API_PARAMS = {
    'q': COMPANY_NAME,
    'apiKey': MY_NEWS_API_KEY,
    'pageSize': 3
}
def get_articles():
    response = requests.get(NEWS_API_URL, params=NEWS_API_PARAMS, verify=False)
    response.raise_for_status()
    data = response.json()
    return data['articles']

## STEP 3: Send email notification
# Send a seperate message with the percentage change and each article's title and description to your email address

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
MY_SEND_EMAIL = os.environ.get('MY_SEND_EMAIL')
MY_SEND_EMAIL_PASSWORD = os.environ.get('MY_SEND_EMAIL_PASSWORD')
MY_CLIENT_EMAIL = os.environ.get('MY_CLIENT_EMAIL')
def send_email_news():
    articles = get_articles()
    icon = "🔺" if percent_changed > 0 else "🔻"
    message = f"Subject: Stock Alert: {COMPANY_NAME} {STOCK}: {icon} {percent_changed:.2f}%\n\n"
    for article in articles:
        message += f"Headline: {article['title']}\n"
        message += f"Brief: {article['description']}\n"
        message += f"Link: {article['url']}\n\n"
    message = message.encode('utf-8')
    
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_SEND_EMAIL, password=MY_SEND_EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_SEND_EMAIL, to_addrs=MY_CLIENT_EMAIL, msg=message)
        connection.close()

# if abs(percent_changed) > 5 :
send_email_news()
print("Get News")
print(percent_changed)
