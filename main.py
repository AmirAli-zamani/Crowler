import requests
from crowl import find_links, store_data

if __name__ == '__main__':
    url_base = 'https://vigiato.net/daily-timeline/page/{}?skip=585545'

    all_links_and_titles = []

    for page_num in range(1, 10):
        url = url_base.format(page_num)
        response = requests.get(url)

        if response.status_code == 200:
            html_doc = response.text
            links = find_links(html_doc)
            all_links_and_titles.extend(links)
            store_data(links, f'links{page_num}')

            print(f"Page {page_num}: Found {len(links)} links.")
            for title_text, href in links:
                print(f"URL: {href}, Title Text: {title_text}")
        else:
            print(f"Failed to retrieve page {page_num}")

    # Save all collected links and titles to a single file
    store_data(all_links_and_titles, 'all_links_and_titles')
