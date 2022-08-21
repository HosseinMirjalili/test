import requests
from bs4 import BeautifulSoup
from abc import ABC
from abc import abstractproperty

class Bot_site(ABC):
    @abstractproperty
    def get_Html(self , url):
        res = requests.get(url)
        return res.text

    @abstractproperty
    def get_Tag(self , html , tag , attrbiute=None):
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find(tag , attrs=attrbiute)
        return tags

    @abstractproperty
    def get_Tags(self , html , tag , attrbiute=None):
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all(tag , attrs=attrbiute)
        return tags

    @abstractproperty
    def text_Tag(self , html , tag):
        soup = BeautifulSoup(html , 'html.parser')
        text = tag.text
        return text

    @abstractproperty
    def text_Tags(self , html , list_tags):
       soup = BeautifulSoup(html , 'html.parser')
       for tag in list_tags:
           print(tag.text)

    @abstractproperty
    def get_tag_in_tag(self , list_tag , tag):
        list1 = []
        for i in list_tag:
            for a in i.find_all(tag):
                list1.append(a)
        return list1

    @abstractproperty
    def get_links_in_tag(self ,  list_tag):
        links = []
        for i in list_tag:
            for tag_a in i.find_all('a'):
                if tag_a.has_attr('href'):
                    href = tag_a.attrs['href']
                    links.append('https://www.irna.ir/' + href)
        return links



