from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

articles = soup.select('span.titleline > a')
article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get('href')
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.select('span.score')]

max_upvotes = max(article_upvotes)
max_upvotes_index = article_upvotes.index(max_upvotes)
max_upvotes_text = article_texts[max_upvotes_index]
max_upvotes_link = article_links[max_upvotes_index]

print(max_upvotes_text)
print(max_upvotes_link)
print(max_upvotes)