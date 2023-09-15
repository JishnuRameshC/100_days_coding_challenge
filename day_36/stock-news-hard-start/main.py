import requests
from config import NEWS_API_KEY,STOCK_API_KEY,Account_SID,Auth_Token
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
stock_param = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey":STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT,params=stock_param)
data = response.json()['Time Series (Daily)']
data_list = [value for (key,value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday['4. close']

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_percent = round((difference/float(yesterday_closing_price)) * 100)
print(yesterday_closing_price,day_before_yesterday_closing_price,difference,diff_percent)

if abs(diff_percent) > 1:
    params = {
        'apiKey':NEWS_API_KEY,
        'q':COMPANY_NAME,
        "language":'en'
    }
    news_response = requests.get(NEWS_ENDPOINT,params)
    articles = news_response.json()["articles"]
    first_three_article =articles[:3]
    article_list = [f"\n\n{STOCK}:{up_down}{diff_percent}% \n Headline:{article['title']} \n\nBrief:{article['description']}" for article in first_three_article]
    print(article_list)

    client = Client(Account_SID, Auth_Token)
    for article in article_list:
        message = client.messages.create(
            body=article,
            from_='+12565988957',
            to='')
        print(message.sid)



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printin           g ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

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

