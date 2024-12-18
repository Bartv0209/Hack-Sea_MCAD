# Hack-Sea_MCAD

## Description

This project is a web scraper designed to search for and filter news articles related to maritime cyberattacks. The scraper uses Google News to find articles that match specific keywords related to both maritime activities and cyberattacks. The filtered articles are then saved to a text file for further analysis.

## Features

- **Scrape Google News**: Searches Google News for articles matching a specified query.
- **Filter Articles**: Filters the scraped articles to include only those related to maritime cyberattacks using predefined keywords.
- **Save to File**: Saves the filtered articles to a text file, including the title, URL, and snippet of each article.

## Files

- `scraper.py`: The main script that performs the web scraping, filtering, and saving of articles.
- `keywords.py`: Contains the lists of keywords related to maritime activities and cyberattacks.
- `sources.py`: (Optional) Contains a list of news sources if needed for further expansion.

## Usage

1. Ensure you have the required Python packages installed:
   ```sh
   pip install requests beautifulsoup4
