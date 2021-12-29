This is currently a placeholder README that will be updated with more detailed instructions very soon. Thanks for understanding.


<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![MIT License][license-shield]][https://mit-license.org/]
![LinkedIn][linkedin-shield][https://www.linkedin.com/in/samuel-mcguire/]

<h3 align="center">Simple Scraper</h3>

<br />
<div align="center">
  <a href="https://github.com/SamuelAdamsMcGuire/simplescraper">
    <img src="images/scraper.png" alt="Logo">
  </a>



  <p align="center">
    project_description
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

After writing this program to help me scrape some sitemaps and eventually the links they scraped I though I would package it for repeated use. 

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is currently a placeholder README that will be updated with more detailed instructions very soon. Thanks for understanding.

### Prerequisites

This program used python 3.8

### Installation

Option 1 is to clone the repo and use the code but the simpler approach would be to `pip` install the package and use as needed. 

Install `pip` package
  ```sh
  pip install samssimplescraper==0.0.2
  ```

At this point in order to use the method `get_html()` please have the following folder structure inside of your project folder:
```
─ data
   ├── scraped_html
   └── pickled_lists
─ scraper.py
```
                
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The package has two modules. 

1. `sitemapscraper` is used to scrape sitemaps and can also scrape further levels of sub-sitemaps The methods will return lists of the scraped links that can be used to scrape the wanted links.
2. `scraper` is used to scrape the the list that is returned from the sitemapscraper or a user-made list of links. There is also a method that returns a status check of how many links have been scraped of the total. 

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [] Feature 1
- [] Feature 2
- [] Feature 3
    - [] Nested Feature

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

Project Link: [https://github.com/SamuelAdamsMcGuire/simplescraper](https://github.com/SamuelAdamsMcGuire/simplescraper)

<p align="right">(<a href="#top">back to top</a>)</p>
