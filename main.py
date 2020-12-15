import requests
from bs4 import BeautifulSoup


def main():
    urlName = "https://paperswithcode.com"
    url = requests.get(urlName)
    soup = BeautifulSoup(url.content, "html.parser")
    trends = soup.find_all('div', class_='col-lg-9 item-content')
    for trend in trends:
        title = trend.h1.a.text
        link = trend.h1.a.get("href")
        all_link = urlName + link
        print(all_link)
        abst = trend.find('p', class_='item-strip-abstract').text
    print(len(trends))
    # print(trends)

if __name__ == '__main__':
    main()
