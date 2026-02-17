from bs4 import BeautifulSoup

html = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Extract title
print("Title:", soup.title.text)

# Extract h1
print("H1:", soup.h1.text)

# Extract paragraph
print("Paragraph:", soup.p.text)

html = '<a href="https://example.com">Click Here</a>'

soup = BeautifulSoup(html, "html.parser")

a_tag = soup.find("a")

print("Link Text:", a_tag.text)
print("Href:", a_tag["href"])

print(soup.prettify())

html = """
<div class="product">
  <h2 class="name">iPhone 14</h2>
  <span class="price">$999</span>
  <span class="rating">4.5</span>
  <span class="availability">In Stock</span>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

product_name = soup.find("h2", class_="name").text
price = soup.find("span", class_="price").text
rating = soup.find("span", class_="rating").text
availability = soup.find("span", class_="availability").text

print("Product:", product_name)
print("Price:", price)
print("Rating:", rating)
print("Availability:", availability)

html = """
<img src="image1.jpg">
<img src="image2.png">
"""

soup = BeautifulSoup(html, "html.parser")

images = soup.find_all("img")

for img in images:
    print(img["src"])

print()

import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Print all links
for link in soup.find_all("a"):
    print(link.get("href"))
