# API key: bb7fbde2f77e4a8db8c1ee8736542e3e
import requests
from pprint import pprint

class NewsFeed:
    '''Representing multiple news titles and links as a single string'''

    base_url = 'https://newsapi.org/v2/everything?'
    api_key = 'bb7fbde2f77e4a8db8c1ee8736542e3e'

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f'{self.base_url}' \
              f'qInTitle={self.interest}&' \
              f'from={self.from_date}&' \
              f'to={self.to_date}&' \
              f'language={self.language}&' \
              f'apiKey={self.api_key}'

        response = requests.get(url)
        content = response.json()

        email_body = ''
        for article in content['articles']:
            email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n'

        return email_body


if __name__=="__main__":
    news_feed = NewsFeed(interest='nasa', from_date='2022-01-01', to_date='2022-01-02', language='en')
    print(news_feed.get())