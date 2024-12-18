import requests
from bs4 import BeautifulSoup
import re
from keywords import maritime_keywords, cyberattack_keywords

def scrape_google_news(query):
    """
    Scrapes Google News for articles matching the query.

    Args:
        query: The search query.

    Returns:
        A list of dictionaries, where each dictionary represents an article.
    """
    url = f"https://www.google.com/search?q={query}&tbm=nws"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    articles = []

    for item in soup.select("div.dbsr"):
        title = item.select_one("div.JheGif.nDgy9d").text
        url = item.a["href"]
        snippet = item.select_one("div.Y3v8qd").text
        articles.append({"title": title, "url": url, "snippet": snippet})

    return articles

def filter_articles(articles, maritime_keywords, cyberattack_keywords):
    """
    Filters articles to include only those related to maritime cyberattacks.

    Args:
        articles: A list of dictionaries, where each dictionary represents an article.
        maritime_keywords: A list of maritime-related keywords.
        cyberattack_keywords: A list of cyberattack-related keywords.

    Returns:
        A list of filtered articles.
    """
    filtered_articles = []
    for article in articles:
        if any(mk in article["title"].lower() or mk in article["snippet"].lower() for mk in maritime_keywords) and \
           any(ck in article["title"].lower() or ck in article["snippet"].lower() for ck in cyberattack_keywords):
            filtered_articles.append(article)
    return filtered_articles

if __name__ == "__main__":
    query = "cyberattack"
    articles = scrape_google_news(query)
    filtered_articles = filter_articles(articles, maritime_keywords, cyberattack_keywords)

    if filtered_articles:
        print("Found articles on maritime cyberattacks:")
        with open("maritime_cyberattacks_articles.txt", "w", encoding="utf-8") as file:
            for article in filtered_articles:
                file.write(f"Title: {article['title']}\n")
                file.write(f"URL: {article['url']}\n")
                file.write(f"Snippet: {article['snippet']}\n")
                file.write("-" * 20 + "\n")
                print(f"Title: {article['title']}")
                print(f"URL: {article['url']}")
                print(f"Snippet: {article['snippet']}")
                print("-" * 20)
    else:
        print("No articles found on maritime cyberattacks.")