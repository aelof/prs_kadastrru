import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        print('oooops')


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    sorted_list = soup.find('div', id='postsList-Kadastr-RU.Блог').find('div', class_='postsLayout sortedList')
    posts = sorted_list.find_all('div', class_='postPreview large')
    for post in posts:
        name = post.find(class_='blogPreviewTitle').text.strip()
        date = post.find(class_='blogPostDate').text.strip()
        link = 'https://kadastrru.info' + post.find(class_='blogPreviewTitle').get('href') 
        print(name, date, link)

def main():
    url = 'https://kadastrru.info/ru/blog/'
    print('парсинг пошёл!')

    get_page_data(get_html(url))


if __name__ == '__main__':
    main()

