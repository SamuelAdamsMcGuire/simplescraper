<div id="top"></div>

<h3 align="center">Simple Scraper</h3>

<br />
<div align="center">
  <a href="https://github.com/SamuelAdamsMcGuire/simplescraper">
    <img src="images/scraper.png" alt="Logo">
  </a>


  <p align="center">
    <br />
    <a href="https://github.com/SamuelAdamsMcGuire/simplescraper"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/SamuelAdamsMcGuire/simplescraper">View Demo</a>
    ·
    <a href="https://github.com/SamuelAdamsMcGuire/simplescraper/issues">Report Bug</a>
    ·
    <a href="https://github.com/SamuelAdamsMcGuire/simplescraper/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

Wrote this program to scrape some sitemaps and the following sitemap links on multiple servers. In order to save time it was pip packaged for easy repeated use. 

<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

* [Python](https://www.python.org/)
* [Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Follow the installation instructions. The docstrings have detailed explainations for use. 

### Prerequisites

This program uses python 3.8

### Installation

`pip` install package and use as needed. 

Install `pip` package
  ```sh
  pip install samssimplescraper==0.1.3
  ```
                
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

The package has two modules. 

1. `sitemapscraper` is used to scrape sitemaps and can also scrape further levels of sub-sitemaps The methods will return lists of the scraped links that can be used to scrape the wanted links.
2. `scraper` is used to scrape the the list that is returned from the sitemapscraper or a user-made list of links. There is also a method that returns a status check of how many links have been scraped of the total. 

<!-- to do:_For more examples, please refer to the [Documentation](https://example.com)_-->

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

1. Find sitemap for the site you are looking to scrape. Some tips can be found here:

  [how-to-find-your-sitemap](https://writemaps.com/blog/how-to-find-your-sitemap/)
  https://writemaps.com/blog/how-to-find-your-sitemap/

2. Scrape sitemap:

```python
from samssimplescraper import LinksRetriever

# instantiate LinksRetriever with the sitemap you wish to scrape
links_retriever = LinksRetriever(url='https://www.example.com/sitemap_index.xml')
# get a list of the link using .get_sitemap_links method, can also add filter
mainpage_links = links_retriever.get_sitemap_links(tag='loc')
# if website has more layers use the method to get the links on those pages
final_links = links_retriever.get_next_links(links=mainpage_links, tag='loc')
```
**Note:** If you are not going to continue scraping in the same script then be sure to save your list using pickle:

```python 
import pickle

# the data folder is automatically created when LinksRetriever is instantiated
with open('./data/pickled_lists/sitemap_links_list.pkl', 'wb') as fp:
        pickle.dump(final_links, fp)
```

3. Now you can scrape the list of links that the `LinksRetriever` module has produced for you. The files will be saved in the `data/scraped_html` folder.

```python
from samssimplescraper import Scraper

# pass the list of links and for naming purposes the root_url
Scraper.get_html(link_list=final_links, root_url='https://www.example.com/)
``` 

See the [open issues](https://github.com/SamuelAdamsMcGuire/simplescraper/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Samuel Adams McGuire - samuelmcguire@engineer.com

Pypi Link: [https://pypi.org/project/samssimplescraper/0.1.3/](https://pypi.org/project/samssimplescraper/0.1.3/)

Linkedin: [LinkedIn](https://www.linkedin.com/in/samuel-mcguire/)

Project Link: [https://github.com/SamuelAdamsMcGuire/simplescraper](https://github.com/SamuelAdamsMcGuire/simplescraper)

<p align="right">(<a href="#top">back to top</a>)</p>
