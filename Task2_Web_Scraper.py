# Import libraries
import requests
from bs4 import BeautifulSoup

# Get the webpage
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract data
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# Print results
for i in range(len(quotes)):
    print(f"Quote: {quotes[i].text}")
    print(f"Author: {authors[i].text}")
    print("-" * 50)