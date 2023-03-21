import requests
from bs4 import BeautifulSoup

# Define endpoint for GET request
url = 'https://www.sensormatic.com/who-we-are/leadership-team/subramanian-kunchithapatham'

# Create string for output text
text = ""

# GET request for website HTML
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# Isolate the needed description and save it to text variable
for data in doc.find_all("p"):
    text = text + data.get_text()
print(text)

# Create a new text file and write the output text to it
with open('output.txt', 'w') as file:
    file.write(text)
