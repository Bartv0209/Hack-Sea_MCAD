const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');

const keyword = "ais-spoofing";

async function fetchArticles(keyword) {
    const url = `https://news.google.com/search?q=${encodeURIComponent(keyword)}`;
    try {
        const response = await axios.get(url);
        const html = response.data;
        const $ = cheerio.load(html);
        const articles = [];

        $('article').each((index, element) => {
            if (index < 10) {
                const title = $(element).find('h3').text();
                let link = $(element).find('a').attr('href');
                if (link && !link.startsWith('http')) {
                    link = `https://news.google.com${link.substring(1)}`;
                }
                articles.push({ title, link });
            }
        });

        console.log(`Fetched articles for keyword "${keyword}":`, articles);
        return articles;
    } catch (error) {
        console.error(`Error fetching articles for keyword "${keyword}": ${JSON.stringify(error, null, 2)}`);
        return [];
    }
}

async function scrapeAll() {
    const articles = await fetchArticles(keyword);

    const fileContent = articles.map(article => `${article.title}\n${article.link}`).join('\n\n');
    fs.writeFileSync('articles.txt', fileContent, 'utf8');
    console.log('Articles have been saved to articles.txt');
}

scrapeAll();