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
    Used to retrieve links from sitemaps.

    Parameters
    ----------
    url : string
        Must be valid sitemap URL for the desired website
    header : dict, optional
        Used to mask scraper as a browser to avoid being blocked
    folders : bool, default False
        Package depends on a defined folder strucure. This parameter
        will create it for user unless set to True.

    Attributes
    ----------
    None

    Methods
    -------
    get_sitemap_links()
    get_next_links()

    Examples
    -------
    >>> links_retriever = LinksRetriever(url='https://www.example.com/sitemap_index.xml')
    '''

    def __init__(self, url, header=HEADER, folders=False):
        self.url = url
        self.header = header
        if folders is False:
            os.makedirs('./data/pickled_lists/', exist_ok=True)
            os.makedirs('./data/scraped_html/', exist_ok=True)

    def get_sitemap_links(self, tag, link_filter=False):
        '''
        Retrieves all sitemap links from main sitemap based on a html tag the user sets.
        Optionally the links can be filtered by a user defined string

        Parameters
        ----------
        tag : string
        HTML tag used to locate the links to be scraped
        link_filter : string, optional
        Partial link sting used to filter for specific links

        Examples
        --------
        >>> links_retriever = LinksRetriever(url='https://www.example.com/sitemap_index.xml')
        >>> sitemap_links = links_retriever.get_sitemap_links(tag='loc',
                                                              filter='specific_lnk-sitemap')
        '''

        site_map = requests.get(self.url, headers=self.header)
        sitemap_soup = BeautifulSoup(site_map.text, 'html.parser')
        raw_sitemap_review_links = sitemap_soup.find_all(tag)
        sitemap_review_links = [link.text for link in raw_sitemap_review_links]
        if link_filter:
            filtered_sitemap_review_links = \
            [filtered_link for filtered_link in sitemap_review_links \
            if link_filter in filtered_link]
        else:
            return sitemap_review_links
        return filtered_sitemap_review_links

    def get_next_links(self, links, tag):
        '''
        Retrieves all links from each sitemap link according to user defined
        html tag and returns links as a list of strings.

        Parameters
        ----------
        links : list
        List of links from the scraped sitemap to further scrape another level
        tag : string
        HTML tag used to locate the links to be scraped

        Examples
        -------
        >>> links_retriever = LinksRetriever(url='https://www.example.com/sitemap_index.xml')
        >>> sitemap_links = links_retriever.get_sitemap_links(tag='loc',
                                                              filter='specific_lnk-sitemap')
        >>> total_links = links_retriever.get_next_links(links=sitemap_links, tag='loc')
        '''
        site_links = [requests.get(link, headers=self.header).text for link in tqdm(links)]
        soup_list = [BeautifulSoup(link, 'html.parser') for link in tqdm(site_links)]
        link_list=[]
        for soup in tqdm(soup_list):
            links = soup.find_all(tag)
            link_list += links
        cleaned_link_list = [link.text for link in link_list]
        return cleaned_link_list
        