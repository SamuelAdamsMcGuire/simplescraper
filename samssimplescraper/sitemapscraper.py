'''
Various methods that can be used to scrape a sitemap,
in turn scrape those links for more links and so on.
Can be filtered according to user's need and returned
as a list to scrape the entire site of specifics parts.
'''
import os
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup


HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

class LinksRetriever:
    '''
    used to retrieve links from sitemaps
    '''
    def __init__(self, url, header=HEADER, folders=False):
        self.url = url
        self.header = header
        if folders==False:
            os.makedirs('./data/pickled_lists/', exist_ok=True)
            os.makedirs('./data/scraped_html/', exist_ok=True)

    def get_sitemap_links(self, tag, filter=False):
        '''
        Retrieves all sitemap links from main sitemap based on a html tag the user sets.
        Optionally the links can be filtered by a user defined string
        '''

        site_map = requests.get(self.url, headers=self.header)
        sitemap_soup = BeautifulSoup(site_map.text, 'html.parser')
        raw_sitemap_review_links = sitemap_soup.find_all(tag)
        sitemap_review_links = [link.text for link in raw_sitemap_review_links]
        if filter:
            filtered_sitemap_review_links = \
            [filtered_link for filtered_link in sitemap_review_links \
            if filter in filtered_link]
        else:
            return sitemap_review_links
        return filtered_sitemap_review_links

    def get_next_links(self, links, tag):
        '''
        retrieves all links from each sitemap link according to user defined
        html tag and returns links as a list of strings
        '''
        site_links = [requests.get(link, headers=self.header).text for link in tqdm(links)]
        soup_list = [BeautifulSoup(link, 'html.parser') for link in tqdm(site_links)]
        link_list=[]
        for soup in tqdm(soup_list):
            links = soup.find_all(tag)
            link_list += links
        cleaned_link_list = [link.text for link in link_list]
        return cleaned_link_list
        