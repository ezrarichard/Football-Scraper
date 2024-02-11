
![EzraRichard_Banner (1)](https://github.com/ezrarichard/Football-Scraper/assets/125721936/855cc669-128c-490f-ad10-7df62e7af590)


# Football Data Scraping
This repository contains a Python script (fbref_scraper.py) that extracts football data from the top 5 European leagues, transforms it into a structured format, and saves it as a CSV file named all_leagues_2023_2024.csv. The script is scheduled to run via GitHub Actions every week to ensure that the data is regularly updated with the latest statistics.

## Instructions for Usage:
To utilize the football data extracted by the script for further analysis and visualization, follow these steps:

## Access the CSV File:
After each scheduled run, the updated CSV file (all_leagues_2023_2024.csv) will be available in the root directory of this repository.

## Download the CSV File:
You can download the CSV file directly from this repository by navigating to the file link and clicking on the "Download" button.

##Utilize the Data:
Once downloaded, you can use the CSV file for various data analysis and visualization tasks using your preferred tools and programming languages (e.g., Python, R, Excel, Tableau).

## About the Python Script:
The fbref_scraper.py Python script utilizes the requests and BeautifulSoup libraries to fetch football statistics from the top 5 European leagues from the FBRef website. It extracts various statistics such as team performance, possession, shooting, passing, and defensive metrics.

The script then merges the extracted data into a single DataFrame, updates column names, and saves the final result as a CSV file (all_leagues_2023_2024.csv). The CSV file contains detailed statistics for each team across different categories, facilitating in-depth analysis of football performance.

## Schedule:
The script is scheduled to run automatically via GitHub Actions every week according to the following schedule:

#### 10:30 PM UTC Saturday, Sunday, Monday, Tuesday 

Notes:
The CSV file is updated with the latest football statistics after each scheduled run.
You can customize the script or schedule according to your specific requirements by modifying the workflow configuration (main.yml) or the Python script (fbref_scraper.py).

## Need Help?

If you have any questions, encounter issues, or need further assistance, please don't hesitate to raise an issue ticket in this repository. Our team will be glad to assist you.

#### To raise an issue ticket:
1. Click on the "Issues" tab in the repository.
2. Click on the "New issue" button.
3. Provide a descriptive title and detailed description of your question or issue.
4. Submit the issue, and our team will respond to it promptly.

Your feedback is valuable to us, and we're committed to providing support to help you effectively utilize the football data extracted by this script.

---

*Disclaimer: This repository and script are provided for educational and analytical purposes only. The accuracy and reliability of the data obtained from external sources may vary. Users are encouraged to verify the data and exercise caution when interpreting the results.*

## Support
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Donate-yellow.svg)](https://www.buymeacoffee.com/ezrarichard)
