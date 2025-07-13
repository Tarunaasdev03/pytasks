import requests
from bs4 import BeautifulSoup

url = "...."  # Replace with your target website
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract and display data
titles = soup.find_all("h2")
for title in titles:
    print(title.text)  # Prints data instead of storing it
