from bs4 import BeautifulSoup
import requests
import re
from sources import news_sources  # Import the list of news sources
from keywords import attack_related_keywords  # Import the list of attack-related keywords

def scrape_news_urls(urls):
    """
    Scrapes news articles from given URLs and extracts URLs of related cyberattacks.

    Args:
        urls: A list of URLs to scrape.

    Returns:
        A list of URLs related to cyberattacks in the maritime sector.
    """

    attack_urls = []

    for url in urls:
        try:
            print(f"Fetching URL: {url}")
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes
            print(f"Successfully fetched URL: {url}")
            soup = BeautifulSoup(response.content, "html.parser")

            # Extract text from the article
            article_text = " ".join(p.get_text() for p in soup.find_all("p"))
            print(f"Extracted article text from URL: {url}")

            # Find URLs in the article text
            urls_in_text = re.findall(r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', article_text)
            print(f"Found {len(urls_in_text)} URLs in the article text from URL: {url}")

            # Filter URLs based on keywords
            for found_url in urls_in_text:
                if any(keyword.lower() in found_url.lower() for keyword in attack_related_keywords):
                    attack_urls.append(found_url)
                    print(f"Found attack-related URL: {found_url}")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL: {url} - {e}")

    return list(set(attack_urls))  # Remove duplicates

# Scrape URLs
attack_urls = scrape_news_urls(news_sources)

# Write URLs to a text file
with open("attack_urls.txt", "w") as f:
    for url in attack_urls:
        f.write(url + "\n")

print("Attack URLs written to attack_urls.txt")