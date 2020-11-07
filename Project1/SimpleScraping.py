import requests
from bs4 import BeautifulSoup
import pprint


# votes = soup.select('.score')
def create_soup_object(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html5lib')


def sort_hn_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k['vote'], reverse=True)


def create_custom_hn(links_list, subtext_list):
    hn = []
    for index, item in enumerate(links_list):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext_list[index].select('.score')
        if vote:
            points = int(vote[0].getText().replace(' points', ''))
            if points > 100:
                hn.append({'title': title, 'link': href, 'vote': points})
    return sort_hn_by_votes(hn)


soup_page1 = create_soup_object('https://news.ycombinator.com/news')
soup_page2 = create_soup_object('https://news.ycombinator.com/news?p=2')
links_page1 = soup_page1.select('.storylink')
subtext_page1 = soup_page1.select('.subtext')
links_page2 = soup_page2.select('.storylink')
subtext_page2 = soup_page2.select('.subtext')
mega_links = links_page1 + links_page2
mega_subtext = subtext_page1 + subtext_page2
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
