import yagmail
import pandas as pd
from news import NewsFeed
import datetime

df = pd.read_excel('people.xlsx')
#print(df)

for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=(datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                         to_date=datetime.datetime.now().strftime('%Y-%m-%d'),
                         language='en')
    email = yagmail.SMTP(user='pythonprocourse.amurthy@gmail.com', password='pythonprocourse_amurthy_1')
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}\n See what's on {row['interest']} today.\n {news_feed.get()}\nAbhishek")