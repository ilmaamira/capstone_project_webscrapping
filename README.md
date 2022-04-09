# Capstone Project: Webscrapping using BeautifulSoup
This is a capstone project of Algoritma Data Science School: Data Analytics Specialization. This repository contains guidances and steps to do a simple webscrapping using BeautifulSoup. The expected deliverable from this project is doing a simple webscrapping to get information and insights.

Webscrapping is actually one of the methods to collect data from the internet. In this project, we will try to do a webscrapping, show the scrap results, and make some visualizations. Come join me and get started! 💞

## Case Background
In this project, we will try to scrap the historical data of Ethereum trading volume from CoinGecko site. CoinGecko is a site that provides the historical data and fundamental analysis of the cryptocurrencies. Ethereum, as the most popular cryptocurrency after Bitcoin, can be a beautiful target to analyze and discuss.

A lot of you might ask why we need to scrap data from the site, while it already has a good enough visualization. Let's say that you have task to make a forecast. To do that, you need to look at the data pattern that went before. In other words, you need to have the historical data, right? So, webscrapping is an effective way to collect them.

Never heard about forecasting? Keep calm, you don't need to worry about it. Because in this repository, we mainly discuss about webscrapping. But, in additional, we will also try to take insight from simple visualizations. The data that we use is Ethereum trading volume (in U.S. Dollar) from January 1, 2020 to June 30, 2021, hence we will take two points from the site, namely Date and Volume. See the original data in [here](https://www.coingecko.com/en/coins/ethereum/historical_data/usd?start_date=2020-01-01&end_date=2021-06-30#panel).

## Dependencies
The libraries we need:
- beautifulsoup4
- pandas
- matplotlib

## Disclaimer
You can see the full explanation in `.ipynb` file; and you can see the flask app using `app.py` and `index.html`.

Let's learn together~
