
import requests
from bs4 import BeautifulSoup
import csv

# BBC News RSS URL
url = "https://feeds.bbci.co.uk/news/rss.xml"

response = requests.get(url, timeout=15)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, "xml")

    news_list = []

    articles = soup.find_all("item")

    for article in articles:
        headline = article.find("title")
        date = article.find("pubDate")
        category = article.find("category")

        title = headline.get_text(strip=True) if headline else "N/A"
        pub_date = date.get_text(strip=True) if date else "N/A"
        category_name = category.get_text(strip=True) if category else "General"

        news_list.append([title, pub_date, category_name])

    # Save data into CSV
    with open("news_headlines.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Headline", "Publication Date", "Category"])
        writer.writerows(news_list)

    print("News headlines saved successfully!")
    print("Total articles:", len(news_list))

else:
    print("Failed to access website.")

