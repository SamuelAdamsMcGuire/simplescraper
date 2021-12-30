'''
script to scrape websites in their entirety and check the status of the scraping
'''
import os
import re
import time
import pickle
import random
import datetime
import requests
from tqdm import tqdm

HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

class Scraper():
    '''
    Scrapes a list of web links and saves them in a data folder.
    If scrape is unsuccessful the so-called bad links are saved
    for later inspection.

    Parameters
    ----------
    link_list : list
        List of links to scrape.
    root_url : string
        This string will be filtered out and the rest of the URL is
        used to name the html files in the scarped_html folder.
    header : dict, optional
        Used to mask scraper as a browser to avoid being blocked
    folders : bool, default False
        Package depends on a defined folder strucure. This parameter
        will create it for user unless set to True.

    Attributes
    ----------
    Nonw

    Methods
    -------
    get_html()
    get_check_status()

    Examples
    -------
    >>> scraper = Scraper(link_list=links, root_url='www.example.com')
    '''

    def __init__(self, link_list, root_url, folders=False, header=HEADER):
        self.link_list = link_list
        self.root_url = root_url
        self.header = header
        if folders is False:
            os.makedirs('./data/pickled_lists/', exist_ok=True)
            os.makedirs('./data/scraped_html/', exist_ok=True)

    def get_html(self):
        '''
        Loops through scraped list to scrape the each webpage in it's entirety.

        Examples
        --------
        >>> scraper.get_html()
        '''
        bad_links=[]
        finished_links = os.listdir('./data/scraped_html')
        for link in tqdm(self.link_list):
            page_name = re.sub(self.root_url, '', link)[:-1]
            if f'{page_name}.html' in finished_links:
                pass
            else:
                finished_links.append(f'{page_name}.html')
                url = link
                time.sleep(random.uniform(0.6, 1.8))
                try:
                    page_response = requests.get(url, headers=self.header)
                    if page_response.status_code == 200:
                        with open(f'./data/scraped_html/{page_name}.html', \
                           'w', encoding="utf8") as f:
                            f.write(page_response.text)
                    else:
                        bad_links.append(link)
                        with open('./data/pickled_lists/bad_links.pkl', 'wb') as fp:
                            pickle.dump(bad_links, fp)
                except requests.ConnectionError:
                    bad_links.append(link)
                    with open('./data/pickled_lists/bad_links.pkl', 'wb') as fp:
                        pickle.dump(bad_links, fp)
                    continue
        if len(bad_links) > 0:
            print(f"You have scraped {len(os.listdir('./data/scraped_html'))} pages so far")
            print(f'There are {len(bad_links)} \
            links that might not have been scraped. Check bad links file.')
        else:
            print(f"You have scraped {len(os.listdir('./data/scraped_html'))} pages so far")
            print('Scraping completed with no bad links!')

    def check_status(self):
        '''
        Checks the progress of the scraper if scraping is being done as a background process.

        Examples
        --------

        >>> scraper.check_status()
        '''
        page_data = os.listdir('./data/scraped_html')

        print(f'As of {datetime.datetime.now()} you have successfully scraped \
        {len(page_data)} of {len(self.link_list)} pages!')

        try:
            with open('./data/pickled_lists/bad_links.pkl', 'rb') as fp:
                bad_links = pickle.load(fp)
            print(f'Currently there are {len(bad_links)} bad links to look into.')
        except (SyntaxError, EOFError):
            print('Currently there are 0 bad links to look into.')
