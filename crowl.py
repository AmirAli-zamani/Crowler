from bs4 import BeautifulSoup
import json
import os

def find_links(html_doc):
    # Parse HTML document
    soup = BeautifulSoup(html_doc, 'html.parser')
    # Find all links with specific class
    links = soup.find_all('a', attrs={'class': 'rowCard__title'})
    result = []
    for link in links:
        title_text = link.get_text(strip=True)  # Extract title text
        href = link.get('href')  # Extract URL
        result.append((title_text, href))
    return result

def store_data(data, filename):
    # Ensure the directory exists
    os.makedirs('store', exist_ok=True)
    # Save the data to a JSON file
    with open(f'store/{filename}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f'Saved to store/{filename}.json')

# Testing the storage function
test_data = {"test": "This is a test"}
store_data(test_data, 'test_file')